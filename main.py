from Classes.EmployeeTimeSlot import EmployeeTimeSlot


def main():
    andrew = EmployeeTimeSlot("Andrew", "+79999999999", "rnd", "09:00", "18:00", 35)
    andrew.print_slots()
    andrew.take_slot("14:15")
    andrew.print_slots()

    alex = EmployeeTimeSlot("Alex", "+79998888888", "rnd2", "12:30", "23:00", 35)
    alex.print_slots()
    employees = [andrew, alex]
    EmployeeTimeSlot.get_employees_joint_timeslots(employees)


if __name__ == "__main__":
    main()
