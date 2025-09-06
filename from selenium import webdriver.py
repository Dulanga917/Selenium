from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    try:
        driver.get(URL)

        user_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        pwd_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        user_input.clear()
        user_input.send_keys(USERNAME)
        pwd_input.clear()
        pwd_input.send_keys(PASSWORD)

        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_btn.click()

        wait.until(EC.url_contains("/dashboard"))
        print("✅ Login successful on OrangeHRM demo site")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()