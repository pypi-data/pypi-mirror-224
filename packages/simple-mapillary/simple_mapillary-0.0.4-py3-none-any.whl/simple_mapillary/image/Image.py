from imread_from_url import imread_from_url

from .ImageAPI import ImageAPI
from .ImageData import ImageData
from .DetectionData import DetectionData


class Image():
    image_data: ImageData

    def __init__(self, image_id: str):
        raw_data = ImageAPI.get_image(image_id, fields=ImageData.fields())
        self.image_data = ImageData(raw_data)

    def get_cvimage(self):
        return imread_from_url(self.image_data.thumb_1024_url)

    def get_detections(self):
        raw_data = ImageAPI.get_image_detections(self.image_data.id, fields=DetectionData.fields())
        return [DetectionData(raw_detection) for raw_detection in raw_data]
