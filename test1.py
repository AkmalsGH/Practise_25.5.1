from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def set():
   driver = webdriver.Chrome('/Users/a11/Downloads/chromedriver_mac64/chromedriver')
   driver.get('http://petfriends.skillfactory.ru/login')

   yield

   driver.quit()