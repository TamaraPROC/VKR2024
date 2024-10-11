from playwright.sync_api import Page
from test_dbp_steps import *

def test_demoblaze_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")
        page.click(locator_button_login)# Клик по кнопке "Log in"
        page.wait_for_selector(locator_modal_login)# Ожидание открытия модального окна
        assert page.query_selector(locator_modal_login) is not None # Проверка, что модальное окно открыто
        page.screenshot(path='screenshots/login.jpeg')# Скриншот модального окна
        page.fill(locator_field_user_name, data_username)# Ввод логина и пароля
        page.fill(locator_field_user_pass, data_password)
        page.click(locator_field_user_name)# Клик по кнопке "Log in" внутри модального окна
        page.wait_for_timeout(3000)# Ожидание закрытия модального окна
        page.screenshot(path='screenshots/login1.jpeg')# Скриншот после логина
        browser.close()

def test_demoblaze_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")
        page.click(locator_button_login)# Клик по кнопке "Log in"
        page.wait_for_selector(locator_modal_login)# Ожидание открытия модального окна
        assert page.query_selector(locator_modal_login) is not None, "Модальное окно не открыто" # Проверка, что модальное окно открыто
        page.fill(locator_field_user_name, data_username)# Ввод логина и пароля
        page.fill(locator_field_user_pass, data_password)
        page.click("button[onclick='logIn()']")# Клик по кнопке "Log in" внутри модального окна
        page.wait_for_selector("#logout2")# Ожидание закрытия модального окна и успешного входа
        assert page.query_selector("#logout2") is not None, "Пользователь не вошел в систему"# Проверка, что пользователь вошел в систему
        page.screenshot(path='screenshots/logged_in.jpeg')# Скриншот после успешного входа
        page.click("a#logout2")# Клик по кнопке "Log out"
        page.wait_for_selector("#login2")# Ожидание закрытия сессии и появления кнопки "Log in"
        assert page.query_selector("#login2") is not None, "Пользователь не вышел из системы"# Проверка, что пользователь вышел из системы
        page.screenshot(path='screenshots/logout.jpeg')# Скриншот после выхода
        browser.close()

def test_demoblaze_cat_product():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")
        page.click("a#itemc[onclick='byCat(\\'phone\\')']")# Клик по категории "Phones"
        page.wait_for_selector(".card-title")# Ожидание загрузки продуктов в категории "Phones"
        assert page.query_selector_all(".card-title") is not None, "Продукты в категории 'Phones' не загружены"# Проверка, что продукты в категории "Phones" загружены
        page.screenshot(path='screenshots/phones_category.jpeg')# Скриншот страницы с продуктами в категории "Phones"
        page.click("a#itemc[onclick='byCat(\\'notebook\\')']")# Клик по категории "Laptops"
        page.wait_for_selector(".card-title")# Ожидание загрузки продуктов в категории "Laptops"
        assert page.query_selector_all(".card-title") is not None, "Продукты в категории 'Laptops' не загружены"# Проверка, что продукты в категории "Laptops" загружены
        page.screenshot(path='screenshots/laptops_category.jpeg')# Скриншот страницы с продуктами в категории "Laptops"
        page.click("a#itemc[onclick='byCat(\\'monitor\\')']")# Клик по категории "Monitors"
        page.wait_for_selector(".card-title")# Ожидание загрузки продуктов в категории "Monitors"
        assert page.query_selector_all(".card-title") is not None, "Продукты в категории 'Monitors' не загружены"# Проверка, что продукты в категории "Monitors" загружены
        page.screenshot(path='screenshots/monitors_category.jpeg')# Скриншот страницы с продуктами в категории "Monitors"
        browser.close()

def test_demoblaze_get_product():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")
        page.click("a#itemc[onclick='byCat(\\'phone\\')']")# Клик по категории "Phones"
        page.wait_for_selector(".card-title")# Ожидание загрузки продуктов в категории "Phones"
        assert page.query_selector_all(".card-title") is not None, "Продукты в категории 'Phones' не загружены"# Проверка, что продукты в категории "Phones" загружены
        product_link = page.query_selector("div.card-block a")# Выбор первого продукта в категории "Phones"
        product_name = product_link.text_content()
        product_link.click()
        page.wait_for_selector("#tbodyid h2")# Ожидание загрузки страницы продукта
        assert page.query_selector("#tbodyid h2").text_content() == product_name, "Неверный продукт открыт"# Проверка, что открыта страница выбранного продукта
        page.screenshot(path='screenshots/product_page.jpeg')# Скриншот страницы выбранного продукта
        browser.close()

