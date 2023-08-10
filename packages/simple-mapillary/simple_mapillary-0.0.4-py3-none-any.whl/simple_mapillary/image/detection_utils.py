import mapbox_vector_tile
import base64
import numpy as np
import cv2

rng = np.random.default_rng(3)
classes = ['Bird', 'Ground Animal', 'Acoustic', 'Ambiguous', 'Concrete Block', 'Curb', 'Fence',
           'Guard Rail', 'Other Barrier', 'Road Median', 'Road Side', 'Separator', 'Temporary',
           'Wall', 'Bike Lane', 'Crosswalk Plain', 'Curb Cut', 'Driveway', 'Parking', 'Parking Aisle',
           'Pedestrian Area', 'Rail Track', 'Road', 'Road Shoulder', 'Service Lane', 'Sidewalk',
           'Traffic Island', 'Bridge', 'Building', 'Garage', 'Tunnel', 'Individual', 'Person Group',
           'Bicyclist', 'Motorcyclist', 'Other Rider', 'Dashed', 'Solid', 'Zigzag', 'Ambiguous',
           'Ambiguous', 'Left', 'Other', 'Right', 'Split Left Or Right',
           'Split Left Or Right Or Straight', 'Split Left Or Straight', 'Split Right Or Straight',
           'Straight', 'U Turn', 'Crosswalk Zebra', 'Give Way Row', 'Give Way Single', 'Chevron',
           'Diagonal', 'Other Marking', 'Stop Line', 'Ambiguous', 'Bicycle', 'Other', 'Pedestrian',
           'Wheelchair', '30', '40', '50', 'Ambiguous', 'Bus', 'Other', 'School', 'Slow', 'Stop',
           'Taxi', 'Beach', 'Mountain', 'Sand', 'Sky', 'Snow', 'Terrain', 'Vegetation', 'Water',
           'Banner', 'Bench', 'Bike Rack', 'Catch Basin', 'Cctv Camera', 'Fire Hydrant',
           'Junction Box', 'Mailbox', 'Manhole', 'Parking Meter', 'Phone Booth', 'Pothole',
           'Ramp', 'Advertisement', 'Ambiguous', 'Back', 'Information', 'Other', 'Store',
           'Street Light', 'Pole', 'Pole Group', 'Traffic Sign Frame', 'Utility Pole', 'Traffic Cone',
           'Ambiguous', 'Cyclists Back', 'Cyclists Front', 'Cyclists Side', 'General Horizontal Back',
           'General Horizontal Front', 'General Horizontal Side', 'General Single Back',
           'General Single Front', 'General Single Side', 'General Upright Back', 'General Upright Front',
           'General Upright Side', 'Other', 'Pedestrians', 'Pedestrians Back', 'Pedestrians Front',
           'Pedestrians Side', 'Warning', 'Ambiguous', 'Back', 'Direction Back', 'Direction Front',
           'Front', 'Information Parking', 'Temporary Back', 'Temporary Front', 'Trash Can', 'Bicycle',
           'Boat', 'Bus', 'Car', 'Caravan', 'Motorcycle', 'On Rails', 'Other Vehicle', 'Trailer', 'Truck',
           'Vehicle Group', 'Wheeled Slow', 'Water Valve', 'Wire Group', 'Car Mount', 'Dynamic',
           'Ego Vehicle', 'Ground', 'Static', 'Unlabeled']
colors = rng.uniform(0, 255, size=(len(classes), 3))
label_colors = dict(zip(classes, colors))


def geometry_to_coordinates(pixel_geometry):
    decoded_data = base64.decodebytes(pixel_geometry.encode('utf-8'))
    detection_geometry = mapbox_vector_tile.decode(decoded_data)
    extent = detection_geometry['mpy-or']['extent']
    coordinates = np.array(detection_geometry['mpy-or']['features'][0]['geometry']['coordinates'][0])
    coordinates = coordinates / extent
    coordinates[:, 1] = 1 - coordinates[:, 1]
    return coordinates


def draw_detection(img, coordinates, color):
    coordinates[:, 0] = coordinates[:, 0] * img.shape[1]
    coordinates[:, 1] = coordinates[:, 1] * img.shape[0]
    coordinates = coordinates.astype(int)

    cv2.fillPoly(img, pts=[coordinates], color=color)


def draw_detections(img, detections):
    img_copy = img.copy()
    for detection in detections:
        points = detection.points
        label = detection.label
        if label not in label_colors:
            continue
        color = label_colors[label]
        draw_detection(img_copy, points, color)
    return img_copy
