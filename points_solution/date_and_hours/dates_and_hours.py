from datetime import datetime
from datetime import timedelta


def format_date(date_init, date_finish):
    format = "%d/%m/%Y %H:%M:%S %z"
    if not date_init or not date_finish:
        raise ValueError("date_init and date_finish can't be empty")

    date_init = datetime.strptime(date_init, format)
    date_finish = datetime.strptime(date_finish, format)

    if not date_init < date_finish:
        raise ValueError("Try to make the start date less than the end date")

    return date_init, date_finish


def count_days(date_init, date_finish):

    date_init, date_finish = format_date(date_init, date_finish)

    days = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    string_days = {
        0: "Lunes",
        1: "Martes",
        2: "Miercoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sabado",
        6: "Domingo",
    }
    while date_init <= date_finish:
        days[date_init.weekday()] += 1
        date_init += timedelta(days=1)

    for day in days:
        print(f"{string_days[day]}: {days[day]}")


def working_hours(date_init, date_finish):
    date_init, date_finish = format_date(date_init, date_finish)

    sum_days = 0
    while date_init <= date_finish:
        if date_init.weekday() in range(0, 4):
            sum_days += 1
        date_init += timedelta(days=1)
    print(f"Horas laborales: {sum_days*8}")


def subtract_date(date_init, date_finish):
    format = "%S-%H-%d"
    date_init, date_finish = format_date(date_init, date_finish)

    result = date_finish - date_init

    days_hours = str(result).split(",")

    hours_seconds = days_hours[1].split(":")

    print(f"{hours_seconds[2]}-{hours_seconds[1]}-{days_hours[0]}")
