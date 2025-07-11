from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)

    button_add = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]"))
    )

    select = Select(browser.find_element(By.XPATH, "//select[contains(@name, 'language')]"))
    print(f"\nВыбранное значение языка на странице: {select.first_selected_option.text}")

    assert button_add, "Кнопка добавления в корзину не отображается"