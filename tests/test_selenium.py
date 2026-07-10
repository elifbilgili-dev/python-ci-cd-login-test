
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_demo_login_form():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")
        login_button.click()

        header_text = driver.find_element(By.TAG_NAME, "h2").text
        assert header_text == "Secure Area"

    finally:
        driver.quit()