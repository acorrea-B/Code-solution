import pytest

from product import get_position
from product import add_product
from product import order_products


@pytest.fixture(name="in_products")
def setUp():
    yield [
        {
            "Nombre": "Zapatos XYZ",
            "Código de barras": 8569741233658,
            "Fabricante": "Deportes XYZ",
            "Categoría": "Zapatos",
            "Género": "Masculino",
        },
        {
            "Nombre": "Zapatos ABC",
            "Código de barras": 7452136985471,
            "Fabricante": "Deportes XYZ",
            "Categoría": "Zapatos",
            "Género": "Femenino",
        },
        {
            "Nombre": "Camisa DEF",
            "Código de barras": 5236412896324,
            "Fabricante": "Deportes XYZ",
            "Categoría": "Camisas",
            "Género": "Masculino",
        },
        {
            "Nombre": "Bolso KLM",
            "Código de barras": 5863219635478,
            "Fabricante": "Carteras Hi-Fashion",
            "Categoría": "Bolsos",
            "Género": "Femenino",
        },
    ]


@pytest.fixture(name="out_products")
def result():
    yield {
        "Deportes XYZ": {
            "Zapatos": {
                "Masculino": [
                    {
                        "Nombre": "Zapatos XYZ",
                        "Código de barras": 8569741233658,
                        "Fabricante": "Deportes XYZ",
                        "Categoría": "Zapatos",
                        "Género": "Masculino",
                    }
                ],
                "Femenino": [
                    {
                        "Nombre": "Zapatos ABC",
                        "Código de barras": 7452136985471,
                        "Fabricante": "Deportes XYZ",
                        "Categoría": "Zapatos",
                        "Género": "Femenino",
                    }
                ],
            },
            "Camisas": {
                "Masculino": [
                    {
                        "Nombre": "Camisa DEF",
                        "Código de barras": 5236412896324,
                        "Fabricante": "Deportes XYZ",
                        "Categoría": "Camisas",
                        "Género": "Masculino",
                    }
                ]
            },
        },
        "Carteras Hi-Fashion": {
            "Bolsos": {
                "Femenino": [
                    {
                        "Nombre": "Bolso KLM",
                        "Código de barras": 5863219635478,
                        "Fabricante": "Carteras Hi-Fashion",
                        "Categoría": "Bolsos",
                        "Género": "Femenino",
                    }
                ]
            }
        },
    }


def test_get_position(in_products):
    products = {}
    out_result = get_position(in_products[0], products)
    assert type(out_result) == list
    assert in_products[0]["Fabricante"] in products
    assert in_products[0]["Categoría"] in products[in_products[0]["Fabricante"]]
    assert (
        in_products[0]["Género"]
        in products[in_products[0]["Fabricante"]][in_products[0]["Categoría"]]
    )


def test_add_product(in_products):
    products = {}
    add_product(in_products[0], products)
    assert (
        products[in_products[0]["Fabricante"]][in_products[0]["Categoría"]][
            in_products[0]["Género"]
        ][0]
        == in_products[0]
    )


def test_order_products(in_products, out_products):
    out_result = order_products(in_products)

    assert out_result == out_products
