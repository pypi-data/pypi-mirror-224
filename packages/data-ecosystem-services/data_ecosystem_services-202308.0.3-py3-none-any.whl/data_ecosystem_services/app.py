"""
This module, app.py, serves as the primary entry point to the Program Agnostic Data Ecosystem (PADE) application. It initializes the application and sets up the endpoints for various services, including Alation.

The Alation service is specifically designed to manage and monitor Alation. It provides the following API endpoints:

    GET /alation/metadata_excel_file_download/{schema_id}: Retrieves an Excel metadata file from Alation based on the provided schema_id.
    POST /alation/metadata_excel_file_upload: Uploads an Excel metadata file to Alation via direct upload.
    GET /alation/metadata_json_file_download/{schema_id}: Retrieves a JSON metadata file from Alation based on the provided schema_id.
    POST /alation/metadata_json_file_upload: Uploads a JSON metadata file to Alation via direct upload.

The module also integrates other services of the PADE, which include CDC Tech Environment service, Azure Key Vault service, CDC Self Service, CDC Admin service, CDC Security service, and Posit service.

Besides, it includes HTTP enforcement, logging, exception handling, metrics reporting to Azure Monitor, and telemetry instrumentation functionalities.

The app is primarily designed to serve as an HTTP server for the PADE, exposing various functionalities as HTTP endpoints for file uploads, downloads, log access, and error presentation.

Usage:
python app.py
"""

import sys
import os
import time
import traceback
from datetime import datetime
import json
import base64
import ast
import requests
import jwt
from jwcrypto import jwk
from urllib.parse import urlencode, quote_plus, urlparse, urlunparse, unquote
from functools import wraps
from werkzeug.datastructures import FileStorage
from requests.exceptions import RequestException
from flask import redirect, send_file, request, render_template, Blueprint, jsonify, make_response
from flask_restx import Resource, fields
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from azure.monitor.opentelemetry.exporter import AzureMonitorMetricExporter
from azure.identity import DefaultAzureCredential, ClientSecretCredential

try:
    from data_ecosystem_services.app_startup import create_api, create_app
except ModuleNotFoundError as ex:
    trace_msg = traceback.format_exc()
    line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
    error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg}"
    exc_info = sys.exc_info()
    # logger_singleton.error_with_exception(error_message, exc_info)
    raise ModuleNotFoundError

from data_ecosystem_services.alation_service import (
    db_schema as alation_schema
)
from data_ecosystem_services.cdc_tech_environment_service import (
    environment_file as cdc_env_file
)
from data_ecosystem_services.az_key_vault_service import (
    az_key_vault as pade_az_key_vault
)
from data_ecosystem_services.cdc_admin_service import (
    environment_tracing as cdc_env_tracing,
    environment_logging as cdc_env_logging
)
from data_ecosystem_services.cdc_security_service import (
    security_core as pade_security_core,
)
from data_ecosystem_services.posit_service import (
    posit_connect as pade_posit_connect
)

TIMEOUT_5_SEC = 5
TIMEOUT_ONE_MIN = 60
# Get the currently running file name
SERVICE_NAME = os.path.basename(__file__)
# Get the parent folder name of the running file
NAMESPACE_NAME = os.path.basename(os.path.dirname(__file__))
ENVIRONMENT = 'dev'

print(f"SERVICE_NAME:{SERVICE_NAME}")
print(f"NAMESPACE_NAME: {NAMESPACE_NAME}")
sys.path.append(os.getcwd())
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_dir)

app = create_app()

# Define the blueprint
cdc_admin_bp = Blueprint('logs', __name__,
                         url_prefix='/logs')

# Define the blueprint
cdc_files_bp = Blueprint('files', __name__,
                         url_prefix='/files')

cdc_files_protected_bp = Blueprint('protected_files', __name__,
                                   url_prefix='/protected_files')


def jwk_to_pem(jwk_dict):
    """
    Converts a JSON Web Key (JWK) into Public Key in PEM format.

    The function uses the jwcrypto library to convert a JWK from dictionary 
    format to a JWK object, then exports this JWK object to a public key in 
    PEM format.

    Args:
        jwk_dict (dict): A dictionary representing the JWK to be converted.

    Returns:
        str: A string representing the Public Key in PEM format.

    Note:
        This function involves using additional cryptography libraries, which 
        might not be desirable in some cases due to increased complexity and 
        potential security implications. Be sure to validate this approach fits 
        into your security requirements before using it.
    """
    jwk_key = jwk.JWK()
    jwk_key.import_key(**jwk_dict)
    public_key = jwk_key.export_to_pem(private_key=False, password=None)
    return public_key.decode()


