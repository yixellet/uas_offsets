import math
from calc_azimuth import calc_azimuth
from calc_offsets import calc_offsets
from config import RX1

with open('photo_centers_RX1.txt', 'r') as source, open('photo_centers_RX1_offsets.txt', 'w') as result:
    
    points = []
    for line in source:
        line_array = line.split(';')
        point = {}
        point['name'] = int(line_array[0])
        point['nord'] = float(line_array[1].replace(',', '.'))
        point['east'] = float(line_array[2].replace(',', '.'))
        point['elev'] = float(line_array[3].replace(',', '.'))
        point['time'] = line_array[4]
        point['stdne'] = float(line_array[7].replace(',', '.'))
        point['stdh'] = float(line_array[8].replace(',', '.'))
        points.append(point)
    
    for i in range(len(points) - 1):
        cur_point = points[i]
        next_point = points[i + 1]
        points[i]['azimuth'] = calc_azimuth(cur_point, next_point)
    
    points[-1]['azimuth'] = calc_azimuth(points[-2], points[-1])

    for i in range(len(points) - 2):
        cur_point = points[i]
        next_point = points[i + 1]
        next2_point = points[i + 2]
        dazimuth = next2_point['azimuth'] - next_point['azimuth']
        if abs(dazimuth) >= 15:
            next_point['azimuth'] = cur_point['azimuth']

    for point in points:
        p = calc_offsets(point, RX1['X'], RX1['Y'], RX1['Z'])
        result.write(str(p['name']) + '\t' + str(p['nord']) + '\t' + str(p['east']) + '\t' + str(p['elev']) + '\t' + str(p['stdn']) + '\t' + str(p['stde']) + '\t' + str(p['stdh']) + '\n')
    
