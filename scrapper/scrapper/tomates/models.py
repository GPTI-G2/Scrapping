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

class ScrapTomates(ABC):
  def __init__(
      self,
      links: List[str],
      classes: Dict[str, List[str]],
      expected_class: str
    ):
    self.links = links
    self.classes = classes
    self.expected_class = expected_class
    self.tags = ['div', 'span', 'h1', 'h2', 'p']
    self.columns = ["Code", "Name", "Photo", "Price", "Price x Kg"]
  
  @abstractmethod
  def get_photo_from_style_string(style: str) -> str:
    ...

  @abstractmethod
  def get_codes(self, html_soup, info):
    ...

  @abstractmethod
  def get_names(self, html_soup, info):
    ...

  @abstractmethod
  def get_photo(self, html_soup, info):
    ...

  @abstractmethod
  def get_price(self, html_soup, info):
    ...

  @abstractmethod
  def get_price_kg(self, html_soup, info):
    ...
  
  def get_info_from_url(self, url):
    html_soup = get_html_soup(url, expected_class=self.expected_class)
    info = []
    info = self.get_codes(html_soup, info)
    info = self.get_names(html_soup, info)
    info = self.get_photo(html_soup, info)
    info = self.get_price(html_soup, info)
    info = self.get_price_kg(html_soup, info)
    return info


class ScrapTomatesJumbo(ScrapTomates):
  def __init__(
      self,
      links: List[str],
      classes: Dict[str, List[str]] = {
          "code": ["product-code"], 
          "name": ["product-name"],
          "photo": ["zoomed-image"],
          "price": ["price-best", "product-sigle-price-wrapper"],
          "price_x_kg": ["product-price-ppum"]
      },
      expected_class: str = "zoomed-image"
    ):
    
    self.links = links
    self.classes = classes
    self.expected_class = expected_class
    self.tags = ['div', 'span', 'h1', 'h2', 'p']
    self.columns = ["Code", "Name", "Photo", "Price", "Price x Kg"]
  

  def get_photo_from_style_string(self, style: str) -> str:
    style_dict = style_string_to_dict(style)
    return style_dict["background-image"].split('("')[1].split("?")[0]

  def get_codes(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["code"]:
            code = (html_soup.find(tag, class_=className))
            if code:
                found = True
                break
        if found:
            break
    if found:
        try:
            code = code.string.split(" ")[1]
            info.append(code)
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

  def get_photo(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["photo"]:
            style_photo = (html_soup.find(tag, class_=className))
            if style_photo:
                found = True
                break
        if found:
            break
    if found:
        try:
            photo = self.get_photo_from_style_string(style_photo["style"])
            info.append(photo)
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

  def get_price_kg(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["price_x_kg"]:
            price_x_kg = (html_soup.find(tag, class_=className))
            if price_x_kg:
                found = True
                break
        if found:
            break
    if found:
        try:
            price_x_kg = price_x_kg.string
            price_x_kg = price_x_kg.split("$")[1].strip(")").strip(" x kg")
            info.append(price_x_kg)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info


class ScrapTomatesLider(ScrapTomates):
  def __init__(
      self,
      links: List[str],
      classes: Dict[str, List[str]] = {
          "code": ["pdp-desktop-item-number"],
          "name": ["product-detail-display-name"],
          "photo": ["styled__FigureContainer-sc-13lpau7-2"],
          "price": ["pdp-mobile-sales-price"],
          "price_x_kg": ["price-per-um__pdp"]
      },
      expected_class: str = "styled__FigureContainer-sc-13lpau7-2"
    ):
    
    self.links = links
    self.classes = classes
    self.expected_class = expected_class
    self.tags = ['div', 'span', 'h1', 'h2', 'p']
    self.columns = ["Code", "Name", "Photo", "Price", "Price x Kg"]
  

  def get_photo_from_style_string(self, style: str) -> str:
    style_dict = style_string_to_dict(style)
    return style_dict["background-image"].split('("')[1].split(")")[0]

  def get_codes(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["code"]:
            code = (html_soup.find(tag, class_=className))
            if code:
                found = True
                break
        if found:
            break
    if found:
        try:
            code = code.string.split(" ")[1]
            info.append(code)
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

  def get_photo(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["photo"]:
            style_photo = (html_soup.find(tag, class_=className)).find("figure", recursive=False)
            if style_photo:
                found = True
                break
        if found:
            break
    if found:
        try:
            photo = self.get_photo_from_style_string(style_photo["style"])
            info.append(photo)
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

  def get_price_kg(self, html_soup, info):
    found = False
    for tag in self.tags:
        for className in self.classes["price_x_kg"]:
            price_x_kg = (html_soup.find(tag, class_=className))
            if price_x_kg:
                found = True
                break
        if found:
            break
    if found:
        try:
            price_x_kg = price_x_kg.string
            price_x_kg = price_x_kg.split("$")[1].strip(")").strip(" x kg")
            info.append(price_x_kg)
        except Exception as e:
            print(e)
            info.append(None)
    else:
        info.append(None)
    return info

