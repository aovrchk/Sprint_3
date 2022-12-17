from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_signing_in(env):
    # Открытие страницы
    env.driver.get(env.urls.login_page)

    # Поиск текстовых полей
    inputs = env.driver.find_elements(By.TAG_NAME, env.ui.input)

    # Ввод почты
    inputs[0].send_keys(env.user.email)

    # Ввод пароля
    inputs[1].send_keys(env.user.password)

    # Нажатие на кнопку входа
    env.driver.find_element(By.XPATH, env.xpaths.registration_submit_button).click()

    # Ожидание перехода на главную страницу
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.main_page))

    # Завершение работы браузера
    env.driver.quit()

def test_sign_in_from_main_page(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.XPATH, env.xpaths.main_page_account_button).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.login_page))

    # Завершение работы браузера
    env.driver.quit()

def test_sign_in_from_account_page(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.login_page))

    # Завершение работы браузера
    env.driver.quit()

def test_sign_in_from_sign_up_page(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Переход на регистрацию
    env.driver.find_element(By.LINK_TEXT, env.link_texts.sign_up).click()

    # Переход на вход
    env.driver.find_element(By.LINK_TEXT, env.link_texts.sign_in).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.login_page))

    # Завершение работы браузера
    env.driver.quit()

def test_sign_in_from_password_restoration_page(env,):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Переход на восстановление
    env.driver.find_element(By.LINK_TEXT, env.link_texts.restore).click()

    # Переход на вход
    env.driver.find_element(By.LINK_TEXT, env.link_texts.sign_in).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.login_page))

    # Завершение работы браузера
    env.driver.quit()