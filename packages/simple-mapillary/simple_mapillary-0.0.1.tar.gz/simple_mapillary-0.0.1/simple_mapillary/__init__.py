from . import __token__
from .Client import Client
from .Image import Image

def set_access_token(access_token=""):
    if len(access_token) == 0:
        if len(__token__.token) == 0:
            raise Exception("\n\nNo access token was provided. Please pass a token to the set_access_token"
                            " function or set the token in the __token__.py file. Check the README for more"
                            " information.\n")
    else:
        __token__.token = access_token

    Client.init_static(__token__.token)

set_access_token()