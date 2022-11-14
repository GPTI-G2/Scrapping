from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)

def get_html_soup(url: str, expected_class: str):
    print("")
    print("Doing request!")
    print("Expected class is:", expected_class)
    driver.get(url)
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, expected_class))
    )
    datos = driver.execute_script("return document.body.innerHTML")
    print("Request executed!")
    return BeautifulSoup(datos, "html.parser")
