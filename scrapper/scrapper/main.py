# from scrapper.tomates.models import ScrapTomatesJumbo, ScrapTomatesLider
from scrapper.licores.models import ScrapLicoresJumbo, ScrapLicoresLider
from scrapper.driver.search import search

# Tomates
# links_jumbo = [
#     "https://www.jumbo.cl/tomate-larga-vida-granel/p",
#     "https://www.jumbo.cl/tomate-malla-1-kg/p",
#     "https://www.jumbo.cl/tomate-salad-granel/p",
#     "https://www.jumbo.cl/tomate-jumbo-granel-beef-2/p"
# ]
# scrapper_jumbo = ScrapTomatesJumbo(links_jumbo)

# links_lider = [
#     "https://www.lider.cl/supermercado/product/sku/327604/tomates-tomate-larga-vida-granel-500-g-2-a-3-un-aprox",
#     "https://www.lider.cl/supermercado/product/sku/325702/tomates-tomate-larga-vida-malla-1-kg",
#     "https://www.lider.cl/supermercado/product/sku/452098/tomates-tomate-pera-granel-500-g-3-a-4-un-aprox",
#     "https://www.lider.cl/supermercado/product/sku/323558/tomates-tomate-beef-granel-500-g"
# ]
# scrapper_lider = ScrapTomatesLider(links_lider)

# productos_jumbo = search(scrapper_jumbo)
# productos_lider = search(scrapper_lider)

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
    types= links_jumbo.keys(),
    links = links_jumbo.values(),
    sizes = sizes,
)

scrapper_lider = ScrapLicoresLider(
    types= links_lider.keys(),
    links = links_lider.values(),
    sizes = sizes,
)

productos_jumbo = search(scrapper_jumbo)
productos_lider = search(scrapper_lider)
