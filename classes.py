# class Track(object):
#
#     def __init__(self, track, lane_time, rank, lap, points):
#         """Constructor"""
#         self.track = track
#         self.lane_time = lane_time
#         self.rank = rank
#         self.lap = lap
#         self.points = points
#
#     def info(self):
#         return '{} {} {} {} {}'.format(self.track, self.lane_time, self.rank, self.lap, self.points)
#
#
# class Competitor(object):
#
#     def __init__(self, track, first_name=None, last_name=None):
#         self.track = track
#         self.first_name = first_name
#         self.last_name = last_name
#         self.full_name = None
#
#     def full_name(self):
#         self.full_name = '{} {}'.format(self.first_name, self.last_name)
#         return self.full_name
#
#     def info(self):
#         return '{} {} {}'.format(self.track, self.first_name, self.last_name)
#


class Info(object):

    def __init__(self, track, first_name=None, last_name=None, lane_time=None, rank=None, lap=None, points=None,
                 raw_time=None):
        self.track = track
        self.first_name = first_name
        self.last_name = last_name
        self.lane_time = lane_time
        self.rank = rank
        self.lap = lap
        self.points = points
        self.raw_time = raw_time
        self.full_name = None

    def full_name(self):
        if (self.first_name is not None) and (self.last_name is not None):
            self.full_name = '{} {}'.format(self.first_name, self.last_name)
        else:
            self.full_name = '[some name is empty]'
        return self.full_name

    def to_string(self):
        return "{} track: {}, first_name: {}, last_name: {}, lane_time: {}, lap: {}, raw_time: {}, rank: {} {}".format(
            '{',
            str(self.track), str(self.first_name),
            str(self.last_name), str(self.lane_time),
            str(self.lap), str(self.raw_time), str(self.rank),
            '}'
        )

    # return "{}\"track\": \"{}\", \"first_name\": \"{}\", \"last_name\": \"{}\", \"lane_time\": \"{}\", \"lap\": \"{}\", \"raw_time\": \"{}\", rank: {} {}]".format(

    # return "{} track: {}, first_name: {}, last_name: {}, lane_time: {}, lap: {}, raw_time: {}, rank: {} {}"
    def is_full(self):
        return self.track is not None and \
               self.first_name is not None and \
               self.last_name is not None and \
               self.first_name is not '' and \
               self.last_name is not '' and \
               self.lane_time is not None and \
               self.rank is not None and \
               self.lap is not None and \
               self.points is not None
