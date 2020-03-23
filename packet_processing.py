from classes import *
from constants import *
from time_converter import *


def parsing_data(s, info=None):
    print("\t\t[LOG_ED] Starting extract data...")
    # Competitor\t	4	FirstName	Анастасия
    #   0           1       2           3
    # track, first_name=None, last_name=None, lane_time=None, rank=None, lap=None, points=None

    s = s.replace('\r', '')
    track = s.split('\t')[1]
    print("\t\t\tInfos: {}".format(str(info)))
    if info is None:
        print("\t\t\tTrack number {}".format(track))
        info = Info(track=track)
        info = check_conditions(s, info)
    else:
        info = check_conditions(s, info)
    print("\t\t[LOG_ED] End extract data...")
    return info


def check_conditions(s, info=Info):
    print("check conditions...")
    if COMPETITOR in s:
        result = extract_ppl_info(s, info)
        return result
    elif (LANE_TIME in s) and (LAP in s) and (UNUSED_TRACK not in s):
        result = extract_track_info(s, info)
        return result


def extract_track_info(s, info=Info):
    # Time\t 3	 LaneTime	804319	Rank	5	Lap	 2	Points	0.00
    #   0    1      2         3       4     5    6   7     8     9
    print("[LOG_ETI] Starting extract track info...")
    print("check eq obj: " + str(info))
    spl = s.split('\t')
    print("Splited data: {}".format(spl))
    seconds = int(spl[3])
    lane_time = in_minuts(seconds)
    rank = int(spl[5])
    lap = spl[7]
    points = spl[9]
    info.lane_time = lane_time
    info.raw_time = seconds
    info.rank = rank
    info.lap = lap
    info.points = points
    print("[LOG_ETI] End extract track info...")
    return info


def extract_ppl_info(s, info=Info):
    print("[LOG_EPI] Starting extract ppl info...")
    spl = s.split('\t')
    name = spl[3]
    if FIRST_NAME in s:
        info.first_name = name.strip()
    elif LAST_NAME in s:
        info.last_name = name.strip()
    print("[LOG_EPI] End extract ppl info...")
    return info
