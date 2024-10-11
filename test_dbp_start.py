from playwright.sync_api import sync_playwright
from config_dbp import *

# Локаторы
locators = {
    "locator_button_login": "a#login2",
    "locator_modal_login": "#logInModal",
    "locator_field_user_name": "#loginusername",
    "locator_field_user_pass": "#loginpassword",
    "locator_button_login_modal": "#logInModal > div > div > div.modal-footer > button.btn.btn-primary",
    "locator_button_logout": "#logout2",
    "locator_cat": "#cat",
    "locator_cat_phones": "a#itemc[onclick=\"byCat('phone')\"]",
    "locator_cat_laptops": "a#itemc[onclick='byCat(\\'notebook\\')']",
    "locator_cat_monitors": "a#itemc[onclick='byCat(\\'monitor\\')']",
    "locator_cat_phones_product_2": "#tbodyid > div:nth-child(2) > div > div > h4",
    "locator_cat_laptops_product_3": "#tbodyid > div:nth-child(3)",
    "locator_cat_monitors_product_1": "#tbodyid > div:nth-child(1)",
    "locator_shopping_cart": "#cartur",
    "locator_button_Add_to_cart": "a.btn.btn-success.btn-lg",
    "locator_button_plase_order": "#page-wrapper > div > div.col-lg-1 > button",
    "locator_button_plase_order_name": "#name",
    "locator_button_plase_order_country": "#country",
    "locator_button_plase_order_City": "#city",
    "locator_button_plase_order_Creditcard": "#card",
    "locator_button_plase_order_Month": "#month",
    "locator_button_plase_order_Year": "#year",
    "locator_button_plase_order_purchase": "#orderModal > div > div > div.modal-footer > button.btn.btn-primary",
    "locator_button_plase_order_ok": "body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button",
    "locator_button_plase_order_close": "#orderModal > div > div > div.modal-footer > button.btn.btn-secondary",
    "locator_modal_plase_order": "#orderModal"  # Локатор для модального окна plase_order
}

