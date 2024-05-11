from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_user_should_see_add_to_the_basket_button_on_the_page(browser):
    browser.get(link)
    add_to_the_basket_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert add_to_the_basket_button, "There is no add_to_the_basket_button on the page"
