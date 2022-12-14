from datetime import datetime


class Employee:
    def __init__(self, name, phone, position, work_time_start, work_time_end):
        self.__name = name
        self.__phone = phone
        self.__position = position
        try:
            self.__work_time_start = datetime.strptime(work_time_start, "%H:%M")
            self.__work_time_end = datetime.strptime(work_time_end, "%H:%M")
        except ValueError:
            print("Введено некорректное время. "
                  "\nРабочее время сотрудника должно быть в числовом виде от 0 до 23 часов и от 0 до 59 минут."
                  "\nПерепроверьте вводимые данные.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def work_time_start(self):
        return self.__work_time_start

    def work_time_start_print(self):
        return "{}:{}".format(self.__work_time_start.hour, self.__work_time_start.minute)

    @work_time_start.setter
    def time_start(self, work_time_start):
        try:
            self.__work_time_start = datetime.strptime(work_time_start, "%H:%M")
        except ValueError:
            print("Введено некорректное время. Рабочее время сотрудника должно быть от 0 до 23 часов и от 0 до 59 минут.")

    @property
    def work_time_end(self):
        return self.__work_time_end

    def work_time_end_print(self):
        return "{}:{}".format(self.__work_time_end.hour, self.__work_time_end.minute)

    @work_time_end.setter
    def work_time_end(self, work_time_end):
        try:
            self.__work_time_end = datetime.strptime(work_time_end, "%H:%M")
        except ValueError:
            print("Введено некорректное время. Рабочее время сотрудника должно быть от 0 до 23 часов и от 0 до 59 минут.")