def azure_ad_authentication(func):
    """
    Decorator to protect the function using Azure AD authentication.

    This decorator checks the access token provided in the 'Authorization' header
    of the request for validity using Azure AD. If the token is valid, the original
    function is called. Otherwise, a 401 Unauthorized response is returned.

    Args:
        func (function): The function to be protected.

    Returns:
        function: A wrapped function that performs Azure AD authentication
                  before calling the original function.

    Raises:
        None.

    Example:
        @api.route('/protected_page')
        class ProtectedPageResource(Resource):
            @azure_ad_authentication
            def get(self):
                # Your logic to render the template
                return render_template('protected_template.html')

    Note:
        The `azure_credential` should be set up with the appropriate Azure AD
        credentials before using this decorator.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            # Get the access token from the request headers
            id_token = request.cookies.get('id_token')

            if id_token is None:
                raise Exception("No id_token found in request")
            else:
                # TODO Implement validation
                decoded_token = validate_id_token(id_token)

                # If the token is valid, call the original function
                original_response = func(*args, **kwargs)

                # Now you can access claims in the token, like the user's ID
                # 'oid' stands for Object ID
                user_id = decoded_token.get('unique_name')

                flask_response = make_response(original_response)

                # Set the user_id as a secure cookie on the response
                flask_response.set_cookie(
                    'user_id', user_id)
                # Set the user_id as a secure cookie on the response
                # TODO:  secure=True,
                flask_response.set_cookie(
                    'id_token', httponly=True, secure=True)

                flask_response.headers['Authorization'] = f'Bearer {id_token}'
                return flask_response

        except Exception as ex_not_authenticated:
            logger.warning(
                f"Error: not authenticated: {str(ex_not_authenticated)}")

            response = get_login_redirect_response()
            # Return the response, which includes the expired cookie and the redirect
            return response

    return wrapper


def get_login_redirect_response():

    config = app.cdc_config
    tenant = config.get("tenant_id")
    client_id = config.get("client_id")

    # Define the base URL for Azure AD authorization
    base_url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize"

    current_url = request.url

    # Define your data
    data = {
        'redirect_url': current_url
    }

    # Convert the data to JSON
    json_data = json.dumps(data)

    # Encode the JSON data as bytes
    json_bytes = json_data.encode('utf-8')

    # Base64 encode the bytes
    base64_data = base64.urlsafe_b64encode(json_bytes)

    # Convert the base64 bytes to a string
    base64_string = base64_data.decode('utf-8')

    callback_url = get_callback_url()

    state = base64_string

    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": callback_url,
        "response_mode": "query",
        "scope": "openid",
        "state": state,  # Replace with a secure, random state
    }

    # URL encode the parameters
    params_encoded = urlencode(params, quote_via=quote_plus)

    # Construct the full Azure AD authorization URL
    auth_url = f"{base_url}?{params_encoded}"

    # Create a response object with the redirect
    response = make_response(redirect(auth_url))

    # Expire the 'id_token' cookie
    # TODO  secure=True,
    response.set_cookie('id_token', httponly=True, secure=True)

    return response


def get_callback_url():
    # Get the current URL
    current_url = request.url

    # Parse the current URL into components
    url_parts = urlparse(current_url)

    # Split the path into directories
    directories = url_parts.path.split('/')

    # Remove the last directory (i.e., go up one directory)
    directories = directories[:-2]

    # Add 'callback' to the list of directories
    directories.append('cdc_security/callback')

    # Join the directories back into a path
    new_path = '/'.join(directories)

    # Azure AD auth will only work on local host not ip adress
    if os.name == 'nt':  # 'nt' is the name for Windows in the os module
        new_path = new_path.replace("127.0.0.1", "localhost")

    # Create a new URL with the new path
    callback_url = urlunparse(
        (url_parts.scheme, url_parts.netloc,
         new_path, None, None, None)
    )

    return callback_url


def enforce_https(function_name):
    """
    Decorator function to enforce HTTPS. If a request is made using HTTP,
    it redirects the request to HTTPS.

    Args:
        function_name (function): The Flask view function to decorate.

    Returns:
        function: The decorated function.
    """
    @wraps(function_name)
    def decorated(*args, **kwargs):
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)
        return function_name(*args, **kwargs)
    return decorated


def get_datetime(entry):

    date_string = entry[0]
    if date_string == '0001-01-01 00:00:00':
        # Handle the specific string and return a valid datetime object
        return datetime.min
    try:
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    except Exception as ex:
        msg = f"Error processing {entry}.  Could not convert '{date_string}' to a datetime object. Please check if it matches the format %Y-%m-%d %H:%M:%S'. Error: {str(ex)}"
        print(msg)

        # return datetime.min to sort invalid dates to the beginning, or datetime.max to sort them to the end
        return datetime.min


@cdc_files_bp.route('/download')
def download():
    calling_page_url = request.args.get('calling_page')
    return render_template('download.html', calling_page_url=calling_page_url)


@cdc_files_protected_bp.route('/upload')
@azure_ad_authentication
def upload():
    calling_page_url = request.args.get('calling_page')
    return render_template('upload.html', calling_page_url=calling_page_url)


@cdc_admin_bp.route('/error')
def error():
    error_message = "An unexpected error occurred"
    return render_template('error.html', error_message=error_message, error_url="")


@cdc_admin_bp.route('/get_log_file_tail/<int:number_of_lines>')
def get_log_file_tail(number_of_lines):
    """Get the last n lines of the log file"""

    logger_singleton = cdc_env_logging.LoggerSingleton.instance(
        calling_namespace_name=NAMESPACE_NAME, calling_service_name=SERVICE_NAME)

    with tracer.start_as_current_span(f"get_log_file_tail"):

        try:

            log_data = None

            status_code, number_of_lines, log_data = logger_singleton.get_log_file_tail(
                number_of_lines)
            if status_code == 500:
                error_msg = f"Internal Server Error fetching log file: The server encountered an error. {log_data}"
                raise Exception(error_msg)

            if log_data is None:
                raise ValueError(
                    f"Internal Server Error fetching log file: Log data is None. {log_data}")

            if number_of_lines is None or number_of_lines == 0:
                raise ValueError(
                    f"Internal Server Error fetching log file: number_of_lines is missing or blank")

            log_entries = []

            for line_number, line in enumerate(log_data.strip().split('\n'), start=1):
                log_entries.append(line.split('\u001F'))

            for entry in log_entries:
                try:
                    asctime, name, module, lineno, levelname, message = entry
                    datetime_object = datetime.strptime(
                        asctime, "%Y-%m-%d %H:%M:%S")
                    asctime = datetime_object.strftime("%Y-%m-%d %I:%M:%S %p")
                    entry = [asctime, name, module, lineno, levelname, message]
                except ValueError as ex:
                    logger.warning(f"Error parsing line: {str(ex)}")
                except IndexError:
                    logger.warning(f"Error: line has missing fields: {entry}")

            # Sort log_entries by date and time in descending order
            log_entries.sort(
                key=lambda entry: get_datetime(entry), reverse=True)

            return render_template('log_file.html', entries=log_entries)

        except Exception as ex:
            trace_msg = traceback.format_exc()
            line_number = traceback.extract_tb(ex.__traceback__)[-1].lineno
            error_message = f"An unexpected error occurred: {ex} at line {line_number}\nCall Stack:{trace_msg}"
            exc_info = sys.exc_info()
            # logger_singleton.error_with_exception(error_message, exc_info)
            return render_template('error.html', error_message=error_message)


app.register_blueprint(cdc_admin_bp)
app.register_blueprint(cdc_files_bp)
app.register_blueprint(cdc_files_protected_bp)

metric_exporter = AzureMonitorMetricExporter()

logger = app.logger
tracer = app.tracer

FlaskInstrumentor().instrument_app(app)

API_DESCRIPTION = '''
<h2>API Documentation</h2>
<p>The Program Agnostic Data Ecosystem (PADE) provides shared resources,
practices and guardrails for analysts to discover, access, link, and use
agency data in a consistent way. PADE improvements in standardized and 
streamlined workflows reduce the effort required to find, access, and
trust data.</p>
<p><a href="protected_files/upload">Upload Page</a></p>
<p><a href="files/download">Download Page</a></p>
<p>For detailed logs, please visit the <a href="logs/get_log_file_tail/1000">Log File Page</a>.</p>
'''

api, ns_welcome, ns_alation, ns_jira, ns_posit, ns_cdc_admin, ns_cdc_security = create_api(
    app, API_DESCRIPTION)

# Set Azure AD credentials using DefaultAzureCredential
azure_credential = DefaultAzureCredential()

# Define a model for the metadata
metadata_model = api.model('Metadata', {
    'start_time': fields.Float,
    'end_time': fields.Float,
    'total_time': fields.Float,
    'data': fields.String
})

# Define the file link model
file_link_model = api.model('FileLink', {
    'link': fields.String(description='Download link for the metadata file')
})


def get_posit_api_key():

    with tracer.start_as_current_span(f"get_posit_api_key"):

        config = app.cdc_config

        posit_connect_base_url = config.get("posit_connect_base_url")

        logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
        az_kv_az_sub_client_secret_key = config.get(
            "az_kv_az_sub_client_secret_key")
        az_kv_az_sub_client_secret_key = az_kv_az_sub_client_secret_key.replace(
            "-", "_")
        client_secret = os.getenv(az_kv_az_sub_client_secret_key)
        tenant_id = config.get("tenant_id")
        client_id = config.get("client_id")
        az_kv_key_vault_name = config.get("az_kv_key_vault_name")
        running_interactive = False
        if not client_secret:
            running_interactive = True

        az_key_vault = pade_az_key_vault.AzKeyVault(
            tenant_id, client_id, client_secret, az_kv_key_vault_name, running_interactive)

        az_kv_posit_connect_secret_key = config.get(
            "az_kv_posit_connect_secret_key")

        az_kv_posit_connect_secret = az_key_vault.get_secret(
            az_kv_posit_connect_secret_key)

        return az_kv_posit_connect_secret


def get_access_token():
    """
    Retrieves an access token using the Azure Active Directory client secret credential.

    The function uses a client secret credential, which consists of the tenant ID, client ID,
    and client secret, to authenticate with Azure Active Directory and obtain an access token.
    The access token can then be used to authenticate requests to Azure services.

    The configuration settings and client secret are retrieved from the environment variables.

    Returns:
    str: The access token.

    Raises:
    azure.core.exceptions.ClientAuthenticationError: If there's a problem with
        client authentication, such as an invalid client secret.

    Note:
    Ensure that the required environment variables are set and the necessary permissions
    are granted in Azure AD for the app registration. The client secret should be stored securely,
    and it's recommended to use a secure method to retrieve it (such as Azure Key Vault).
    """

    config = app.cdc_config
    az_kv_az_sub_client_secret_key = config.get(
        "az_kv_az_sub_client_secret_key")
    az_kv_az_sub_client_secret_key = az_kv_az_sub_client_secret_key.replace(
        "-", "_")
    client_secret = os.getenv(az_kv_az_sub_client_secret_key)
    tenant_id = config.get("tenant_id")
    client_id = config.get("client_id")

    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    token = credential.get_token("https://management.azure.com/.default")
    return token.token


def validate_id_token(id_token):
    """
    Validates an ID token received from Azure Active Directory (Azure AD).

    This function retrieves the OpenID Connect metadata document for the tenant,
    obtains the JSON Web Key Set (JWKS), locates the signing key matching the `kid` (Key ID) in the token header,
    and then decodes and verifies the ID token using the found key.

    Parameters:
    id_token (str): The ID token to validate.

    Returns:
    dict: The decoded ID token if the token is valid.

    Raises:
    ValueError: If unable to find the signing key for the token.

    Note:
    This function performs basic ID token validation which includes signature verification, 
    and checking of the audience ('aud') claim. Depending on the requirements of your application, 
    you might need to perform additional validation, such as checking the issuer ('iss') claim, 
    token expiration, etc.

    Ensure that your Azure AD tenant, client ID and client secret are correctly set in your application configuration.

    """

    config = app.cdc_config
    tenant_id = config.get("tenant_id")
    client_id = config.get("client_id")

    # Get the OpenID Connect metadata document
    openid_config_url = f"https://login.microsoftonline.com/{tenant_id}/v2.0/.well-known/openid-configuration"
    openid_config_response = requests.get(openid_config_url)
    openid_config = openid_config_response.json()

    # Decode the token header without validation to get the kid
    token_header = jwt.get_unverified_header(id_token)
    kid = token_header["kid"]

    # Get the signing keys
    jwks_url = openid_config["jwks_uri"]
    jwks_response = requests.get(jwks_url)
    jwks = jwks_response.json()

    # Find the key with the matching kid
    key = next((k for k in jwks["keys"] if k["kid"] == kid), None)
    if key is None:
        raise ValueError("Unable to find the signing key for the token.")

    # Use the function
    public_key = jwk_to_pem(key)

    # Validate the token
    try:

        # Decode the JWT without verification
        decoded_token = jwt.decode(
            id_token, options={"verify_signature": False})

        # Todo add back signature verificaiton
        # decoded_token = jwt.decode(id_token, public_key, algorithms=["RS256"], audience=client_id)

    except Exception as e:
        print(f"Failed to decode token: {e}")

    return decoded_token


def get_id_token_from_auth_code(auth_code):
    """
    Exchange an authorization code for an access token from Azure AD.

    This function sends a POST request to the Azure AD token endpoint with the
    provided authorization code and application's client ID, secret, and redirect URI.
    If the request is successful, the function returns the access token.

    Args:
        auth_code (str): The authorization code received from Azure AD.
        redirect_uri (str): The redirect URI of your application as registered in Azure AD.

    Returns:
        str: The access token if the request is successful; None otherwise.

    Example:
        access_token = get_id_token_from_auth_code(auth_code, redirect_uri)
        if access_token:
            print("Successfully received access token.")
        else:
            print("Failed to receive access token.")

    Note:
        Replace the "client_id", "client_secret", and "tenant_id" placeholders with your actual Azure AD client ID, 
        client secret, and tenant ID. The redirect_uri must match exactly with the one used in the authorization 
        request and the one configured in your Azure AD app registration.

        The function does not handle errors. In a production environment, you should add error handling code to 
        deal with potential issues, like network errors or an invalid authorization code.
    """

    logger_singleton = cdc_env_logging.LoggerSingleton.instance(
        calling_namespace_name=NAMESPACE_NAME, calling_service_name=SERVICE_NAME)

    config = app.cdc_config
    az_kv_az_sub_client_secret_key = config.get(
        "az_kv_az_sub_client_secret_key")
    az_kv_az_sub_client_secret_key = az_kv_az_sub_client_secret_key.replace(
        "-", "_")
    client_secret = os.getenv(az_kv_az_sub_client_secret_key)
    tenant_id = config.get("tenant_id")
    client_id = config.get("client_id")

    # Azure AD token endpoint
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    callback_url = get_callback_url()

    # Data for the token request
    token_data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": callback_url,
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "openid"
    }

    # If the request was successful, return the access token
    try:
        # Send a POST request to the token endpoint
        response = requests.post(token_url, data=token_data)
        response.raise_for_status()
        return response.json()["access_token"]
    except Exception as ex:
        msg = f"An unexpected error occurred: {str(ex)}"
        if 'response' in locals():  # Check if 'response' is defined
            msg += f" Response text: {response.text}"
        exc_info = sys.exc_info()
        # logger_singleton.error_with_exception(msg, exc_info)
        logger_singleton.force_flush()
        return {"error": f"An unexpected error occurred: {msg}"}


class AuthCallback(Resource):
    def get(self):

        url_with_error = request.url

        # Get the authorization code from the response
        auth_code = request.args.get('code')

        if auth_code is None:
            return {"error": f"Missing authorization code in url {url_with_error}"}, 400

        # Get the authorization code and state from the response
        state = request.args.get('state')

        if state is None:
            return {"error": f"Missing state parameter in url {url_with_error}"}, 400

        base64_string = state

        # Get the redirect_url from the query parameters and unquote it
        # redirect_url = unquote(request.args.get('redirect_url'))
        # Base64 decode the string
        decoded_bytes = base64.urlsafe_b64decode(base64_string)

        # Decode the bytes to a string
        decoded_string = decoded_bytes.decode('utf-8')

        # URL decode the string
        url_decoded_string = unquote(decoded_string)

        # Convert the string to a dictionary
        data = ast.literal_eval(url_decoded_string)

        # Load the JSON data
        redirect_url = data.get("redirect_url")
        id_token = get_id_token_from_auth_code(auth_code)

        id_token = get_id_token_from_auth_code(auth_code)

        if id_token and '.' in id_token and id_token.count('.') >= 2:
            try:
                # Decode the JWT without verification
                decoded_token = jwt.decode(
                    id_token, options={"verify_signature": False})

                # Now you can access claims in the token, like the user's ID
                # 'oid' stands for Object ID
                user_id = decoded_token.get('unique_name')

                # Make a response object that includes a redirect
                response = make_response(redirect(redirect_url))
                # Set the user_id as a secure cookie on the response
                # todo  secure=True,
                response.set_cookie(
                    'user_id', user_id)
                # todo  secure=True,
                response.set_cookie(
                    'id_token', id_token, secure=True, httponly=True)

                response.headers['Authorization'] = f'Bearer {id_token}'

                # Redirect the user to the home page, or wherever they should go next
                return response

            except Exception as e:
                print(e)
                return {"message": "Error in decoding id_token"}

        else:
            msg = "Invalid id_token"
            print(msg)
            response = get_login_redirect_response()
            return response


class WelcomeSwagger(Resource):
    def get(self):
        """
        Returns the Swagger API documentation.

        Returns:
            dict: The Swagger API documentation schema.
        """
        with tracer.start_as_current_span("/api/swagger"):
            return api.__schema__


class Task(Resource):
    """
    Represents the endpoint for retrieving tasks related to a specific project.

    This class is used as a Flask-RESTful resource to handle requests related
    to retrieving tasks for a specific JIRA project.

    Args:
        Resource (type): The base class for implementing Flask-RESTful
        resources.

    Attributes:
        project (str): The name or identifier of the project associated with
        the tasks.
    """

    def get(self, project=None):
        """
        Retrieves tasks associated with a specific project from JIRA.

        Args:
            project (str, optional): The name or identifier of the project. If
            not provided, retrieves tasks for all projects.

        Returns:
            dict: A dictionary containing the retrieved tasks.

        Note:
            This method communicates with JIRA to fetch the tasks.

        Example: DTEDS

        """

        logger_singleton = cdc_env_logging.LoggerSingleton.instance(
            calling_namespace_name=NAMESPACE_NAME, calling_service_name=SERVICE_NAME)

        with tracer.start_as_current_span(f"tasks/{project}"):
            try:

                config = app.cdc_config

                jira_client_secret_key = config.get("jira_client_secret_key")
                az_kv_jira_env_var = jira_client_secret_key.replace("-", "_")
                jira_client_secret = os.getenv(az_kv_jira_env_var)
                logger.info(
                    f"jira_client_secret_length:{str(len(jira_client_secret))}")

                if project is None:
                    project = "DTEDS"  # Set your default project value here

                jira_base_url = config.get("jira_base_url")
                api_url = "/rest/api/latest/search"

                url = f"{jira_base_url}{api_url}"

                headers = {
                    "Authorization": f"Bearer {jira_client_secret}",
                    "Content-Type": "application/json"
                }
                logger.info(f"headers:{headers}")

                params = {
                    "jql": f"project = {project} AND issuetype = Task",
                    "fields": ["summary", "status", "assignee"],
                }

                logger.info(f"Retrieving tasks for project {project}")
                logger.info(f"url: {url}")
                logger.info(f"params: {params}")
                response_jira_tasks = requests.get(url,
                                                   headers=headers,
                                                   params=params,
                                                   timeout=TIMEOUT_5_SEC)
                response_jira_tasks_status_code = response_jira_tasks.status_code
                msg = "response_jira_tasks_status_code:"
                msg = msg + f"{response_jira_tasks_status_code}"
                logger.info(msg)
                content_t = response_jira_tasks.content.decode("utf-8")
                response_jira_tasks_content = content_t
                error_message = msg
                if response_jira_tasks_status_code in (200, 201):
                    msg = "response_jira_tasks_content:"
                    msg = msg + f"{response_jira_tasks_content}"
                    logger.info(msg)
                    try:
                        tasks = response_jira_tasks.json()["issues"]
                        logger.info(f"tasks: {tasks}")
                        # Process the retrieved tasks as needed
                        logger_singleton.force_flush()
                        return {"tasks": tasks}
                    except ValueError:
                        msg = f"Failed to retrieve json tasks from url: {url}."
                        msg = msg + f" parms:{params}"
                        msg = msg + "response_jira_tasks_content:"
                        msg = msg + f"{response_jira_tasks_content}"
                        exc_info = sys.exc_info()
                        # logger_singleton.error_with_exception(msg, exc_info)
                        logger_singleton.force_flush()
                        return {"error": msg}
                else:
                    msg = f"Failed to retrieve tasks from url:{url}"
                    msg = msg + \
                        f": status_code: {response_jira_tasks.status_code}"
                    msg = msg + ": response_jira_tasks_content:"
                    msg = msg + f"{response_jira_tasks_content}"
                    if response_jira_tasks.status_code == 500:
                        try:
                            error_message = response_jira_tasks.json()[
                                "message"]
                        except ValueError:
                            error_message = "Failed to retrieve json from url:"
                            error_message = error_message + \
                                f"{url}: params: {params}."
                    msg = msg + ": error_message: " + error_message
                    exc_info = sys.exc_info()
                    # logger_singleton.error_with_exception(msg, exc_info)
                    logger_singleton.force_flush()
                    return {"error": msg}
            except Exception as ex:
                msg = f"An unexpected error occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                logger_singleton.force_flush()
                return {"error": f"An unexpected error occurred: {msg}"}


class MetadataJsonFileDownload(Resource):
    """
    A Flask-RESTful resource responsible for downloading metadata JSON files.

    This class handles HTTP requests to the corresponding endpoint. It likely
    implements methods such as GET to handle the downloading of a metadata
    JSON file. Each method corresponds to a standard HTTP method
    (e.g., GET, POST, PUT, DELETE) and carries out a specific operation.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating new
        RESTful resources.
    """

    def get(self, schema_id):
        """
        Retrieves the JSON metadata file from Alation based on the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            JSON file.

        Returns:
            dict: A dictionary containing the downloaded JSON metadata file.

        Example:
            Use schema_id 106788 to test OCIO_PADE_DEV (DataBricks): ocio_pade_dev
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alation
        """

        logger_singleton = cdc_env_logging.LoggerSingleton.instance(
            calling_namespace_name=NAMESPACE_NAME, calling_service_name=SERVICE_NAME)

        with tracer.start_as_current_span("metadata_json_file_download"):
            try:

                start_time = time.time()  # Record the start time

                config = app.cdc_config

                schema = alation_schema.Schema()
                manifest_json_file = schema.download_schema_manifest_json_file(
                    schema_id, config)

                # Return the file as a download
                file_name = os.path.basename(manifest_json_file)

                end_time = time.time()  # Record the start time

                total_time = end_time - start_time  # Calculate the total time

                # Return the file as a response
                return send_file(manifest_json_file, as_attachment=True, download_name=file_name)

            except Exception as ex:
                msg = f"An unexpected error occurred for download file for schema_id: {schema_id}: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                logger_singleton.force_flush()
                response = make_response(jsonify({"error": str(ex)}), 500)
                return response


class MetadataExcelFileDownload(Resource):
    """
    A Flask-RESTful resource responsible for handling requests for downloading
    metadata Excel files with a specific schema id.

    This class corresponds to the endpoint
    '/metadata_excel_file_download/<int:schema_id>'.
    It handles HTTP requests that include a specific schema id in the URL, and
    it likely implements methods like GET to manage the download of the
    associated metadata Excel file.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating
        new RESTful resources.
    """

    def get(self, schema_id):
        """
        Retrieves the Excel metadata file from Alation based on the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            Excel file.

        Returns:
            dict: A dictionary containing the downloaded Excel metadata file.

        Example:
            Use schema_id 106788 to test OCIO_PADE_DEV (DataBricks): ocio_pade_dev
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alationn
        """

        logger_singleton = cdc_env_logging.LoggerSingleton.instance(
            calling_namespace_name=NAMESPACE_NAME, calling_service_name=SERVICE_NAME)

        with tracer.start_as_current_span(f"metadata_excel_file_download/{schema_id}"):
            try:

                start_time = time.time()  # Record the start time

                config = app.cdc_config

                obj_file = cdc_env_file.EnvironmentFile()
                app_dir = os.path.dirname(os.path.abspath(__file__))
                parent_dir = os.path.dirname(app_dir)

                repository_path = config.get("repository_path")
                environment = config.get("environment")

                schema = alation_schema.Schema()
                schema_file = schema.get_excel_schema_file_path(
                    repository_path, environment)
                manifest_excel_file = schema.download_schema_manifest_excel_file(
                    schema_id, config, schema_file)

                # Return the file as a download
                file_name = os.path.basename(manifest_excel_file)
                logger.info(f"file_name:{file_name}")

                end_time = time.time()  # Record the start time

                total_time = end_time - start_time  # Calculate the total time

                # Create the return message with the start, end, and total time
                message = {
                    'start_time': start_time,
                    'end_time': end_time,
                    'total_time': total_time,
                    'data': 'Success'
                }

                mime_type = "application/vnd.openxmlformats"
                mime_type = mime_type + "-officedocument.spreadsheetml.sheet"

                # Return the file as a response
                return send_file(manifest_excel_file, as_attachment=True, download_name=file_name)

            except Exception as ex:
                msg = f"An unexpected error occurred for download file for schema_id: {schema_id}: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                logger_singleton.force_flush()
                response = make_response(jsonify({"error": str(ex)}), 500)
                return response


class AzSubscriptionClientSecretVerification(Resource):
    """
    A Flask-RESTful resource for handling the verification of API keys.

    """

    def get(self):
        """
        Verifies the key stored in key vault based on configuration setting: az_kv_az_sub_client_secret_key

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"verify_az_sub_client_secret"):

            config = app.cdc_config
            az_kv_az_sub_client_secret_key = config.get(
                "az_kv_az_sub_client_secret_key")
            az_kv_az_sub_client_secret_key = az_kv_az_sub_client_secret_key.replace(
                "-", "_")
            client_secret = os.getenv(az_kv_az_sub_client_secret_key)
            tenant_id = config.get("tenant_id")
            client_id = config.get("client_id")

            security_core = pade_security_core.SecurityCore()
            status_code, response_content = security_core.verify_az_sub_client_secret(
                tenant_id, client_id, client_secret)

            # Handle the verification logic
            return {
                'status_code': status_code,
                'response_content': response_content
            }


