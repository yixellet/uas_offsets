from math import degrees, atan

def calc_azimuth(point1, point2):

    dnord = point2['nord'] - point1['nord']
    deast = point2['east'] - point1['east']
    rumb = degrees(atan(abs(deast / dnord)))
    azimuth = 0
    
    if dnord >= 0:
        if deast > 0:
            azimuth = rumb
        elif deast < 0:
            azimuth = 360 - rumb
    elif dnord < 0:
        if deast > 0:
            azimuth = 180 - rumb
        elif deast < 0:
            azimuth = 180 + rumb
    
    return azimuth