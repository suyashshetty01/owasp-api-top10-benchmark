""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_identity_api_auth_v2_7_user_login_with_token_post_token = dependencies.DynamicVariable("_identity_api_auth_v2_7_user_login_with_token_post_token")

_identity_api_v2_user_videos_post_id = dependencies.DynamicVariable("_identity_api_v2_user_videos_post_id")

_community_api_v2_community_posts_post_id = dependencies.DynamicVariable("_community_api_v2_community_posts_post_id")

_workshop_api_shop_orders_post_id = dependencies.DynamicVariable("_workshop_api_shop_orders_post_id")

def parse_identityapiauthv27userloginwithtokenpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["token"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_identity_api_auth_v2_7_user_login_with_token_post_token", temp_7262)


def parse_identityapiv2uservideospost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8173 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_identity_api_v2_user_videos_post_id", temp_8173)


def parse_communityapiv2communitypostspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7680 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7680 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_community_api_v2_community_posts_post_id", temp_7680)


def parse_workshopapishoporderspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5581 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5581 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_workshop_api_shop_orders_post_id", temp_5581)

req_collection = requests.RequestCollection([])
# Endpoint: /identity/api/auth/signup, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("signup"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("Cristobal.Weissnat@example.com", quoted=True, examples=["Cristobal.Weissnat@example.com"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("Cristobal.Weissnat", quoted=True, examples=["Cristobal.Weissnat"]),
    primitives.restler_static_string(""",
    "number":"""),
    primitives.restler_fuzzable_string("6915656974", quoted=True, examples=["6915656974"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("Password1!", quoted=True, examples=["Password1!"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/auth/signup"
)
req_collection.add_request(request)

# Endpoint: /identity/api/auth/login, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("login"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("test@example.com", quoted=True, examples=["test@example.com"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("Password1!", quoted=True, examples=["Password1!"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/auth/login"
)
req_collection.add_request(request)

# Endpoint: /identity/api/auth/forget-password, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forget-password"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("adam007@example.com", quoted=True, examples=["adam007@example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/auth/forget-password"
)
req_collection.add_request(request)

# Endpoint: /identity/api/auth/v3/check-otp, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("check-otp"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "otp":"""),
    primitives.restler_fuzzable_string("9969", quoted=True, examples=["9969"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("Password1!", quoted=True, examples=["Password1!"]),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("Cristobal.Weissnat@example.com", quoted=True, examples=["Cristobal.Weissnat@example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/auth/v3/check-otp"
)
req_collection.add_request(request)

# Endpoint: /identity/api/auth/v2/check-otp, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("check-otp"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "otp":"""),
    primitives.restler_fuzzable_string("9969", quoted=True, examples=["9969"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("Password1!", quoted=True, examples=["Password1!"]),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("Cristobal.Weissnat@example.com", quoted=True, examples=["Cristobal.Weissnat@example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/auth/v2/check-otp"
)
req_collection.add_request(request)

# Endpoint: /identity/api/auth/v4.0/user/login-with-token, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v4.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("login-with-token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("restlertest@example.com", quoted=True),
    primitives.restler_static_string(""",
    "token":"""),
    primitives.restler_static_string(_identity_api_auth_v2_7_user_login_with_token_post_token.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/auth/v4.0/user/login-with-token"
)
req_collection.add_request(request)

# Endpoint: /identity/api/auth/v2.7/user/login-with-token, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auth"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2.7"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("login-with-token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("restlertest@example.com", quoted=True),
    primitives.restler_static_string(""",
    "token":"""),
    primitives.restler_fuzzable_string("test-token-123", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_identityapiauthv27userloginwithtokenpost,
            'dependencies':
            [
                _identity_api_auth_v2_7_user_login_with_token_post_token.writer()
            ]
        }

    },

],
requestId="/identity/api/auth/v2.7/user/login-with-token"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/reset-password, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reset-password"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("restlertest@example.com", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("Password1!", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/user/reset-password"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/change-email, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("change-email"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "new_email":"""),
    primitives.restler_fuzzable_string("Sofia.Predovic@example.com", quoted=True, examples=["Sofia.Predovic@example.com"]),
    primitives.restler_static_string(""",
    "old_email":"""),
    primitives.restler_fuzzable_string("Cristobal.Weissnat@example.com", quoted=True, examples=["Cristobal.Weissnat@example.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/user/change-email"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/verify-email-token, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("verify-email-token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "old_email":"""),
    primitives.restler_fuzzable_string("Einar.Swaniawski@example.com", quoted=True, examples=["Einar.Swaniawski@example.com"]),
    primitives.restler_static_string(""",
    "new_email":"""),
    primitives.restler_fuzzable_string("Danielle.Ankunding@example.com", quoted=True, examples=["Danielle.Ankunding@example.com"]),
    primitives.restler_static_string(""",
    "token":"""),
    primitives.restler_fuzzable_string("T9O2s6i3C7o2E8l7X5Y4", quoted=True, examples=["T9O2s6i3C7o2E8l7X5Y4"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/user/verify-email-token"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/dashboard, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dashboard"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/user/dashboard"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/videos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_identityapiv2uservideospost,
            'dependencies':
            [
                _identity_api_v2_user_videos_post_id.writer()
            ]
        }

    },

],
requestId="/identity/api/v2/user/videos"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/videos/{video_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_identity_api_v2_user_videos_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/user/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/videos/{video_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_identity_api_v2_user_videos_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "videoName":"""),
    primitives.restler_fuzzable_string("test.mp4", quoted=True),
    primitives.restler_static_string(""",
    "video_url":"""),
    primitives.restler_fuzzable_string("http://example.com/test.mp4", quoted=True),
    primitives.restler_static_string(""",
    "conversion_params":"""),
    primitives.restler_fuzzable_string("-v codec h264", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/user/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/user/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_identity_api_v2_user_videos_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/user/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/admin/videos/{video_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("videos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1", examples=["12345"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/admin/videos/{video_id}"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/vehicle/vehicles, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vehicle"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vehicles"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/vehicle/vehicles"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/vehicle/add_vehicle, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vehicle"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("add_vehicle"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "pincode":"""),
    primitives.restler_fuzzable_string("9896", quoted=True, examples=["9896"]),
    primitives.restler_static_string(""",
    "vin":"""),
    primitives.restler_fuzzable_string("0IOJO38SMVL663989", quoted=True, examples=["0IOJO38SMVL663989"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/vehicle/add_vehicle"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/vehicle/{vehicleId}/location, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vehicle"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=False, examples=["1929186d-8b67-4163-a208-de52a41f7301"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("location"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/vehicle/{vehicleId}/location"
)
req_collection.add_request(request)

# Endpoint: /identity/api/v2/vehicle/resend_email, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("identity"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vehicle"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resend_email"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/identity/api/v2/vehicle/resend_email"
)
req_collection.add_request(request)

# Endpoint: /community/api/v2/community/posts/{postId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("posts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_community_api_v2_community_posts_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/community/api/v2/community/posts/{postId}"
)
req_collection.add_request(request)

# Endpoint: /community/api/v2/community/posts, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("posts"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "content":"""),
    primitives.restler_fuzzable_string("Est maiores voluptas velit. Necessitatibus vero veniam quos nobis.", quoted=True, examples=["Est maiores voluptas velit. Necessitatibus vero veniam quos nobis."]),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("Velit quia minima.", quoted=True, examples=["Velit quia minima."]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_communityapiv2communitypostspost,
            'dependencies':
            [
                _community_api_v2_community_posts_post_id.writer()
            ]
        }

    },

],
requestId="/community/api/v2/community/posts"
)
req_collection.add_request(request)

# Endpoint: /community/api/v2/community/posts/{postId}/comment, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("posts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_community_api_v2_community_posts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comment"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "content":"""),
    primitives.restler_fuzzable_string("Porro aut ratione et.", quoted=True, examples=["Porro aut ratione et."]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/community/api/v2/community/posts/{postId}/comment"
)
req_collection.add_request(request)

# Endpoint: /community/api/v2/community/posts/recent, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("posts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recent"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["30"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/community/api/v2/community/posts/recent"
)
req_collection.add_request(request)

# Endpoint: /community/api/v2/coupon/new-coupon, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("coupon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("new-coupon"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "coupon_code":"""),
    primitives.restler_fuzzable_string("TRAC075", quoted=True, examples=["TRAC075"]),
    primitives.restler_static_string(""",
    "amount":"""),
    primitives.restler_fuzzable_string("75", quoted=True, examples=["75"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/community/api/v2/coupon/new-coupon"
)
req_collection.add_request(request)

# Endpoint: /community/api/v2/coupon/validate-coupon, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("community"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("coupon"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("validate-coupon"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "coupon_code":"""),
    primitives.restler_fuzzable_string("TRAC075", quoted=True, examples=["TRAC075"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/community/api/v2/coupon/validate-coupon"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/products, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("products"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/shop/products"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/products, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("products"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("WheelBase", quoted=True, examples=["WheelBase"]),
    primitives.restler_static_string(""",
    "price":"""),
    primitives.restler_fuzzable_string("10.12", quoted=True, examples=["10.12"]),
    primitives.restler_static_string(""",
    "image_url":"""),
    primitives.restler_fuzzable_string("http://example.com/wheelbase.png", quoted=True, examples=["http://example.com/wheelbase.png"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/shop/products"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/orders, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "product_id":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "quantity":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_workshopapishoporderspost,
            'dependencies':
            [
                _workshop_api_shop_orders_post_id.writer()
            ]
        }

    },

],
requestId="/workshop/api/shop/orders"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/orders/{order_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_workshop_api_shop_orders_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "product_id":"""),
    primitives.restler_static_string(_workshop_api_shop_orders_post_id.reader(), quoted=False),
    primitives.restler_static_string(""",
    "quantity":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/shop/orders/{order_id}"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/orders/{order_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_workshop_api_shop_orders_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/shop/orders/{order_id}"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/orders/all, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("all"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["30"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/shop/orders/all"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/orders/return_order, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("return_order"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("order_id="),
    primitives.restler_fuzzable_int("1", examples=["33"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/shop/orders/return_order"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/shop/apply_coupon, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("apply_coupon"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "amount":"""),
    primitives.restler_fuzzable_int("1", examples=["75"]),
    primitives.restler_static_string(""",
    "coupon_code":"""),
    primitives.restler_fuzzable_string("TRAC075", quoted=True, examples=["TRAC075"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/shop/apply_coupon"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/management/users/all, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("management"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("all"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["30"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/management/users/all"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/mechanic, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mechanic"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/mechanic"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/merchant/contact_mechanic, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merchant"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contact_mechanic"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "number_of_repeats":"""),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(""",
    "mechanic_api":"""),
    primitives.restler_fuzzable_string("http://www.google.com", quoted=True),
    primitives.restler_static_string(""",
    "vin":"""),
    primitives.restler_fuzzable_string("0BZCX25UTBJ987271", quoted=True),
    primitives.restler_static_string(""",
    "repeat_request_if_failed":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "problem_details":"""),
    primitives.restler_fuzzable_string("Car issue for testing", quoted=True),
    primitives.restler_static_string(""",
    "mechanic_code":"""),
    primitives.restler_fuzzable_string("TRAC_JME", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/merchant/contact_mechanic"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/mechanic/receive_report, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mechanic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("receive_report"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("mechanic_code="),
    primitives.restler_fuzzable_string("TRAC_MECH1", quoted=False, examples=["TRAC_MECH1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("problem_details="),
    primitives.restler_fuzzable_string("My car has engine trouble, and I need urgent help!", quoted=False, examples=["My car has engine trouble, and I need urgent help!"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("vin="),
    primitives.restler_fuzzable_string("0BZCX25UTBJ987271", quoted=False, examples=["0BZCX25UTBJ987271"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/mechanic/receive_report"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/mechanic/mechanic_report, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mechanic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mechanic_report"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("report_id="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/mechanic/mechanic_report"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/mechanic/service_requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mechanic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("service_requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["30"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/mechanic/service_requests"
)
req_collection.add_request(request)

# Endpoint: /workshop/api/mechanic/signup, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("workshop"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mechanic"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("signup"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8888\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("RESTler Tester", quoted=True),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("restlertest@example.com", quoted=True),
    primitives.restler_static_string(""",
    "number":"""),
    primitives.restler_fuzzable_string("0891234567", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("Password1!", quoted=True),
    primitives.restler_static_string(""",
    "mechanic_code":"""),
    primitives.restler_fuzzable_string("TRAC_JME", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/workshop/api/mechanic/signup"
)
req_collection.add_request(request)
