from typing import List
from tqdm import tqdm
from scrapper.tomates.models import ScrapTomates


def search(scrapper: ScrapTomates) -> List[List[str]]:
    productos_filtrados = []
    for index in tqdm(range(len(scrapper.links))):
        info = scrapper.get_info_from_url(scrapper.links[index])
        productos_filtrados.append(info)
    print(productos_filtrados)
    return (productos_filtrados)