class ConnectApiKeyVerification(Resource):
    """
    A Flask-RESTful resource for handling the verification of API keys.

    """

    def get(self):
        """
        Verifies the key stored in key vault based on configuration setting: az_kv_posit_connect_secret_key

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"connect_api_key_verification"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
            connect_api_key = get_posit_api_key()
            posit_connect = pade_posit_connect.PositConnect()
            status_code, response_content, api_url = posit_connect.verify_api_key(
                connect_api_key, posit_connect_base_url)

            # Handle the verification logic
            return {
                'status_code': status_code,
                'posit_connect_base_url': posit_connect_base_url,
                'api_url': api_url,
                "connect_api_key": connect_api_key,
                'response_content': response_content
            }


class DeploymentBundle(Resource):
    """
    A Flask-RESTful resource for handling POSIT Deployment Bundle.

    """

    def get(self, content_id, bundle_id):
        """
        Generates DeploymentBundle

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"build_deployment_bundle"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key")
            connect_api_key = get_posit_api_key()
            posit_connect = pade_posit_connect.PositConnect()
            status_code, response_content, api_url = posit_connect.build_deployment_bundle(
                connect_api_key, posit_connect_base_url, content_id, bundle_id)

            # Handle the verification logic
            return {
                'posit_connect_base_url': posit_connect_base_url,
                'api_url': api_url,
                'response_content': response_content
            }


