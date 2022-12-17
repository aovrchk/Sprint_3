import pytest
from selenium import webdriver

class User:
    # Имя пользователя
    name = "alexandra_overchuk_5_846"
    # Почта
    email = "alexandra_overchuk_5_846@mail.ru"
    # Пароль
    password = "qwerty"

class Urls:
    # Главная страница
    main_page = "https://stellarburgers.nomoreparties.site/"
    # Страница входа
    login_page = "https://stellarburgers.nomoreparties.site/login"
    # Страница аккаунта
    account = "https://stellarburgers.nomoreparties.site/account/profile"

class LinkTexts:
    account = "Личный Кабинет"
    sign_up = "Зарегистрироваться"
    sign_in = "Войти"
    restore = "Восстановить пароль"
    constructor = "Конструктор"

class UI:
    # Поле ввода текста
    input = "input"

class Xpaths:
    # Кнопка завершения регистрации/входа
    registration_submit_button = ".//form/button"
    # Текст некорректного пароля
    incorrect_password_text = ".//p[@class='input__error text_type_main-default']"
    # Кнопка аккаунта на главной
    main_page_account_button = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    # Кнопка выхода на странице профиля
    account_logout_button = ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
    # Логотип
    logo = ".//nav/div/a"
    # Секция ингредиентов
    ingredient_sections = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[1]/div"
    # Вкладка соусов
    sauces_section_title = ".//h2[contains(text(), 'Соусы')]"
    # Вкладка начинок
    contents_section_title = ".//h2[contains(text(), 'Начинки')]"
    # Вкладка булок
    buns_section_title = ".//h2[contains(text(), 'Булки')]"

class Env:
    user = User()
    urls = Urls()
    link_texts = LinkTexts()
    xpaths = Xpaths()
    ui = UI()
    wait_timeout = 1
    driver = webdriver.Chrome()

@pytest.fixture
def env():
    return Env()