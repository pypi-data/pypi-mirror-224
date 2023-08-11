import random
from pykml import parser
import pandas as pd
import simplekml
from datetime import datetime
import os
import math
from vinhvh_package import vinhvh as v
# def get_random_color():
#     """
#     Generate a random color in hexadecimal format.
#     """
#     color = '#{:06x}'.format(random.randint(0, 256**3 - 1))
#     return color


def get_random_color():
    """
    Generate a random color in RGBA format.
    """
    color = '{:02x}{:02x}{:02x}{:02x}'.format(random.randint(0, 255), random.randint(0, 255),
                                              random.randint(0, 255), random.randint(0, 255))
    return color


def read_polygon(polygon_path):
    # Read the KML file
    with open(polygon_path) as f:
        root = parser.parse(f).getroot()
        ns = {'kml': 'http://www.opengis.net/kml/2.2'}

    # Get the coordinates of the polygon from the Placemark element
    polygon = [(float(coord.split(',')[0]), float(coord.split(',')[1]))
               for coord in root.xpath('//kml:Placemark/kml:Polygon/kml:outerBoundaryIs/kml:LinearRing/kml:coordinates/text()', namespaces=ns)[0].split()]
    return polygon


def get_point(df_data, polygon, sitename):

    # Find the points that are inside the polygon
    points_inside_polygon = []
    for index, row in df_data.iterrows():
        site = row[sitename]
        long = row['Lon']
        lat = row['Lat']
        point = (long, lat)
        if is_point_in_polygon(point, polygon):
            points_inside_polygon.append(site)

    df_result = df_data[df_data[sitename].isin(points_inside_polygon)]
    return df_result


def is_point_in_polygon(point, polygon):
    """
    Check if a point is inside a polygon using the ray-casting algorithm.
    """
    x, y = map(float, point)
    inside = False
    n = len(polygon)
    p1x, p1y = map(float, polygon[0])
    for i in range(n+1):
        p2x, p2y = map(float, polygon[i % n])
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= max(p1x, xints):
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def draw_line(kml, main_point, target_point, color, description: str = None, width: float = 1.5):
    """
    Draw a line between two points in a KML file.

    Args:
        kml: The KML object where the line will be added.
        main_point: The coordinates of the starting point of the line.
        target_point: The coordinates of the ending point of the line.
        color: The color of the line in hexadecimal format (e.g., '#FF0000' for red).
        width (optional): The width of the line in units specified by the KML file. Default is 0.2.

    Returns:
        kml: The updated KML object with the line added.
    """
    line = kml.newlinestring()
    line.coords = [main_point, target_point]
    line.style.linestyle.color = color
    line.style.linestyle.width = width
    line.description = description
    return kml



def calculate_azimuth(start_lat, start_lng, end_lat, end_lng):
    lat1 = math.radians(start_lat)
    lon1 = math.radians(start_lng)
    lat2 = math.radians(end_lat)
    lon2 = math.radians(end_lng)

    delta_lon = lon2 - lon1

    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon))

    azimuth = math.atan2(y, x)
    azimuth_degrees = math.degrees(azimuth)
    if azimuth_degrees < 0:
        azimuth_degrees += 360

    return int(azimuth_degrees)

def check_type_site(x):
    if len(x) == 7:
        check =  x[-1:]
    elif len(x) == 9:
        check = x[-3:]
    elif len(x) == 10:
        check = x[-4:]
    elif len(x) == 11:
        check = x[-5:]
    else:
        check = 'other'
    return v.type_site(check)
    
def check_sector(x):
    if len(x) in range(7,11):
        check =  x[-1:]
    elif len(x) == 11:
        check = x[6]
    else:
        check = 'other'
    sector_types = {
        'Sector 1': ['A', 'D', 'G', 'J', 'M', 'P'],
        'Sector 2': ['B', 'E', 'H', 'K', 'N', 'Q'],
        'Sector 3': ['C', 'F', 'I', 'L', 'O', 'R']

    }
    for sector_type, codes in sector_types.items():
        if check in codes:
            return sector_type
    return 'Other'
