import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time
from selenium.webdriver.common.by import By

class TestConstructor:
    def test_navigation_to_constructor_from_personal_account(self,browser_account_authorization):
        button_profile = WebDriverWait(browser_account_authorization, 10).until(expected_conditions.element_to_be_clickable(Locators.profile_button))
        button_profile.click()
        time.sleep(3)
        WebDriverWait(browser_account_authorization, 10).until(expected_conditions.element_to_be_clickable(Locators.constructor_button)).click()
        url_constructor = 'https://stellarburgers.nomoreparties.site/'
        assert browser_account_authorization.current_url == url_constructor

    def test_navigation_to_logo_from_personal_account(self, browser_account_authorization):
        button_profile = WebDriverWait(browser_account_authorization, 10).until(expected_conditions.element_to_be_clickable(Locators.profile_button))
        button_profile.click()
        time.sleep(3)
        WebDriverWait(browser_account_authorization, 10).until(expected_conditions.element_to_be_clickable(Locators.logo_button)).click()
        assert browser_account_authorization.current_url == 'https://stellarburgers.nomoreparties.site/'

