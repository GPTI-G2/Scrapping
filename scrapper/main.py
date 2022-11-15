from scrapper.licores.models import ScrapLicoresJumbo, ScrapLicoresLider, ScrapLicoresLiquidos
from scrapper.driver.search import search, format_body
from scrapper.api_connection.store import post_products_to_store

# Licores
links_lider = {
    "alto-normal-750": "https://www.lider.cl/supermercado/product/sku/1361/alto-del-carmen-pisco-especial-35-botella-750-ml",
    "alto-normal-1000": "https://www.lider.cl/supermercado/product/sku/468481/alto-del-carmen-pisco-especial-35-botella-1-l",
    "mistral-normal-750": "https://www.lider.cl/supermercado/product/sku/1375/mistral-pisco-35-especial-anejado-en-roble-botella-750-cc",
    "corona-6-330": "https://www.lider.cl/supermercado/product/sku/993393/corona-cerveza-lager-botellin-6-un-x-330-ml-cu",
    "royal-guard-12-350": "https://www.lider.cl/supermercado/product/sku/704136/royal-guard-pack-cerveza-lager-latas-12-un"
}


links_jumbo = {
    "alto-normal-750": "https://www.jumbo.cl/pisco-alto-del-carmen-750-cc-35-gl-especial-botella-verde/p",
    "alto-normal-1000": "https://www.jumbo.cl/pisco-alto-del-carmen-1-l-35/p",
    "mistral-normal-750": "https://www.jumbo.cl/pisco-mistral-750-cc-35/p",
    "corona-6-330": "https://www.jumbo.cl/cerveza-corona-botella-6x330cc-2/p",
    "royal-guard-12-350": "https://www.jumbo.cl/cerveza-royal-guard-pack-12-unid-lata-350-cc-cu/p",
}

links_liquidos = {
    "alto-normal-1000": "https://www.liquidos.cl/productos/1180/pisco-alto-del-carmen-1-litro-35-grados-liquidos-cl",
    "mistral-normal-750": "https://www.liquidos.cl/productos/18987/pisco-mistral-35-botella-750cc",
    "corona-6-330": "https://www.liquidos.cl/productos/746/cerveza-corona-botella-330-cc-x6-liquidos-cl",
}

sizes = [
    "1 x 750 cc.",
    "1 x 1000 cc.",
    "1 x 750 cc.",
    "6 x 330 cc.",
    "12 x 350 cc."
]

sizes_liquidos = [
    "1 x 1000 cc.",
    "1 x 750 cc.",
    "6 x 330 cc."
]

scrapper_jumbo = ScrapLicoresJumbo(
    types= list(links_jumbo.keys()),
    links = list(links_jumbo.values()),
    sizes = sizes,
    store = "Jumbo"
)

scrapper_lider = ScrapLicoresLider(
    types= list(links_lider.keys()),
    links = list(links_lider.values()),
    sizes = sizes,
    store = "Lider"
)

scrapper_liquidos = ScrapLicoresLiquidos(
    types= list(links_liquidos.keys()),
    links = list(links_liquidos.values()),
    sizes = sizes_liquidos,
    store = "Liquidos"
)

productos_jumbo = search(scrapper_jumbo)
productos_lider = search(scrapper_lider)
productos_liquidos = search(scrapper_liquidos)

print(productos_jumbo)
print(productos_lider)
print(productos_liquidos)

keys = [
    "sku",
    "name",
    "brand",
    "size",
    "image_url",
    "price",
    "type",
    "store"
]

body_jumbo = format_body(
    keys=keys,
    values=productos_jumbo
)
body_lider = format_body(
    keys=keys,
    values=productos_lider
)
body_liquidos = format_body(
    keys=keys,
    values=productos_liquidos
)

try:
    post_products_to_store(
        store="Lider",
        products_list=body_lider
    )
except Exception as e:
    print(e)
    print("No se pudo realizar la request al lider!")

try:
    post_products_to_store(
        store="Jumbo",
        products_list=body_jumbo
    )
except Exception as e:
    print(e)
    print("No se pudo realizar la request al jumbo!")

try:
    post_products_to_store(
        store="Liquidos",
        products_list=body_liquidos
    )
except Exception as e:
    print(e)
    print("No se pudo realizar la request al liquidos!")

