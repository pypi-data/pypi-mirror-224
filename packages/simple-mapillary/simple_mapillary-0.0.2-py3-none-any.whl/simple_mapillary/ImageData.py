from dataclasses import dataclass, fields


@dataclass
class ImageData:
    id: str
    altitude: float
    atomic_scale: float
    camera_parameters: list
    camera_type: str
    captured_at: str
    compass_angle: float
    computed_altitude: float
    computed_compass_angle: float
    computed_geometry: dict
    computed_rotation: str
    exif_orientation: str
    geometry: dict
    height: int
    thumb_256_url: str
    thumb_1024_url: str
    thumb_2048_url: str
    thumb_original_url: str
    merge_cc: int
    mesh: dict
    sequence: str
    sfm_cluster: dict
    width: int
    detections: list

    def __init__(self, raw_data):
        self.id = self.get_id(raw_data)
        self.altitude = self.get_altitude(raw_data)
        self.atomic_scale = self.get_atomic_scale(raw_data)
        self.camera_parameters = self.get_camera_parameters(raw_data)
        self.camera_type = self.get_camera_type(raw_data)
        self.captured_at = self.get_captured_at(raw_data)
        self.compass_angle = self.get_compass_angle(raw_data)
        self.computed_altitude = self.get_computed_altitude(raw_data)
        self.computed_compass_angle = self.get_computed_compass_angle(raw_data)
        self.computed_geometry = self.get_computed_geometry(raw_data)
        self.computed_rotation = self.get_computed_rotation(raw_data)
        self.exif_orientation = self.get_exif_orientation(raw_data)
        self.geometry = self.get_geometry(raw_data)
        self.height = self.get_height(raw_data)
        self.thumb_256_url = self.get_thumb_256_url(raw_data)
        self.thumb_1024_url = self.get_thumb_1024_url(raw_data)
        self.thumb_2048_url = self.get_thumb_2048_url(raw_data)
        self.thumb_original_url = self.get_thumb_original_url(raw_data)
        self.merge_cc = self.get_merge_cc(raw_data)
        self.mesh = self.get_mesh(raw_data)
        self.sequence = self.get_sequence(raw_data)
        self.sfm_cluster = self.get_sfm_cluster(raw_data)
        self.width = self.get_width(raw_data)
        self.detections = self.get_detections(raw_data)

    @staticmethod
    def fields():
        return [field.name for field in fields(ImageData)]

    @staticmethod
    def get_id(raw_data):
        return raw_data['id']

    @staticmethod
    def get_altitude(raw_data):
        return raw_data['altitude']

    @staticmethod
    def get_atomic_scale(raw_data):
        return raw_data['atomic_scale']

    @staticmethod
    def get_camera_parameters(raw_data):
        return raw_data['camera_parameters']

    @staticmethod
    def get_camera_type(raw_data):
        return raw_data['camera_type']

    @staticmethod
    def get_captured_at(raw_data):
        return raw_data['captured_at']

    @staticmethod
    def get_compass_angle(raw_data):
        return raw_data['compass_angle']

    @staticmethod
    def get_computed_altitude(raw_data):
        return raw_data['computed_altitude']

    @staticmethod
    def get_computed_compass_angle(raw_data):
        return raw_data['computed_compass_angle']

    @staticmethod
    def get_computed_geometry(raw_data):
        return raw_data['computed_geometry']

    @staticmethod
    def get_computed_rotation(raw_data):
        return raw_data['computed_rotation']

    @staticmethod
    def get_exif_orientation(raw_data):
        return raw_data['exif_orientation']

    @staticmethod
    def get_geometry(raw_data):
        return raw_data['geometry']

    @staticmethod
    def get_height(raw_data):
        return raw_data['height']

    @staticmethod
    def get_thumb_256_url(raw_data):
        return raw_data['thumb_256_url'].replace('\\', '')

    @staticmethod
    def get_thumb_1024_url(raw_data):
        return raw_data['thumb_1024_url'].replace('\\', '')

    @staticmethod
    def get_thumb_2048_url(raw_data):
        return raw_data['thumb_2048_url'].replace('\\', '')

    @staticmethod
    def get_thumb_original_url(raw_data):
        return raw_data['thumb_original_url'].replace('\\', '')

    @staticmethod
    def get_merge_cc(raw_data):
        return raw_data['merge_cc']

    @staticmethod
    def get_mesh(raw_data):
        return raw_data['mesh']

    @staticmethod
    def get_sequence(raw_data):
        return raw_data['sequence']

    @staticmethod
    def get_sfm_cluster(raw_data):
        return raw_data['sfm_cluster']

    @staticmethod
    def get_width(raw_data):
        return raw_data['width']

    @staticmethod
    def get_detections(raw_data):
        if 'detections' not in raw_data:
            return []
        return raw_data['detections']
