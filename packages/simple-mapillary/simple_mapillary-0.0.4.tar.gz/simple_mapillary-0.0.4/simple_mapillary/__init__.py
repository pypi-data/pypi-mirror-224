from .image import Image

from simple_mapillary.api import init_client


def set_access_token(access_token=""):
    init_client(access_token)

try:
    set_access_token()
except:
    pass


