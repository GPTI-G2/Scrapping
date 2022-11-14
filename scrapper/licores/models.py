from abc import ABC, abstractmethod
from typing import List, Dict
from scrapper.driver.driver import get_html_soup

def style_string_to_dict(style: str) -> Dict[str, str]:
  attributes = style.strip(";").split("; ")
  style_dict = {}
  for line in attributes:
    [key, value] = line.split(": ")
    style_dict[key] = value
  return style_dict

class ScrapLicores(ABC):
  def __init__(
      self,
      types: List[str],
      links: List[str],
      sizes: List[str],
      classes: Dict[str, List[str]],
      expected_class: str,
      store: str
    ):
    self.links = links
    self.classes = classes
    self.types = types
    self.sizes = sizes
    self.expected_class = expected_class
    self.store = store
    self.tags = ['div', 'span', 'h1', 'h2', 'p', 'img']
    self.columns = ["sku", "Name", "image_url", "Price"]
  
  @abstractmethod
  def get_image_url_from_style_string(style: str) -> str:
    ...

  @abstractmethod
  def get_skus(self, html_soup, info):
    ...

  @abstractmethod
  def get_brand(self, html_soup, info):
    ...
  
  @abstractmethod
  def get_names(self, html_soup, info):
    ...

  @abstractmethod
  def get_image_url(self, html_soup, info):
    ...

  @abstractmethod
  def get_price(self, html_soup, info):
    ...

  
  def get_info_from_url(self, url, product_type, size):
    html_soup = get_html_soup(url, expected_class=self.expected_class)
    info = []
    info = self.get_skus(html_soup, info)
    info = self.get_brand(html_soup, info)
    info = self.get_names(html_soup, info)
    info.append(size)
    info = self.get_image_url(html_soup, info)
    info = self.get_price(html_soup, info)
    info.append(product_type)
    info.append(self.store)
    return info


