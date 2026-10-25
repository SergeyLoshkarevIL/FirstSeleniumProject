from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://telranedu.web.app/login"
def test_login():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)
        element = driver.find_element(By.NAME, value: 'email')
        assert element.is_displayer()

    finally:
        driver.quit()