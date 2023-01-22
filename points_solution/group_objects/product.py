import re

from enum import Enum


class Gender(Enum):
    F = "Femenino"
    M = "Masculino"


class Product:
    def __init__(self, name, barcode, maker, category, gender):

        self.name = self._is_valid_name(name)
        self.barcode = self._is_valid_barcode(barcode)
        self.maker = self.is_valid_string(maker)
        self.category = self.is_valid_string(category)
        self.gender = self._is_valid_gender_(gender)

    def _is_valid_gender(self, value):

        if not isinstance(value, Gender):
            raise ValueError("The gender have to Gender class")
        return value

    def _is_valid_barcode(self, value):

        if not isinstance(value, int):
            raise ValueError("The barcode have to integer")
        return value

    def _is_valid_name(self, value):

        if not isinstance(value, str):
            raise ValueError("The gender have to string")
        return value

    def is_valid_string(self, value):
        regex = "^[0-9]"
        if not isinstance(value, str) or re.match(regex, value):
            raise ValueError("The gender have is a string whitout numbers")
        return value


class ProducList:
    def __init__(self):
        self.__products = dict()

    def __product__(self, product):

        if not isinstance(product, Product):
            raise ValueError("The product have to Product class")

    def __get_position__(self, product):
        if not product.maker in self.__products:
            self.__products[product.maker] = {}
        if not product.category in self.__products[product.maker]:
            self.__products[product.maker][product.category] = {}
        if not product.gender.value in self.__products[product.maker][product.category]:
            self.__products[product.maker][product.category][product.gender.value] = []
        return self.__products[product.maker][product.category][product.gender.value]

    def add_product(self, product):
        self.__product__(product)
        self.__get_position__(product).append(product)

    def get_products(self):
        return self.__products
