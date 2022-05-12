import math

def calc_offsets(point, x, y, z):
    point['elev'] = point['elev'] + z
    dnord_y = abs(y) * math.cos(math.radians(point['azimuth']))
    deast_y = abs(y) * math.sin(math.radians(point['azimuth']))
    dnord_x = abs(x) * math.cos(math.radians(point['azimuth'] - 90 if x < 0 else point['azimuth'] + 90))
    deast_x = abs(x) * math.sin(math.radians(point['azimuth'] - 90 if x < 0 else point['azimuth'] + 90))
    point['nord'] = point['nord'] + dnord_x + dnord_y
    point['east'] = point['east'] + deast_x + deast_y
    point['stdn'] = math.sqrt((point['stdne']**2) / 2)
    point['stde'] = math.sqrt((point['stdne']**2) / 2)

    return point