class ScrapLicoresJumbo(ScrapLicores):
  def __init__(
      self,
      types: List[str],
      links: List[str],
      sizes: List[str],
      classes: Dict[str, List[str]] = {
          "sku": ["product-code"], 
          "name": ["product-name"],
          "brand": ["product-brand"],
          "image_url": ["zoomed-image"],
          "price": ["price-best", "product-sigle-price-wrapper"],
      },
      expected_class: str = "zoomed-image",
      store: str = None,
    ):
    
    self.links = links
    self.classes = classes
    self.types = types
    self.sizes = sizes
    self.expected_class = expected_class
    self.store = store
    self.tags = ['div', 'span', 'h1', 'h2', 'p', "a"]
    self.columns = ["sku", "Name", "image_url", "Price"]
  

  def get_image_url_from_style_string(self, style: str) -> str:
    style_dict = style_string_to_dict(style)
    return style_dict["background-image"].split('("')[1].split("?")[0]

  def get_skus(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["sku"]:
            sku = (html_soup.find(tag, class_=className))
            if sku:
                found = True
                break
        if found:
            break
    if found:
        try:
            sku = sku.string.split(" ")[1]
            info.append(sku)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

  def get_names(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["name"]:
            name = (html_soup.find(tag, class_=className))
            if name:
                found = True
                break
        if found:
            break
    if found:
        try:
            name = name.string
            info.append(name)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

  def get_brand(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["brand"]:
            brand = (html_soup.find(tag, class_=className))
            if brand:
                found = True
                break
        if found:
            break
    if found:
        try:
            brand = brand.string
            info.append(brand)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

  def get_image_url(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["image_url"]:
            style_image_url = (html_soup.find(tag, class_=className))
            if style_image_url:
                found = True
                break
        if found:
            break
    if found:
        try:
            image_url = self.get_image_url_from_style_string(style_image_url["style"])
            info.append(image_url)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

  def get_price(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["price"]:
            price = (html_soup.find(tag, class_=className))
            if price:
                found = True
                break
        if found:
            break
    if found:
        try:
            price = price.string.strip("$")
            info.append(price)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info


class ScrapLicoresLider(ScrapLicores):
  def __init__(
      self,
      types: List[str],
      links: List[str],
      sizes: List[str],
      classes: Dict[str, List[str]] = {
          "sku": ["pdp-desktop-item-number"],
          "name": ["product-detail-display-name"],
          "brand": ["prduct-detail-cart__brand-link"],
          "image_url": ["styled__FigureContainer-sc-13lpau7-2"],
          "price": ["pdp-mobile-sales-price"],
      },
      expected_class: str = "styled__FigureContainer-sc-13lpau7-2",
      store: str = None,
    ):
    
    self.links = links
    self.types = types
    self.sizes = sizes
    self.classes = classes
    self.store = store
    self.expected_class = expected_class
    self.tags = ['div', 'span', 'h1', 'h2', 'p', 'a']
    self.columns = ["sku", "Name", "image_url", "Price"]
  

  def get_image_url_from_style_string(self, style: str) -> str:
    style_dict = style_string_to_dict(style)
    return style_dict["background-image"].split('("')[1].split(")")[0]

  def get_skus(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["sku"]:
            sku = (html_soup.find(tag, class_=className))
            if sku:
                found = True
                break
        if found:
            break
    if found:
        try:
            sku = sku.string.split(" ")[1]
            info.append(sku)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

  def get_names(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["name"]:
            name = (html_soup.find(tag, class_=className))
            if name:
                found = True
                break
        if found:
            break
    if found:
        try:
            name = name.string
            info.append(name)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

  def get_brand(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["brand"]:
            brand = (html_soup.find(tag, class_=className))
            if brand:
                found = True
                break
        if found:
            break
    if found:
        try:
            brand = brand.string
            info.append(brand)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

  def get_image_url(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["image_url"]:
            style_image_url = (html_soup.find(tag, class_=className)).find("figure", recursive=False)
            if style_image_url:
                found = True
                break
        if found:
            break
    if found:
        try:
            image_url = self.get_image_url_from_style_string(style_image_url["style"])
            info.append(image_url)
        except:
            info.append(None)
    else:
        info.append(None)
    return info

  def get_price(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["price"]:
            price = (html_soup.find(tag, class_=className))
            if price:
                found = True
                break
        if found:
            break
    if found:
        try:
            price = price.string.strip("$")
            info.append(price)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

class ScrapLicoresLiquidos(ScrapLicores):
    def __init__(
      self,
      types: List[str],
      links: List[str],
      sizes: List[str],
      classes: Dict[str, List[str]] = {
          "sku": ["jss11"],
          "name": ["jss11"],
          "brand": ["jss11"],
          "image_url": ["jss8"],
          "price": ["jss14"],
      },
      expected_class: str = "jss8",
      store: str = None,
    ):
    
        self.links = links
        self.types = types
        self.sizes = sizes
        self.classes = classes
        self.store = store
        self.expected_class = expected_class
        self.tags = ['div', 'span', 'h1', 'h2', 'p', 'a', 'img']
        self.columns = ["sku", "Name", "image_url", "Price"]

    def get_image_url_from_style_string(self, *args):
        print("Won't use")
        pass

    def get_skus(self, html_soup, info):
        found = False
        for tag in self.tags:
            for className in self.classes["sku"]:
                sku = (html_soup.find(tag, class_=className)).find("h1", recursive=False)
                if sku:
                    found = True
                    break
            if found:
                break
        if found:
            try:
                sku = sku.string
                info.append(sku)
            except Exception as e:
                print(e)
                info.append(None)
        else:
            info.append(None)
        return info

    def get_names(self, html_soup, info):
        found = False
        for tag in self.tags:
            for className in self.classes["name"]:
                name = (html_soup.find(tag, class_=className)).find("h1", recursive=False)
                if name:
                    found = True
                    break
            if found:
                break
        if found:
            try:
                name = name.string
                info.append(name)
            except Exception as e:
                print(e)
                info.append(None)
        else:
            info.append(None)
        return info

    def get_brand(self, html_soup, info):
        found = False
        for tag in self.tags:
            for className in self.classes["brand"]:
                brand = (html_soup.find(tag, class_=className)).find("h1", recursive=False)
                if brand:
                    found = True
                    break
            if found:
                break
        if found:
            try:
                brand = brand.string
                info.append(brand)
            except Exception as e:
                print(e)
                info.append(None)
        else:
            info.append(None)
        return info

    def get_image_url(self, html_soup, info):
        found = False
        for tag in self.tags:
            for className in self.classes["image_url"]:
                style_image_url = (html_soup.find(tag, class_=className))
                if style_image_url:
                    found = True
                    break
            if found:
                break
        if found:
            try:
                print(style_image_url)
                image_url = style_image_url["src"]
                info.append(image_url)
            except:
                info.append(None)
        else:
            info.append(None)
        return info
    def get_price(self, html_soup, info):
        found = False
        for tag in self.tags:
            for className in self.classes["price"]:
                price = (html_soup.find(tag, class_=className))
                if price:
                    found = True
                    break
            if found:
                break
        if found:
            try:
                price = price.string.split("$")[1]
                info.append(price)
            except Exception as e:
                print(e)
                info.append(None)
        else:
            info.append(None)
        return info
