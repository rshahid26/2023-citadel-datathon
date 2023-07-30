import numpy as np

R = 3958.8  # Earth radius


def haversine_distance(lat1, lon1, lat2, lon2):
    phi1, phi2 = np.radians(lat1), np.radians(lat2)

    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c


def slerp(p0, p1, t):
    """Spherical linear interpolation."""
    p0 = np.array(p0)
    p1 = np.array(p1)
    omega = np.arccos(np.dot(p0/np.linalg.norm(p0), p1/np.linalg.norm(p1)))
    so = np.sin(omega)
    return np.sin((1.0-t)*omega) / so * p0 + np.sin(t*omega)/so * p1


def interpolate_points(start, end, num_points):
    return np.array([slerp(start, end, t) for t in np.linspace(0, 1, num_points)])


def lat_lon_to_cartesian(lat, lon):
    lat, lon = np.radians([lat, lon])
    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    z = R * np.sin(lat)

    return np.array([x, y, z])


def cartesian_to_lat_lon(x, y, z):
    lon = np.arctan2(y, x)
    lat = np.arcsin(z / R)

    return np.degrees([lat, lon])
