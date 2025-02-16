import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time
from selenium.webdriver.common.by import By

class TestConstructor:
    def test_navigation_to_constructor_from_personal_account(self,browser):
        button_login = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(Locators.login_button))
        button_login.click()
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.imput_email)).send_keys('sergeishiraev15999@yandex.ru')
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.imput_password)).send_keys('12345678')
        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.imput_button)).click()
        button_profile = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.profile_button))
        button_profile.click()
        time.sleep(3)
        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.constructor_button)).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigation_to_logo_from_personal_account(self, browser):
        button_login = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(Locators.login_button))
        button_login.click()
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.imput_email)).send_keys('sergeishiraev15999@yandex.ru')
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.imput_password)).send_keys('12345678')
        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.imput_button)).click()
        button_profile = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.profile_button))
        button_profile.click()
        time.sleep(3)
        WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.logo_button)).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'

