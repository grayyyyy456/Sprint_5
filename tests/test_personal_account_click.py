import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time
from selenium.webdriver.common.by import By
import unittest


class TestClickPersonalAccount:
    def test_navigation_to_personal_account(self, browser_account_authorization):
        button_profile = WebDriverWait(browser_account_authorization, 10).until(expected_conditions.element_to_be_clickable(Locators.profile_button))
        button_profile.click()
        time.sleep(3)
        assert browser_account_authorization.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'