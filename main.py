from Classes.EmployeeTimeSlot import *


def main():
    andrew = EmployeeTimeSlot("Andrew", "+79999999999", "rnd", "09:00", "18:00", 35)
    andrew.print_slots()
    andrew.take_slot("14:15")
    andrew.print_slots()


if __name__ == "__main__":
    main()
