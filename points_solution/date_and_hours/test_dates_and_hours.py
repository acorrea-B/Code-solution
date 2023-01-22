import pytest

from dates_and_hours import count_days
from dates_and_hours import format_date
from dates_and_hours import working_hours
from dates_and_hours import subtract_date


def test_fail_init_date_greater_than_finish_date_format_date():
    with pytest.raises(ValueError) as exec:
        format_date("21/01/2024 18:12:39 +00:00", "21/01/2023 18:12:39 +00:00")
    assert str(exec.value) == "Try to make the start date less than the end date"


def test_fail_empty_init_date_format_day():
    with pytest.raises(ValueError) as exec:
        format_date("", "21/01/2023 18:12:39 +00:00")
    assert str(exec.value) == "date_init and date_finish can't be empty"


def test_fail_empty_finish_date_format_day():
    with pytest.raises(ValueError) as exec:
        format_date("21/01/2023 18:12:39", "")
    assert str(exec.value) == "date_init and date_finish can't be empty"


def test_count_days(capsys):

    count_days("21/01/2022 18:12:39 +00:00", "21/01/2023 18:12:39 +00:00")
    capture = capsys.readouterr()
    assert (
        capture.out
        == "Lunes: 52\nMartes: 52\nMiercoles: 52\nJueves: 52\nViernes: 53\nSabado: 53\nDomingo: 52\n"
    )


def test_working_hours(capsys):

    working_hours("21/01/2022 18:12:39 +00:00", "21/01/2023 18:12:39 +00:00")
    capture = capsys.readouterr()
    assert capture.out == "Horas laborales: 1664\n"


def test_subtract_date(capsys):

    subtract_date("21/01/2022 18:12:39 +00:00", "21/01/2023 18:12:39 +00:00")
    capture = capsys.readouterr()
    assert capture.out == "00-00-365 days\n"


def test_subtract_diferent_time_zone_date(capsys):

    subtract_date("21/01/2022 18:12:39 +00:00", "21/01/2023 18:12:39 +00:08")
    capture = capsys.readouterr()
    assert capture.out == "00-52-364 days\n"
