import typing

from .api_utils import METADATA_URL
from .Client import Client

class ImageAPI:

    @staticmethod
    def get_image(image_id: str, fields: list) -> str:
        url = f"{METADATA_URL}/{image_id}/?fields={','.join(fields)}"
        return Client.get(url)