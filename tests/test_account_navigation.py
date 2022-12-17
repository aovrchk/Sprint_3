from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_opening_account_from_main_page(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Поиск текстовых полей
    inputs = env.driver.find_elements(By.TAG_NAME, env.ui.input)

    # Ввод почты
    inputs[0].send_keys(env.user.email)

    # Ввод пароля
    inputs[1].send_keys(env.user.password)

    # Нажатие на кнопку входа
    env.driver.find_element(By.XPATH, env.xpaths.registration_submit_button).click()

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Ожидание перехода на страницу профиля
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.account))

    # Завершение работы браузера
    env.driver.quit()

def test_logout(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Поиск текстовых полей
    inputs = env.driver.find_elements(By.TAG_NAME, env.ui.input)

    # Ввод почты
    inputs[0].send_keys(env.user.email)

    # Ввод пароля
    inputs[1].send_keys(env.user.password)

    # Нажатие на кнопку входа
    env.driver.find_element(By.XPATH, env.xpaths.registration_submit_button).click()

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Ждем открытия профиля
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.account))

    # Нажатие на кнопку выхода
    env.driver.find_element(By.XPATH, env.xpaths.account_logout_button).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.login_page))

    # Завершение работы браузера
    env.driver.quit()