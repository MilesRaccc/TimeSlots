from datetime import datetime


class TimeSlot:
    def __init__(self, time_start, time_end, not_taken=True):
        self.time_start = time_start
        self.time_end = time_end
        self.__not_taken = not_taken

    @property
    def time_start(self):
        return self.__time_start

    def time_start_print(self):
        return "{}:{}".format(self.__time_start.hour, self.__time_start.minute)

    @time_start.setter
    def time_start(self, time_start):
        self.__time_start = time_start

    @property
    def time_end(self):
        return self.__time_end

    def time_end_print(self):
        return "{}:{}".format(self.__time_end.hour, self.__time_end.minute)

    @time_end.setter
    def time_end(self, time_end):
        self.__time_end = time_end

    @property
    def not_taken(self):
        return self.__not_taken

    @not_taken.setter
    def not_taken(self, not_taken):
        self.__not_taken = not_taken