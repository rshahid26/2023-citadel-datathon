import numpy as np

R = 3958.8  # Earth radius


def haversine_distance(lat1, lon1, lat2, lon2):
    phi1, phi2 = np.radians(lat1), np.radians(lat2)

    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c


def get_compass_bearing(lat1, long1, lat2, long2):
    long_diff = np.radians(long2 - long1)
    lat1, lat2 = np.radians(lat1), np.radians(lat2)

    x = np.sin(long_diff) * np.cos(lat2)
    y = np.cos(lat1) * np.sin(lat2) - (np.sin(lat1) * np.cos(lat2) * np.cos(long_diff))

    initial_bearing = np.arctan2(x, y)
    initial_bearing = np.degrees(initial_bearing)

    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing


def get_destination_point(lat, lon, bearing, distance):
    bearing = np.radians(bearing)  # converting bearing to radians
    lat1 = np.radians(lat)  # Current lat point converted to radians
    lon1 = np.radians(lon)  # Current long point converted to radians

    lat2 = np.arcsin(np.sin(lat1) * np.cos(distance/R) + np.cos(lat1) * np.sin(distance/R) * np.cos(bearing))
    lon2 = lon1 + np.arctan2(np.sin(bearing) * np.sin(distance/R)* np.cos(lat1), np.cos(distance/R)- np.sin(lat1)* np.sin(lat2))

    lat2 = np.degrees(lat2)
    lon2 = np.degrees(lon2)
    return lat2, lon2

