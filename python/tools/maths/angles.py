from math import radians

def dms_to_rad(dms):
    """
    Converts [degree].[arcminute] to radians.

    Args:
        dms (float): Value in the format [degree].[arcminute], e.g., 180.0 for 180 degrees 0 minutes.

    Returns:
        float: Value in radians.
    """
    degrees = int(dms)
    minutes = (dms - degrees) * 100

    decimal_degrees = degrees + minutes / 60

    return radians(decimal_degrees)