import json
import math
import os

if __name__ == '__main__':
    point_gain: dict[int, int] = {}
    for i_level in range(1, 186):
        if i_level <= 99:
            point_gain[i_level] = math.floor(i_level / 5) + 3
        elif 100 <= i_level <= 149:
            point_gain[i_level] = math.floor(i_level / 10) + 13
        elif i_level == 150:
            point_gain[i_level] = 27
        elif 151 <= i_level <= 184:
            point_gain[i_level] = math.floor((i_level - 150) / 7) + 28
        else:
            point_gain[i_level] = 32

    status_point: dict[int, int] = {}
    current_status_point = 48
    for i_level in range(1, 186):
        status_point[i_level] = current_status_point
        current_status_point += point_gain[i_level]

    status_point_transcended: dict[int, int] = {}
    current_status_point_transcended = 100
    for i_level in range(1, 186):
        status_point_transcended[i_level] = current_status_point_transcended
        current_status_point_transcended += point_gain[i_level]

    raise_status_cost: dict[int, int] = {}
    for i_level in range(1, 186):
        if i_level <= 99:
            raise_status_cost[i_level] = math.floor((i_level - 1) / 10) + 2
        else:
            raise_status_cost[i_level] = 4 * math.floor((i_level - 100) / 5) + 16

    try:
        if not os.path.exists('config'):
            os.makedirs('config')

        with open('config/point_gain.json', 'w') as f:
            json.dump(point_gain, f)

        with open('config/status_point.json', 'w') as f:
            json.dump(status_point, f)

        with open('config/status_point_transcended.json', 'w') as f:
            json.dump(status_point_transcended, f)

        with open('config/raise_status_cost.json', 'w') as f:
            json.dump(raise_status_cost, f)

    except Exception as e:
        print(e)
        print('Failed to create config files')
        exit(1)
