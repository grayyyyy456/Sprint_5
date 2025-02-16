import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def random_email():
    login = str(random.randint(10, 99999))
    domain = 'ya.ru'
    return f'{login}@{domain}'

@pytest.fixture(scope='function')
def random_password():
    password = str(random.randint(10000, 99999999))
    return password