def test_demoblaze_purchase():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")
        page.click("a#itemc[onclick='byCat(\\'phone\\')']")# Клик по категории "Phones"
        page.wait_for_selector(".card-title")# Ожидание загрузки продуктов в категории "Phones"
        assert page.query_selector_all(".card-title") is not None, "Продукты в категории 'Phones' не загружены"# Проверка, что продукты в категории "Phones" загружены
        product_link = page.query_selector("div.card-block a")# Выбор первого продукта в категории "Phones"
        product_name = product_link.text_content()
        product_link.click()
        page.wait_for_selector("#tbodyid h2")# Ожидание загрузки страницы продукта
        assert page.query_selector("#tbodyid h2").text_content() == product_name, "Неверный продукт открыт"# Проверка, что открыта страница выбранного продукта
        page.screenshot(path='screenshots/product_page.jpeg')# Скриншот страницы выбранного продукта
        page.click("a#cartur")# Добавление продукта в корзину
        page.wait_for_selector("#page-wrapper")# Ожидание загрузки страницы корзины
        assert page.query_selector("#page-wrapper") is not None, "Продукт не добавлен в корзину"# Проверка, что продукт добавлен в корзину
        page.screenshot(path='screenshots/cart_page.jpeg')# Скриншот страницы корзины
        page.click(locator_button_plase_order)# Клик по кнопке "Place Order"
        page.wait_for_selector("#orderModal")# Ожидание открытия модального окна оформления заказа
        assert page.query_selector("#orderModal") is not None, "Модальное окно оформления заказа не открыто"# Проверка, что модальное окно оформления заказа открыто
        page.fill("#name", "ДРУГ ДРУЖИЩЕ")
        page.fill("#country", "Росси")
        page.fill("#city", "Новосибирск")
        page.fill("#card", "12345678987654432")
        page.fill("#month", "02")
        page.fill("#year", "26")
        page.screenshot(path='screenshots/order_modal.jpeg')# Скриншот модального окна оформления заказа
        page.click(locator_button_plase_order_purchase)# Клик по кнопке "Purchase"
        page.wait_for_selector("#orderModal")# Ожидание загрузки страницы подтверждения заказа
        assert page.query_selector("#orderModal") is not None, "Заказ не оформлен"# Проверка, что заказ успешно оформлен
        page.screenshot(path='screenshots/order_confirmation.jpeg')# Скриншот страницы подтверждения заказа
        browser.close()

def test_demoblaze_login_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)  # Открываем браузер с интерфейсом и замедляем выполнение
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")

        # Авторизация
        page.click(locator_button_login)  # Клик по кнопке "Log in"
        page.wait_for_selector(locator_button_login_modal)  # Ожидание открытия модального окна
        assert page.query_selector(locator_button_login_modal) is not None  # Проверка, что модальное окно открыто
        page.screenshot(path='screenshots/login.jpeg')  # Скриншот модального окна
        page.fill(locator_field_user_name, data_username)  # Ввод логина и пароля
        page.fill(locator_field_user_pass, data_password)
        page.click(locator_button_login_modal)  # Клик по кнопке "Log in" внутри модального окна
        page.wait_for_timeout(3000)  # Ожидание закрытия модального окна
        page.screenshot(path='screenshots/login1.jpeg')  # Скриншот после логина

        # Выбор товара
        page.click(locator_cat_phones)  # Выбор категории "Phones"
        page.click(locator_cat_phones_product_2)  # Выбор второго товара в списке
        page.click(locator_button_Add_to_cart)  # Клик по кнопке "Add to cart"
        page.wait_for_timeout(2000)  # Ожидание добавления товара в корзину
        page.screenshot(path='screenshots/product_page.jpeg')  # Скриншот страницы выбранного продукта
        # Переход в корзину
        page.click(locator_shopping_cart)  # Переход в корзину
        page.wait_for_timeout(2000)  # Ожидание загрузки корзины

        # Оформление заказа
        page.click(locator_button_plase_order)  # Клик по кнопке "Place Order"
        page.wait_for_selector(locator_button_plase_order_name)  # Ожидание открытия модального окна оформления заказа
        page.fill(locator_button_plase_order_name, data_name)  # Заполнение данных для оплаты
        page.fill(locator_button_plase_order_country, data_Country)
        page.fill(locator_button_plase_order_City, data_City)
        page.fill(locator_button_plase_order_Creditcard, data_Creditcard)
        page.fill(locator_button_plase_order_Month, data_Month)
        page.fill(locator_button_plase_order_Year, data_Year)
        page.click(locator_button_plase_order_purchase)  # Клик по кнопке "Purchase"
        page.wait_for_selector(locator_button_plase_order_ok)  # Ожидание модального окна подтверждения
        page.click(locator_button_plase_order_ok)  # Клик по кнопке "OK"
        page.wait_for_timeout(2000)  # Ожидание закрытия модального окна

        # Выход из аккаунта
        page.click(locator_button_logout)  # Клик по кнопке "Log out"
        page.wait_for_timeout(2000)  # Ожидание выхода из аккаунта

        browser.close()



def test_demoblaze_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.demoblaze.com/index.html")

        # Проверка локатора для кнопки "Log in"
        result = page.evaluate("document.querySelector('#login2') !== null")
        assert result, "Кнопка 'Log in' не найдена"

        browser.close()