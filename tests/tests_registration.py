import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time

class TestsRegistration:

    def test_successful_registration_with_valid_data(self, browser, random_email, random_password):
        button_login = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.login_button))
        button_login.click()

        button_registration = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.registration_button))
        button_registration.click()

        input_name = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.name_input))
        input_name.send_keys('Любое Имя')

        input_email = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.email_input))
        input_email.send_keys(random_email)

        input_password = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.password_input))
        input_password.send_keys(random_password)

        button_registration_2 = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.registration_button_2))
        button_registration_2.click()

        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/register'


    def test_invalid_password_error_during_registration(self, browser, random_email):
        button_login = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.login_button))
        button_login.click()

        button_registration = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.registration_button))
        button_registration.click()

        input_name = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.name_input))
        input_name.send_keys('Любое Имя')
        time.sleep(1)

        input_email = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.email_input))
        input_email.send_keys(random_email)
        time.sleep(1)

        input_password = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.password_input))
        input_password.send_keys('123')

        button_registration_2 = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(Locators.registration_button_2))
        button_registration_2.click()

        error_message = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(Locators.error))

        assert 'Некорректный пароль' in error_message.text

