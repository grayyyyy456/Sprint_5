import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time
from selenium.webdriver.common.by import By

class TestConstructorSections:
    def test_navigate_to_sauces_section(self, browser):
        sauces_button = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.sauces_button))
        sauces_button.click()
        time.sleep(3)
        button_2 = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.sauces_button_2))
        assert 'tab_tab_type_current__2BEPc' in button_2.get_attribute('class')

    def test_navigate_to_buns_section(self, browser):
        sauces_button = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.sauces_button))
        sauces_button.click()
        buns_button = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.buns_button))
        buns_button.click()
        time.sleep(3)
        button_1 = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.buns_button_2))
        assert 'tab_tab_type_current__2BEPc' in button_1.get_attribute('class')

    def test_navigate_to_fillings_section(self, browser):
        fillings_button = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.fillings_button))
        fillings_button.click()
        time.sleep(3)
        button_3= WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.fillings_button_2))
        assert 'tab_tab_type_current__2BEPc' in button_3.get_attribute('class')

