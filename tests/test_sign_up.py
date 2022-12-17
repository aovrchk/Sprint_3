from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_registration_with_correct_credentials(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Переход на регистрацию
    env.driver.find_element(By.LINK_TEXT, env.link_texts.sign_up).click()

    # Поиск текстовых полей
    inputs = env.driver.find_elements(By.TAG_NAME, env.ui.input)

    # Ввод имени
    inputs[0].send_keys(env.user.name)

    # Ввод почты
    inputs[1].send_keys(env.user.email)

    # Ввод пароля
    inputs[2].send_keys(env.user.password)

    # Нажатие на кнопку регистрации
    env.driver.find_element(By.XPATH, env.xpaths.registration_submit_button).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.login_page))

    # Завершение работы браузера
    env.driver.quit()

def test_incorrect_password(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Переход на регистрацию
    env.driver.find_element(By.LINK_TEXT, env.link_texts.sign_up).click()

    # Поиск текстовых полей
    inputs = env.driver.find_elements(By.TAG_NAME, env.ui.input)

    # Ввод имени
    inputs[0].send_keys("test")

    # Ввод почты
    inputs[1].send_keys("test@yandex.ru")

    # Ввод пароля
    inputs[2].send_keys("qwe")

    # Нажатие на кнопку регистрации
    env.driver.find_element(By.XPATH, env.xpaths.registration_submit_button).click()

    # Ожидание появления сообщения об ошибке
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.visibility_of(env.driver.find_element(By.XPATH, env.xpaths.incorrect_password_text)))

    # Завершение работы браузера
    env.driver.quit()