from classes import *
from constants import *
from time_converter import *


def parsing_data(data, heat=None):
    heat = check_conditions(data, heat)

    # if HEAT in data or len(data) > 3:
    #     print("-----------------------------------------------------------------------------------")
    #     print('Parsing data processing..')
    #     print('Splitted data: {}'.format(data))
    #     print('processing result: {}'.format(heat))
    #     print("-----------------------------------------------------------------------------------")

    return heat


def check_conditions(data, heat: Heat):
    if HEAT in data:
        result = extract_heat_info(data, heat)
        return result
    elif len(data) > 3:
        if COMPETITOR in data:
            result = extract_ppl_info(data, heat)
            return result
        elif LANE_TIME in data:
            result = extract_track_info(data, heat)
            return result


def extract_heat_info(data, heat: Heat):
    if HEAT_NUMBER in data:
        heat.heat_number = int(data[2])
        heat.laps = -1
        heat.fix_info()
    elif HEAT_LAPS in data:
        heat.laps = int(data[2])
    return heat


def extract_track_info(data, heat: Heat):
    track = int(data[1])
    seconds = int(data[3])
    lane_time = in_minuts(seconds)
    rank = int(data[5])
    lap = int(data[7])
    points = data[9]

    check = True
    if heat.hasInfosByTrack(track):
        info = heat.get_info_by_track(track)
    else:
        info = Info(track=track)
        check = False

    info.lane_time = lane_time
    info.raw_time = seconds
    info.rank = rank
    info.lap = lap
    info.points = points

    if check:
        heat.add_info(info=info, part=PPL_UPDATE_INFO)
    else:
        heat.add_info(info)

    return heat


def extract_ppl_info(data, heat: Heat):
    track = int(data[1])
    check = True

    if heat.hasInfosByTrack(track):
        info = heat.get_info_by_track(track)
    else:
        info = Info(track=track)
        check = False

    name = data[3]
    if FIRST_NAME in data:
        info.first_name = name.strip()
    elif LAST_NAME in data:
        info.last_name = name.strip()

    if check:
        heat.add_info(info=info, part=PPL_UPDATE_INFO)
    else:
        heat.add_info(info)

    return heat
