from datetime import datetime
from datetime import timedelta


def count_days(date_init, date_finish):
    format = "%d/%m/%Y %H:%M:%S.%f"

    if not date_init or not date_finish:
        raise ValueError("date_init and date_finish can't be empty")

    date_init = datetime.strptime(date_init, format)
    date_finish = datetime.strptime(date_finish, format)

    if not date_init < date_finish:
        raise ValueError("Try to make the start date less than the end date")

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
