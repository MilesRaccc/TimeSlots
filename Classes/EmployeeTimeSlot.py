from datetime import datetime, timedelta
from Classes.Employee import Employee
from Classes.TimeSlot import TimeSlot


class EmployeeTimeSlot(Employee):
    def __init__(self, name, phone, position, time_start, time_end, time_slot_duration):
        super().__init__(name, phone, position, time_start, time_end)

        # Заполняем слоты
        # Для начала превращаем начало и конец рабочего времени чисто в минуты

        self.time_slot_duration = time_slot_duration
        time_start_minutes = self.work_time_start.minute + (self.work_time_start.hour * 60)
        time_end_minutes = self.work_time_end.minute + (self.work_time_end.hour * 60)

        # Количество минут отведённых под слоты
        time_duration_minutes = time_end_minutes - time_start_minutes

        # Создаём список слотов, заготовки для заполнения
        # (чтобы цикл вечно не ходил и чтобы заполнять в качестве начала слота последний созданный)
        self.__slots = list()
        last_slot_minutes = time_start_minutes
        new_slot_start = self.work_time_start

        # Заполняем до тех пор пока минуты рабочего времени не закончатся
        while time_duration_minutes != 0:
            # Если оставшееся время больше отведённого на слот - высчитываем время прибавляя к общему количеству минут
            # длительность слота, ставим новое количество минут в соответствии с высчитаным временем и от "счётчика"
            # вычитаем время слота
            if time_duration_minutes > time_slot_duration:
                new_slot_minutes = last_slot_minutes + time_slot_duration
                last_slot_minutes = new_slot_minutes
                time_duration_minutes = time_duration_minutes - time_slot_duration
            # Если оставшееся время меньше отведённого на слот - добавляем к последнему общему количеству минут оставшееся
            # время и ставим счётчик на 0
            else:
                new_slot_minutes = last_slot_minutes + time_duration_minutes
                time_duration_minutes = 0

            # Конвертируем новое завершающее для слота из чисто минут обратно в часы + минуты и добавляем слот в список
            new_slot_finish = datetime.strptime(f"{new_slot_minutes // 60}:{new_slot_minutes % 60}", "%H:%M")
            self.__slots.append(TimeSlot(new_slot_start, new_slot_finish, True))
            # Ставим время старта следующего слота временем финиша текущего
            new_slot_start = new_slot_finish

    @property
    def time_slot_duration(self):
        return "{}:{}".format(self.__time_slot_duration.seconds // 3600, (self.__time_slot_duration.seconds//60) % 60)

    @time_slot_duration.setter
    def time_slot_duration(self, time_slot_duration):
        if time_slot_duration > 60:
            time_slot_hours = time_slot_duration // 60
            time_slot_minutes = time_slot_duration % 60
            self.__time_slot_duration = timedelta(hours=time_slot_hours, minutes=time_slot_minutes)
        else:
            self.__time_slot_duration = timedelta(minutes=time_slot_duration)

    @property
    def slots(self):
        return self.__slots

    def print_slots(self):
        times = list()

        for time_slot in self.__slots:
            if time_slot.not_taken is True:
                times.append("[" + f"{time_slot.time_start.hour}:{time_slot.time_start.minute}" +
                             ", " + f"{time_slot.time_end.hour}:{time_slot.time_end.minute}" + "]")

        print("\n".join(times))

    def get_employee_worktime(self):
        return f"{self.work_time_start_print()} - {self.work_time_end_print()}"

    def take_slot(self, time_slot_start_time_string):
        time_slot_start_time = datetime.strptime(time_slot_start_time_string, "%H:%M")
        for time_slot in self.__slots:
            if time_slot.time_start.hour == time_slot_start_time.hour \
                    and time_slot.time_start.minute == time_slot_start_time.minute:
                time_slot.not_taken = False
                break