class PythonInformation(Resource):
    """
    A Flask-RESTful resource for handling POSIT Python Information.

    """

    def get(self):
        """
        Generates python information about POSIT

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"api_key_verification"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            logger.info(f"posit_connect_base_url:{posit_connect_base_url}")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key")
            connect_api_key = get_posit_api_key()
            posit_connect = pade_posit_connect.PositConnect()
            status_code, response_content, api_url = posit_connect.get_python_information(
                connect_api_key, posit_connect_base_url)

            # Handle the verification logic
            return {
                'posit_connect_base_url': posit_connect_base_url,
                'api_url': api_url,
                "az_kv_posit_connect_secret_key": az_kv_posit_connect_secret_key,
                'response_content': response_content
            }


class GeneratedManifestJson(Resource):
    """
    A Flask-RESTful resource for handling POSIT ManifestJson Generation

    """

    def get(self):
        """
        Generates manifest JSON

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"generate_manifest"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            # Get the full URL
            full_url = request.url
            # Split the URL by '/'
            url_parts = full_url.split('/')
            # Remove the last 2 parts (i.e., the file name or the route)
            url_parts = url_parts[:-2]
            # Join the parts back together
            url_without_filename = '/'.join(url_parts)
            base_url = url_without_filename
            environment = config.get("environment")
            obj_file = cdc_env_file.EnvironmentFile()

            app_dir = os.path.dirname(os.path.abspath(__file__))

            manifest_path = (
                app_dir + "/" + environment + "_posit_manifests/"
            )

            swagger_path = (
                app_dir + "/" + environment + "_swagger_manifests/"
            )

            yyyy = str(datetime.now().year)
            dd = str(datetime.now().day).zfill(2)
            mm = str(datetime.now().month).zfill(2)

            json_extension = (
                "_"
                + yyyy
                + "_"
                + mm
                + "_"
                + dd
                + ".json"
            )
            manifest_json_file = manifest_path + "manifest" + json_extension
            # swagger_file = swagger_path + "swagger" + json_extension
            # use cached json file for now
            # having issues downloading
            swagger_file = swagger_path + "swagger_2023_06_22.json"
            connect_api_key = get_posit_api_key()
            requirements_file = app_dir + "/requirements.txt"

            # headers = {
            #     "Authorization": f"Bearer {connect_api_key}",
            # }
            swagger_url = f"{base_url}/swagger.json"
            # response = requests.get(swagger_url, headers=headers)

            # response_data = None
            # error_message = None
            # if response.status_code == 200:  # HTTP status code 200 means "OK"
            #     try:
            #         response_data =  response.json()
            #         response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
            #   except requests.HTTPError as http_err:
            #        error_message = f"HTTP error occurred: {http_err}"
            #        soup = BeautifulSoup(response.text, 'html.parser')
            #        error_message = (soup.prettify())
            #    except JSONDecodeError:
            #        error_message = "The response could not be decoded as JSON."
            #        soup = BeautifulSoup(response.text, 'html.parser')
            #        error_message = (soup.prettify())
            #    except Exception as err:
            #        error_message = f"An error occurred: {err}"
            #        error_message = "Response content:"+ response.content.decode()
            # else:
            #    error_message = f"Request failed with status code {response.status_code}"
            # if error_message is not None:
            #    return {
            #        'headers' : headers,
            #        'swagger_url' :  swagger_url,
            #        'manifest_json': "",
            #        'status_message': error_message
            #    }, 500
            # with open(swagger_file, 'w') as f:
            #    f.write(response_data)

            logger.info(f"swagger_file:{swagger_file}")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key")
            connect_api_key = get_posit_api_key()

            posit_connect = pade_posit_connect.PositConnect()

            manifest_json = posit_connect.generate_manifest(
                swagger_file, requirements_file)

            with open(manifest_json_file, 'w') as f:
                f.write(manifest_json)

            # Handle the verification logic
            return {
                'swagger_url': swagger_url,
                'manifest_json': manifest_json,
                'status_message': 'success'
            }