def test_demoblaze_checking_locators(): #проверка локаторов на странице входа и выбора товаров
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")
        result = page.evaluate("document.querySelector('#login2') !== null")# Проверка локатора для кнопки "Log in"
        print("Кнопка Log in верна")
        assert result, "Кнопка 'Log in' не найдена"

        # Клик по кнопке "Log in" для открытия модального окна
        page.click(locators["locator_button_login"])# Клик по кнопке "Log in" для открытия модального окна
        page.wait_for_selector(locators["locator_modal_login"])# Ожидание открытия модального окна
        modal_login = page.locator(locators["locator_modal_login"])# Проверка, что модальное окно видно
        assert modal_login.is_visible(), "Модальное окно логина не видно"
        print("Модальное окно логина видно")

        field_user_name = page.locator(locators["locator_field_user_name"])
        assert field_user_name.is_visible(), "Поле ввода имени пользователя не видно"
        print("Поле ввода имени пользователя видно")

        field_user_pass = page.locator(locators["locator_field_user_pass"])
        assert field_user_pass.is_visible(), "Поле ввода пароля не видно"
        print("Поле ввода пароля видно")

        button_login_modal = page.locator(locators["locator_button_login_modal"])
        assert button_login_modal.is_visible(), "Кнопка 'Log in' в модальном окне не видна"
        print("Кнопка 'Log in' в модальном окне видна")

        result = page.evaluate("document.querySelector('#logout2') !== null")  # Проверка локатора для кнопки "Logout"
        print("Кнопка Logout верна")
        assert result, "Кнопка 'Logout' не найдена"

        # Проверка, что элемент с локатором locator_cat виден
        cat_element = page.locator(locators["locator_cat"])
        assert cat_element.is_visible(), "Элемент с локатором 'locator_cat' не виден"
        print("Элемент с локатором 'locator_cat' виден")

        cat_phones_element = page.locator(locators["locator_cat_phones"])
        assert cat_phones_element.is_visible(), "Элемент с локатором 'locator_cat_phones' не виден"
        print("Элемент с локатором 'locator_cat_phones' виден")

        cat_monitors_element = page.locator(locators["locator_cat_monitors"])
        assert cat_monitors_element.is_visible(), "Элемент с локатором 'locator_cat_monitors' не виден"
        print("Элемент с локатором 'locator_cat_monitors' виден")

        cat_laptops_element = page.locator(locators["locator_cat_laptops"])
        assert cat_laptops_element.is_visible(), "Элемент с локатором 'locator_cat_laptops' не виден"
        print("Элемент с локатором 'locator_cat_laptops' виден")

        page.wait_for_selector(locators["locator_cat_phones_product_2"])
        # Проверка, что элемент с локатором locator_cat_phones_product_2 виден
        cat_phones_product_2_element = page.locator(locators["locator_cat_phones_product_2"])
        assert cat_phones_product_2_element.is_visible(), "Элемент с локатором 'locator_cat_phones_product_2' не виден"
        print("Элемент с локатором 'locator_cat_phones_product_2' виден")

        page.wait_for_selector(locators["locator_cat_laptops_product_3"])
        # Проверка, что элемент с локатором locator_cat_laptops_product_3 виден
        cat_laptops_product_3_element = page.locator(locators["locator_cat_laptops_product_3"])
        assert cat_laptops_product_3_element.is_visible(), "Элемент с локатором 'locator_cat_laptops_product_3' не виден"
        print("Элемент с локатором 'locator_cat_laptops_product_3' виден")

        page.wait_for_selector(locators["locator_cat_monitors_product_1"])
        # Проверка, что элемент с локатором locator_cat_monitors_product_1 виден
        cat_monitors_product_1_element = page.locator(locators["locator_cat_monitors_product_1"])
        assert cat_monitors_product_1_element.is_visible(), "Элемент с локатором 'locator_cat_monitors_product_1' не виден"
        print("Элемент с локатором 'locator_cat_monitors_product_1' виден")

        # Проверка, что элемент с локатором locator_shopping_cart виден
        shopping_cart_element = page.locator(locators["locator_shopping_cart"])
        assert shopping_cart_element.is_visible(), "Элемент с локатором 'locator_shopping_cart' не виден"
        print("Элемент с локатором 'locator_shopping_cart' виден")

        browser.close()

def test_demoblaze_checkingcart_locators(): #проверка локаторов на странице корзины
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/cart.html")

        # Проверка, что элемент с локатором locator_button_plase_order виден
        plase_order_button_element = page.locator(locators["locator_button_plase_order"])
        assert plase_order_button_element.is_visible(), "Элемент с локатором 'locator_button_plase_order' не виден"
        print("Элемент с локатором 'locator_button_plase_order' виден")

        # Клик по кнопке "Place Order" для открытия модального окна оформления заказа
        page.click(locators["locator_button_plase_order"])
        page.wait_for_selector(locators["locator_modal_plase_order"])  # Ожидание открытия модального окна

        # Проверка, что модальное окно plase_order видно
        plase_order_modal_element = page.locator(locators["locator_modal_plase_order"])
        assert plase_order_modal_element.is_visible(), "Модальное окно 'plase_order' не видно"
        print("Модальное окно 'plase_order' видно")

        # Проверка, что элемент с локатором locator_button_plase_order_name виден
        plase_order_name_element = page.locator(locators["locator_button_plase_order_name"])
        assert plase_order_name_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_name' не виден"
        print("Элемент с локатором 'locator_button_plase_order_name' виден")

        # Проверка, что элемент с локатором locator_button_plase_order_country виден
        plase_order_country_element = page.locator(locators["locator_button_plase_order_country"])
        assert plase_order_country_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_country' не виден"
        print("Элемент с локатором 'locator_button_plase_order_country' виден")

        # Проверка, что элемент с локатором locator_button_plase_order_City виден
        plase_order_City_element = page.locator(locators["locator_button_plase_order_City"])
        assert plase_order_City_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_City' не виден"
        print("Элемент с локатором 'locator_button_plase_order_City' виден")

        # Проверка, что элемент с локатором locator_button_plase_order_Creditcard виден
        plase_order_Creditcard_element = page.locator(locators["locator_button_plase_order_Creditcard"])
        assert plase_order_Creditcard_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_Creditcard' не виден"
        print("Элемент с локатором 'locator_button_plase_order_Creditcard' виден")

        # Проверка, что элемент с локатором locator_button_plase_order_Month виден
        plase_order_Month_element = page.locator(locators["locator_button_plase_order_Month"])
        assert plase_order_Month_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_Month' не виден"
        print("Элемент с локатором 'locator_button_plase_order_Month' виден")

        # Проверка, что элемент с локатором locator_button_plase_order_Year виден
        plase_order_Year_element = page.locator(locators["locator_button_plase_order_Year"])
        assert plase_order_Year_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_Year' не виден"
        print("Элемент с локатором 'locator_button_plase_order_Year' виден")

        plase_order_purchase_button_element = page.locator(locators["locator_button_plase_order_purchase"])
        assert plase_order_purchase_button_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_purchase' не виден"
        print("Элемент с локатором 'locator_button_plase_order_purchase' виден")

        # Проверка, что элемент с локатором locator_button_plase_order_close виден
        plase_order_close_button_element = page.locator(locators["locator_button_plase_order_close"])
        assert plase_order_close_button_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_close' не виден"
        print("Элемент с локатором 'locator_button_plase_order_close' виден")

        browser.close()


