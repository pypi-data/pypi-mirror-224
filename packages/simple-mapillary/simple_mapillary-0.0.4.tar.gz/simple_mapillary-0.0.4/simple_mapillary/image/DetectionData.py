from dataclasses import dataclass, fields
from .detection_utils import geometry_to_coordinates

@dataclass
class DetectionData:
    id: str
    created_at: str
    geometry: dict
    image: dict
    value: str

    def __init__(self, raw_data):
        self.id = self.get_id(raw_data)
        self.created_at = self.get_created_at(raw_data)
        self.geometry = self.get_geometry(raw_data)
        self.image = self.get_image(raw_data)
        self.value = self.get_value(raw_data)

    @staticmethod
    def fields():
        return [field.name for field in fields(DetectionData)]

    @staticmethod
    def get_id(raw_data):
        return raw_data['id']

    @staticmethod
    def get_created_at(raw_data):
        return raw_data['created_at']

    @staticmethod
    def get_geometry(raw_data):
        return raw_data['geometry']

    @staticmethod
    def get_image(raw_data):
        return raw_data['image']

    @staticmethod
    def get_value(raw_data):
        return raw_data['value']

    @property
    def label(self):
        return self.value.split('--')[-1].title().replace('-', ' ')

    @property
    def coordinates(self):
        return self.image['geometry']['coordinates']

    @property
    def points(self):
        return geometry_to_coordinates(self.geometry)