class PublishManifestJson(Resource):
    """
    A Flask-RESTful resource for handling POSIT ManifestJsonJson Publication

    """

    def get(self):
        """
        Publishes manifest JSON

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"publish_manifest"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")

            # Get the full URL
            full_url = request.url
            # Split the URL by '/'
            url_parts = full_url.split('/')
            # Remove the last 2 parts (i.e., the file name or the route)
            url_parts = url_parts[:-2]
            # Join the parts back together
            url_without_filename = '/'.join(url_parts)
            base_url = url_without_filename
            environment = config.get("environment")
            obj_file = cdc_env_file.EnvironmentFile()

            app_dir = os.path.dirname(os.path.abspath(__file__))

            manifest_path = (
                app_dir + "/" + environment + "_posit_manifests/"
            )

            manifest_json_file = obj_file.get_latest_file(
                manifest_path, "json")

            logger.info(f"manfiest_file:{manifest_json_file}")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key")
            connect_api_key = get_posit_api_key()

            posit_connect = pade_posit_connect.PositConnect()

            status_code, response_content, api_url = posit_connect.publish_manifest(
                connect_api_key, posit_connect_base_url, manifest_json_file)

            # Handle the verification logic
            return {
                'status_code': status_code,
                'response_content': response_content,
                'api_url': api_url
            }


class ContentList(Resource):
    """
    A Flask-RESTful resource for handling POSIT Content Lists

    """

    def get(self):
        """
        Retrieves the manifest JSON for the content list.

        Returns:
            tuple: A tuple containing the status code and response from the server.
                   The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span("list_content"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")
            connect_api_key = get_posit_api_key()

            posit_connect = pade_posit_connect.PositConnect()

            status_code, response_content, api_url = posit_connect.list_content(
                connect_api_key, posit_connect_base_url)

            # Handle the verification logic
            return {
                'status_code': status_code,
                'response_content': response_content,
                'api_url': api_url
            }


class DeploymentBundleList(Resource):
    """
    A Flask-RESTful resource for handling POSIT Bundle Lists

    """

    def get(self, content_id):
        """
        Publishes manifest JSON

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span("list_conent"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key")
            connect_api_key = get_posit_api_key()

            posit_connect = pade_posit_connect.PositConnect()

            status_code, response_content, api_url = posit_connect.list_deployment_bundles(
                connect_api_key, posit_connect_base_url, content_id)

            # Handle the verification logic
            return {
                'status_code': status_code,
                'response_content': response_content,
                'api_url': api_url
            }


class TaskStatus(Resource):
    """
    A Flask-RESTful resource for handling POSIT Bundle Lists

    """

    def get(self, task_id):
        """
        Gets Task Status

        Returns:
            tuple: A tuple containing the status code and response from the server.
            The response will be in JSON format if possible, otherwise it will be the raw text response.
        """

        with tracer.start_as_current_span(f"get_task_status"):

            config = app.cdc_config

            posit_connect_base_url = config.get("posit_connect_base_url")
            az_kv_posit_connect_secret_key = config.get(
                "az_kv_posit_connect_secret_key")
            connect_api_key = get_posit_api_key()

            posit_connect = pade_posit_connect.PositConnect()

            status_code, response_content, api_url = posit_connect.get_task_details(
                connect_api_key, posit_connect_base_url, task_id)

            # Handle the verification logic
            return {
                'status_code': status_code,
                'response_content': response_content,
                'api_url': api_url
            }


upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

# Define the API description with a hyperlink to the log file page
api.description = API_DESCRIPTION


ns_welcome.add_resource(WelcomeSwagger, '/')
ns_welcome.add_resource(WelcomeSwagger, "/api/swagger")
ns_jira.add_resource(Task, '/tasks/<string:project>')

# This model is used for swagger documentation


ns_alation.add_resource(MetadataJsonFileDownload,
                        "/metadata_json_file_download/<int:schema_id>")
ns_alation.add_resource(MetadataExcelFileDownload,
                        "/metadata_excel_file_download/<int:schema_id>")


class MetadataExcelFileUpload(Resource):
    """
    A Flask-RESTful resource for handling the upload of metadata Excel files.

    This class corresponds to the endpoint '/metadata_excel_file_upload'.
    It handles HTTP requests for uploading metadata Excel files.
    Each method in this class corresponds to a specific HTTP
    method (e.g., POST) and carries out the upload operation.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating new
        RESTful resources.

    Returns:
        Response: The response of the HTTP request after processing the
        uploaded file. The specific content and status code of the response
        will depend on the implementation.
    """

    @api.expect(upload_parser, validate=True)
    def post(self):
        """
        Uploads the Excel metadata file to Alation via direct upload based on
        the schema_id.

        Args:
            schema_id (int): The ID of the schema associated with the metadata
            Excel file.

        Returns:
            dict: A dictionary containing the response data.

        Example:
            Use schema_id 106788 to test OCIO_PADE_DEV (DataBricks): ocio_pade_dev
            Use schema_id 1464 to test Acme Bookstore (Synapse SQL Warehouse): EDAV.alation
        """

        with tracer.start_as_current_span("metadata_excel_file_upload"):

            try:
                start_time = time.time()  # Record the start time

                # Get the uploaded file
                args = upload_parser.parse_args()
                file = args['file']
                # Read the contents of the file as JSON
                file_contents = file.read()

                config = app.cdc_config
                schema = alation_schema.Schema()
                repository_path = config.get("repository_path")
                environment = config.get("environment")
                alation_user_id = 7

                manifest_excel_file_path_temp = schema.get_excel_manifest_file_path_temp(
                    "download", repository_path, environment, alation_user_id)

                with open(manifest_excel_file_path_temp, 'wb') as f:
                    f.write(file_contents)

                schema_json_file_path = schema.get_json_schema_file_path(
                    repository_path, environment)

                content_result = schema.upload_schema_manifest_excel_file(
                    manifest_excel_file_path_temp, config, schema_json_file_path)

                logger.info(f"content_result: {content_result}")

                end_time = time.time()  # Record the end time

                total_time = end_time - start_time  # Calculate the total time

                # Create the return message with the start, end, and total time
                message = {
                    'start_time': start_time,
                    'end_time': end_time,
                    'total_time': total_time,
                    'data': 'Success'
                }

                response = make_response(jsonify(message), 200)
                return response

            except RequestException as ex:
                msg = f"RequestException occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                # Create the return message with the start, end, and total time
                message = {
                    'data': msg
                }

                response = make_response(jsonify(message), 500)
                return response


class MetadataJsonFileUpload(Resource):
    """
    A Flask-RESTful resource for handling the upload of metadata JSON files.

    This class corresponds to the endpoint '/metadata_json_file_upload'. It
    handles HTTP requests for uploading metadata JSON files.
    Each method in this class corresponds to a specific HTTP
    method (e.g., POST) and carries out the upload operation.

    Args:
        Resource (Resource): A base class from Flask-RESTful for creating new
        RESTful resources.

    Returns:
        Response: The response of the HTTP request after processing the
        uploaded file.
        The specific content and status code of the response will depend on
        the implementation.
    """

    @api.expect(upload_parser, validate=True)
    def post(self):
        """Uploads JSON metadata file via direct upload to Alation
        based on schema_id.
        Use 106788 to test OCIO_PADE_DEV (DataBricks)
        """

        with tracer.start_as_current_span("metadata_json_file_upload"):

            try:

                start_time = time.time()  # Record the start time

                # Get the uploaded file
                args = upload_parser.parse_args()
                file = args['file']
                # Read the contents of the file as JSON
                file_contents = file.read()
                metadata_json_data = json.loads(file_contents)

                schema = alation_schema.Schema()
                config = app.cdc_config

                repository_path = config.get("repository_path")
                environment = config.get("environment")
                json_schema_file_path = schema.get_json_schema_file_path(
                    repository_path, environment)

                content_result = schema.upload_schema_manifest_excel_file(
                    metadata_json_data, config, json_schema_file_path)

                logger.info(f"content_result: {content_result}")

                end_time = time.time()  # Record the end time

                total_time = end_time - start_time  # Calculate the total time

                # Create the return message with the start, end, and total time
                message = {
                    'start_time': start_time,
                    'end_time': end_time,
                    'total_time': total_time,
                    'data': 'Success'
                }

                response = make_response(jsonify(message), 200)
                return response

            except RequestException as ex:
                msg = f"RequestException occurred: {str(ex)}"
                exc_info = sys.exc_info()
                # logger_singleton.error_with_exception(msg, exc_info)
                # Create the return message with the start, end, and total time
                message = {
                    'start_time': start_time,
                    'end_time': end_time,
                    'total_time': total_time,
                    'data': msg
                }

                response = make_response(jsonify(message), 500)
                return response


ns_alation.add_resource(MetadataJsonFileUpload,
                        "/metadata_json_file_upload")
ns_alation.add_resource(MetadataExcelFileUpload,
                        "/metadata_excel_file_upload")

ns_posit.add_resource(ConnectApiKeyVerification,
                      "/connect_api_key_verification")
ns_posit.add_resource(PythonInformation, "/python_information")
ns_posit.add_resource(GeneratedManifestJson, "/generate_manifest")
ns_posit.add_resource(PublishManifestJson, "/publish_manifest")
ns_posit.add_resource(ContentList, "/list_content")
ns_posit.add_resource(
    DeploymentBundle, "/build_deployment_bundle/<string:content_id>/<string:bundle_id>")
ns_posit.add_resource(DeploymentBundleList,
                      "/list_deployment_bundles/<string:content_id>")
ns_posit.add_resource(TaskStatus, "/get_task_status/<string:task_id>")

ns_cdc_security.add_resource(
    AzSubscriptionClientSecretVerification, "/verify_az_sub_client_secret")
ns_cdc_security.add_resource(AuthCallback, "/callback")
ns_cdc_security.add_resource(AuthCallback, "/get_user_id")

if __name__ == "__main__":
    app.run(debug=True)
