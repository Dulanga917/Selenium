from selenium import webdriver
from selenium.webdriver.common.by import By # pyright: ignore[reportMissingImports]
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()  # Selenium 4+ auto-manages drivers
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    try:
        driver.get("https://www.google.com")

        # Accept consent (if shown)
        try:
            consent_button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[@id='L2AGLb' or .//div[text()='I agree'] or "
                    ".//span[contains(., 'I agree') or contains(., 'Accept all')]]"
                ))
            )
            consent_button.click()
        except Exception:
            pass  # No consent dialog

        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)

        wait.until(EC.title_contains("Selenium WebDriver"))
        print("✅ Google search worked; page title:", driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
