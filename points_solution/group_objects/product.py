def get_position(product, products):
    if not product.maker in products:
        products[product.maker] = {}
    if not product.category in products[product.maker]:
        products[product.maker][product.category] = {}
    if not product.gender.value in products[product.maker][product.category]:
        products[product.maker][product.category][product.gender.value] = []
    return products[product.maker][product.category][product.gender.value]


def add_product(product, products):
    get_position(product, products).append(product)


def get_products(product_list):
    products = {}
    for product in product_list:
        add_product(product, products)
    return products
