""" 3.6. Задание: запуск автотестов для разных языков интерфейса
Тест наличия кнопки Добавить в корзину.
фикстура в conftest.py
Тест запускается pytest --language=es test_items.py , где es - язык (ru , fr и т.д.)
"""
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_basket_exist(browser):
    browser.get(link)
    time.sleep(30)
    # btn btn-lg btn-primary btn-add-to-basket
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button != None
