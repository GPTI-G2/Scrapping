from scrapper.licores.models import ScrapLicoresJumbo, ScrapLicoresLider
from scrapper.driver.search import search, format_body


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

sizes = [
    "1 x 750 cc.",
    "1 x 1000 cc.",
    "1 x 750 cc.",
    "6 x 330 cc.",
    "12 x 350 cc."
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

productos_jumbo = search(scrapper_jumbo)
productos_lider = search(scrapper_lider)

print(productos_jumbo)
print(productos_lider)

#TODO: sent data to backend
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


