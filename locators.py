from copyreg import constructor
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Locators:

    login_button = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # Кнопка 'Войти в аккаунт'
    login_button_2 = (By.XPATH, './/p/a[@href="/login"]')  # Кнопка 'Войти' на странице авторизации
    profile_button = (By.XPATH, './/nav/a[@href="/account"]')  # Кнопка 'Личный кабинет'
    order_feed_button = (By.XPATH, './/li[2]/a[@href="/feed"]')  # Кнопка 'Лента заказов'
    imput_email = (By.XPATH, './/fieldset[1]/div/div/input')  # Поле 'email' при входе
    imput_password = (By.XPATH, './/fieldset[2]/div/div/input')  # Поле 'пароль' при входе
    imput_button = (By.XPATH, './/button[text()="Войти"]')  # Кнопка 'Войти' при входе
    constructor_button = (By.XPATH, '//p[text()="Конструктор"]')  # Кнопка 'Конструктор' на главной странице
    logo_button = (By.XPATH, './/a[@href="/"]')  # Кнопка 'логотип'
    exit_button = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')  # Кнопка 'Выйти' со странице личного профиля

    registration_button = (By.XPATH, './/p/a[@href="/register"]') # Кнопка 'Зарегестрироваться' на странице входа
    registration_button_2 = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # Кнопка 'Зарегистрироваться' на странице регистрации
    name_input = (By.XPATH, './/input[@name="name"]')  # Поле ввода 'имя'
    email_input = (By.XPATH, './/fieldset[2]/div/div/input')  # Поле вводы 'email'
    password_input = (By.XPATH, './/fieldset[3]/div/div/input')  # Поле ввода 'password'
    error = (By.XPATH, './/p[contains(@class, "input__error") and contains(text(), "Некорректный пароль")]')  # Сообщение об ошибке при некорректном пароле при регистрации
    password_recovery_button = (By.XPATH, './/p/a[@href="/forgot-password"]')  # Кнопка 'Забыли пароль'

    order_button = (By.XPATH, '/html/body/div/div/main/section[2]/div/button')  # Кнопка 'Оформить заказ' после входа на сайт

    sauces_button = (By.XPATH, './/span[text()="Соусы"]')  # Кнопка 'соусы' в конструкторе
    sauces_button_2 = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]')  # Локатор для определения нужной странице при клике кнопки 'соусы'
    buns_button = (By.XPATH, './/span[text()="Булки"]')  # Кнопка 'булки' в конструкторе
    buns_button_2 = (By.XPATH,'/html/body/div/div/main/section[1]/div[1]/div[1]')  # Локатор для определения нужной странице при клике кнопки 'булки'
    fillings_button = (By.XPATH, './/span[text()="Начинки"]')  # Кнопка 'начинки' в конструкторе
    fillings_button_2 = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]')  # Локатор для определения нужной странице при клике кнопки 'начинки'