def test_demoblaze_brausers(page): #запуск теста на различных браузерах с неверными данными для ордера
    page.goto("https://www.demoblaze.com/cart.html")

    # Проверка, что элемент с локатором locator_button_plase_order виден
    plase_order_button_element = page.locator(locators["locator_button_plase_order"])
    assert plase_order_button_element.is_visible(), "Элемент с локатором 'locator_button_plase_order' не виден"
    print("Элемент с локатором 'locator_button_plase_order' виден")

    # Клик по кнопке "Place Order" для открытия модального окна оформления заказа
    page.click(locators["locator_button_plase_order"])
    page.wait_for_selector(locators["locator_modal_plase_order"])  # Ожидание открытия модального окна

    # Проверка, что модальное окно plase_order видно
    plase_order_modal_element = page.locator(locators["locator_modal_plase_order"])
    assert plase_order_modal_element.is_visible(), "Модальное окно 'plase_order' не видно"
    print("Модальное окно 'plase_order' видно")

    # Проверка, что элемент с локатором locator_button_plase_order_purchase виден
    plase_order_purchase_button_element = page.locator(locators["locator_button_plase_order_purchase"])
    assert plase_order_purchase_button_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_purchase' не виден"
    print("Элемент с локатором 'locator_button_plase_order_purchase' виден")

    # Заполнение формы оформления заказа на неверных данных
    page.fill(locators["locator_button_plase_order_name"], "3;№")
    page.fill(locators["locator_button_plase_order_country"], "?Г*Ш(Щ")
    page.fill(locators["locator_button_plase_order_City"], "ё4=90")
    page.fill(locators["locator_button_plase_order_Creditcard"], "Хх,45ву@#@#,,,.")
    page.fill(locators["locator_button_plase_order_Month"], "111111111111111111111111111111111111111111111")
    page.fill(locators["locator_button_plase_order_Year"], "класс")

    # Клик по кнопке "Purchase" для подтверждения заказа
    page.click(locators["locator_button_plase_order_purchase"])
    page.wait_for_selector(locators["locator_button_plase_order_ok"])  # Ожидание открытия модального окна подтверждения

    # Проверка, что элемент с локатором locator_button_plase_order_ok виден
    plase_order_ok_button_element = page.locator(locators["locator_button_plase_order_ok"])
    assert plase_order_ok_button_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_ok' не виден"
    print("Элемент с локатором 'locator_button_plase_order_ok' виден")

    # Проверка, что элемент с локатором locator_button_plase_order_close виден
    plase_order_close_button_element = page.locator(locators["locator_button_plase_order_close"])
    assert plase_order_close_button_element.is_visible(), "Элемент с локатором 'locator_button_plase_order_close' не виден"
    print("Элемент с локатором 'locator_button_plase_order_close' виден")