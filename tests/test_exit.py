import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time
from selenium.webdriver.common.by import By



class TestClickPersonalAccount:
    def test_logout_from_personal_account(self, browser_account_authorization):
        button_profile = WebDriverWait(browser_account_authorization, 10).until(expected_conditions.element_to_be_clickable(Locators.profile_button))
        button_profile.click()
        time.sleep(3)
        button_exit = WebDriverWait(browser_account_authorization, 10).until(expected_conditions.element_to_be_clickable(Locators.exit_button))
        button_exit.click()
        time.sleep(3)
        assert browser_account_authorization.current_url == 'https://stellarburgers.nomoreparties.site/login'

