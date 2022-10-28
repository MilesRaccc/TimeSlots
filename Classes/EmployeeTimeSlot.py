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
        return self.__time_slot_duration.seconds

    def print_time_slot_duration(self):
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
        print("\n")

    def get_employee_worktime(self):
        return f"{self.work_time_start_print()} - {self.work_time_end_print()}"

    def take_slot(self, taken_slot_start_time_string):
        taken_slot_start_time = datetime.strptime(taken_slot_start_time_string, "%H:%M")
        for time_slot in self.__slots:
            if time_slot.time_start.hour == taken_slot_start_time.hour \
                    and time_slot.time_start.minute == taken_slot_start_time.minute:
                time_slot.not_taken = False
                break

    # Прошу прощения, если вам необходимо было чтобы в качестве параметра нужно было указать имена сотрудников,
    # а не список их слотов, но у меня не хватило времени.
    @staticmethod
    def get_employees_joint_timeslots(employees_list):
        employee_time_slot_duration = employees_list[0].time_slot_duration
        for employee in employees_list[1:]:
            if employee.time_slot_duration != employee_time_slot_duration:
                print("Время слотов некоторых сотрудников не совпадает. Найти общие слоты не представляется возможным")
                return

        employees_slots_time_starts = list()
        for employee in employees_list:
            time_starts = set()
            for time_slot in employee.slots:
                if time_slot.not_taken is True:
                    time_starts.add(time_slot.time_start)
            employees_slots_time_starts.append(time_starts)

        result = employees_slots_time_starts[0]
        for slots in employees_slots_time_starts[1:]:
            result.intersection_update(slots)

        if len(result) == 0:
            print("Не было найдено общих слотов для сотрудников.")
            return

        joint_slots = list()
        for time in result:
            time_minutes = time.hour * 60 + time.minute
            time_minutes = time_minutes + (employee_time_slot_duration // 60)
            joint_slot_finish = datetime.strptime(f"{time_minutes // 60}:{time_minutes % 60}", "%H:%M")
            joint_slots.append(TimeSlot(time, joint_slot_finish, True))

        times = list()
        times.append("Общие свободные слоты для указанных сотрудников")

        for time_slot in joint_slots:
            times.append("[" + f"{time_slot.time_start.hour}:{time_slot.time_start.minute}" +
                         ", " + f"{time_slot.time_end.hour}:{time_slot.time_end.minute}" + "]")

        print("\n".join(times))
        print("\n")
