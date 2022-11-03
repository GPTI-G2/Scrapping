from typing import List, Dict, Union
from tqdm import tqdm
from scrapper.tomates.models import ScrapTomates
from scrapper.licores.models import ScrapLicores


def search(scrapper: Union[ScrapTomates, ScrapLicores]) -> List[List[str]]:
    productos_filtrados = []
    for index in tqdm(range(len(scrapper.links))):
        info = scrapper.get_info_from_url(
            scrapper.links[index],
            scrapper.types[index],
            scrapper.sizes[index],
        )
        productos_filtrados.append(info)
        
    print(productos_filtrados)
    return (productos_filtrados)


"""
{"store": "Lider",
"products_list": [
  {
      "name": "Cerveza Lager Botellin2",
      "sku": "73094077",
      "brand": "Corona",
      "size": "6 Un x 330 ml c/u",
      "image_url": "https://www.lider.cl/supermercado/product/sku/993393/corona-cerveza-lager-botellin-6-un-x-330-ml-cu",
      "price": 215990,
      "type": "c-corona"
  },
  {
      "name": "Cerveza Corona botella3",
      "sku": "38111466",
      "brand": "Corona",
      "size": "330 CC x6",
      "image_url": "https://www.liquidos.cl/productos/746/cerveza-corona-botella-330-cc-x6-liquidos-cl",
      "price": 2222215890,
      "type": "c-corona"
  }
]}
"""

def format_body(keys: List[str], values: List[str]) -> Dict[str, str]:
    body = []
    print(values)
    print(values[0])
    for i in range(len(values)):
        body.append({keys[j]: values[i][j] for j in range(len(values[i]))})
    return body
