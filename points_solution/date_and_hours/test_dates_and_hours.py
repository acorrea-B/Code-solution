import pytest

from dates_and_hours import count_days


def test_fail_init_date_greater_than_finish_date_count_days():
    with pytest.raises(ValueError) as exec:
        count_days("21/01/2024 18:12:39.054821", "21/01/2023 18:12:39.054821")
    assert str(exec.value) == "Try to make the start date less than the end date"


def test_fail_empty_init_date_count_days():
    with pytest.raises(ValueError) as exec:
        count_days("", "21/01/2023 18:12:39.054821")
    assert str(exec.value) == "date_init and date_finish can't be empty"


def test_fail_empty_finish_date_count_days():
    with pytest.raises(ValueError) as exec:
        count_days("21/01/2023 18:12:39.054821", "")
    assert str(exec.value) == "date_init and date_finish can't be empty"


def test_count_days(capsys):

    count_days("21/01/2022 18:12:39.054821", "21/01/2023 18:12:39.054821")
    capture = capsys.readouterr()
    assert (
        capture.out
        == "Lunes: 52\nMartes: 52\nMiercoles: 52\nJueves: 52\nViernes: 53\nSabado: 53\nDomingo: 52\n"
    )
