import requests
import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_browser():
    """
    Test case WERT-1: Open url testqastudio.me
    """
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"

    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url='https://testqastudio.me/')

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
	

    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()

    sku = driver.find_element(By.CLASS_NAME, value="sku")

    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"

    #[class="product_title entry-title"]>h1
    assert True,''


#11341
	


   

    