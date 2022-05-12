import math
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
    
    for i in range(len(points)):
        cur_point = points[i]
        next_point = points[i + 1]

        dnord = next_point['nord'] - cur_point['nord']
        deast = next_point['east'] - cur_point['east']
        azimuth = math.tan(deast / dnord)

    print(len(points))