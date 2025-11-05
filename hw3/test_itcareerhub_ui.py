from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# проверка, что на странице отображается логотип ITCareerHub

def test_logo_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    logo_element = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.scrollback.tn-elem__13452848611709290178271 img"
    )
    assert logo_element.is_displayed()

# проверка, что на странице отображается cсылка “Программы”

def test_program_link_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    program_link = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.t396__elem-flex.tn-elem__13452582811754487411327  span"
)
    assert program_link.is_displayed()

# проверка, что на странице отображается cсылка “Способы оплаты”

def test_payment_methods_link_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    payment_methods_link = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.t396__elem-flex.tn-elem__13452582811754487411320 span"
    )
    assert payment_methods_link.is_displayed()

# проверка, что на странице отображается cсылка “Новости”

def test_news_link_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    news_link = driver.find_element(
        By.CSS_SELECTOR, "#sbs-1346520371-175888213715344620 span"
    )
    assert news_link.is_displayed()

# проверка, что на странице отображается c "О нас"

def test_about_link_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    about_link = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.t396__elem-flex.tn-elem__13452582811754487411331 span"
    )
    assert about_link.is_displayed()

# проверка, что на странице отображается cсылка "Отзывы"

def test_reviews_link_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    reviews_link = driver.find_element(
        By.CSS_SELECTOR, "div.t396__elem.tn-elem.t396__elem-flex.tn-elem__13452582811754487411336 span"
    )
    assert reviews_link.is_displayed()

# проверка, что на странице отображаются кнопка переключения языка "ru"

def test_language_switcher_ru_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    language_switcher_ru = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.tn-elem__13452582811710152827519 span"
    )
    assert language_switcher_ru.is_displayed()

# проверка, что на странице отображаются кнопка переключения языка "de"

def test_language_switcher_de_displayed(driver):
    driver.get("https://itcareerhub.de/ru")
    language_switcher_de = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.tn-elem__13452582811710153064158 a"
    )
    assert language_switcher_de.is_displayed()




#test_phone_icon_click