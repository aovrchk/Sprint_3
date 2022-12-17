from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_opening_constructor_from_account_page(env):
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

    # Переход в конструктор
    env.driver.find_element(By.LINK_TEXT, env.link_texts.constructor).click()

    # Ожидание перехода на главную
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.main_page))

    # Завершение работы браузера
    env.driver.quit()

def test_opening_constructor_by_tapping_logo(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Переход в личный кабинет
    env.driver.find_element(By.LINK_TEXT, env.link_texts.account).click()

    # Нажатие на логотип
    env.driver.find_element(By.XPATH, env.xpaths.logo).click()

    # Ожидание перехода на главную
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.url_contains(env.urls.main_page))

    # Завершение работы браузера
    env.driver.quit()

def test_navigating_to_sauces_section(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Поиск разделов
    sections = env.driver.find_elements(By.XPATH, env.xpaths.ingredient_sections)

    # Нажатие на "Соусы"
    sections[1].click()

    # Ожидаем, что заголовок соусов появится на экране
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.visibility_of(env.driver.find_element(By.XPATH, env.xpaths.sauces_section_title)))

    # Завершение работы браузера
    env.driver.quit()

def test_navigating_to_contents_section(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Поиск разделов
    sections = env.driver.find_elements(By.XPATH, env.xpaths.ingredient_sections)

    # Нажатие на "Начинки"
    sections[2].click()

    # Ожидаем, что заголовок соусов появится на экране
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.visibility_of(env.driver.find_element(By.XPATH, env.xpaths.contents_section_title)))

    # Завершение работы браузера
    env.driver.quit()

def test_navigating_to_buns_section(env):
    # Открытие страницы
    env.driver.get(env.urls.main_page)

    # Поиск разделов
    sections = env.driver.find_elements(By.XPATH, env.xpaths.ingredient_sections)

    # Нажатие на "Начинки"
    sections[2].click()

    # Нажатие на "Булки"
    sections[0].click()

    # Ожидаем, что заголовок соусов появится на экране
    WebDriverWait(env.driver, env.wait_timeout).until(expected_conditions.visibility_of(env.driver.find_element(By.XPATH, env.xpaths.buns_section_title)))

    # Завершение работы браузера
    env.driver.quit()