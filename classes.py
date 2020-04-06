from constants import TRACK_UPDATE_INFO, PPL_UPDATE_INFO


class Info(object):

    def __init__(self, track=-1, first_name='', last_name='', lane_time=-1, rank=-1, lap=-1, points=-1,
                 raw_time=-1):
        self.track = track
        self.first_name = first_name
        self.last_name = last_name
        self.lane_time = lane_time
        self.rank = rank
        self.lap = lap
        self.points = points
        self.raw_time = raw_time

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_name_with_track(self):
        return f'{self.first_name} {self.last_name} ({self.track})'

    def spreadsheet_data(self):
        return [str(self.rank), str(self.track), self.full_name(), str(self.lane_time)]

    def spreadsheet_data_temporary_results(self):
        return [str(self.track), self.full_name(), str(self.lane_time)]

    def is_full(self):
        return self.track != -1 and \
               self.first_name is not '' and \
               self.last_name is not '' and \
               self.lane_time != -1 and \
               self.rank != -1 and \
               self.lap != -1 and \
               self.points != -1

    def isFinalLap(self, final_lap):
        if self.lap == -1:
            return False
        if self.lap == final_lap:
            return True

    def __repr__(self):
        return f'\n\t\t\t\t\t\t\t\t\t\t\t{self.track}, {self.lap} {self.full_name()}, {self.lane_time}'

    # def __repr__(self):
    #     return '{}"track": "{}", "first_name": "{}", "last_name": "{}", "rank": "{}", "lap": "{}", "lane_time": "{}", "raw_time": "{}", "spreadsheet_data": {} {}'.format(
    #         '{',
    #         self.track,
    #         self.first_name,
    #         self.last_name,
    #         self.rank,
    #         self.lap,
    #         self.lane_time,
    #         self.raw_time,
    #         self.spreadsheet_data(),
    #         '}'
    #     )

    def to_string(self):
        return {
            "track": self.track,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "rank": self.rank,
            "lap": self.lap,
            "lane_time": self.lane_time,
            "raw_time": self.raw_time,
            "spreadsheet_data": self.spreadsheet_data()
        }


class Heat(object):
    current_heat: int
    isSended: bool
    isClean = False

    def __init__(self, heat_number=-1, laps=-1, infos=None):
        self.heat_number = heat_number
        self.laps = laps
        self.infos = infos

    def get_info_by_track(self, track):
        for i in self.infos:
            if i.track == track:
                return i

    def add_info(self, info: Info, part=None):
        if not self.infos:
            self.infos = []
            self.infos.append(info)
        else:
            if not part:
                self.infos.append(info)
            else:
                track = info.track
                for i in self.infos:
                    if i.track == track:
                        if part == PPL_UPDATE_INFO:
                            i.first_name = info.first_name
                            i.last_name = info.last_name
                        elif part == TRACK_UPDATE_INFO:
                            i.lane_time = info.lane_time
                            i.rank = info.rank
                            i.lap = info.lap
                            i.points = info.points
                            i.raw_time = info.raw_time
                        break

    def fix_info(self):
        if self.infos is None or len(self.infos) == 0:
            return
        else:
            for i in self.infos:
                i.lap = -1  # it is bull shit, but it is necessary if the data is corrupted

    def hasInfosByTrack(self, track: int):
        if not self.infos or len(self.infos) == 0:
            return False
        for i in self.infos:
            if i.track == track:
                return True
        return False

    def isFull(self):
        if self.laps == -1:
            return False
        if not self.infos or len(self.infos) == 0:
            return False
        for info in self.infos:
            if not info.isFinalLap(self.laps):
                return False
        return True

    def sort_by_rank(self):
        return sorted(self.infos, key=lambda x: x.rank)

    def __repr__(self):
        return f'[heat_number: {self.heat_number} laps: {self.laps} infos:{self.infos}]'
