def get_position(product, products):
    if not product["Fabricante"] in products:
        products[product["Fabricante"]] = {}
    if not product["Categoría"] in products[product["Fabricante"]]:
        products[product["Fabricante"]][product["Categoría"]] = {}
    if not product["Género"] in products[product["Fabricante"]][product["Categoría"]]:
        products[product["Fabricante"]][product["Categoría"]][product["Género"]] = []
    return products[product["Fabricante"]][product["Categoría"]][product["Género"]]


def add_product(product, products):
    get_position(product, products).append(product)


def order_products(product_list):
    products = {}
    for product in product_list:
        add_product(product, products)
    return products
