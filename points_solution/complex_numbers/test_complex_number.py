from points_solution.complex_numbers.complejo import Complejo


def test_sum_complex_number():
    A = Complejo(2, 1)
    B = Complejo(5, 6)

    assert A.sum(B) == 7 + 7j


def test_subtract_complex_number():
    A = Complejo(2, 1)
    B = Complejo(5, 6)

    assert A.subtract(B) == -3 - 5j


def test_multiply_complex_number():
    A = Complejo(2, 1)
    B = Complejo(5, 6)

    assert A.multiply(B) == 4 + 17j


def test_divide_complex_number():
    A = Complejo(2, 1)
    B = Complejo(5, 6)

    assert A.divide(B) == 0.26 - 0.11j


def test_module_complex_number():
    A = Complejo(2, 1)
    B = Complejo(5, 6)

    assert A.mod() == 2.24 - 0j
    assert B.mod() == 7.81 - 0j
