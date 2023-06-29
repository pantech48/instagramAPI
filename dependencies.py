from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_instagram_photos(username: str, password: str, target_username: str, max_count: int):
    driver = webdriver.Chrome()

    # Instagram login page
    driver.get("http://www.instagram.com")

    # Fill the username and password fields
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username_field.clear()
    username_field.send_keys(username)
    password_field.clear()
    password_field.send_keys(password)

    # Click the login button
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # Skip the "Save Your Login Info?" and "Turn on Notifications" prompts
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

    # Go to the target user's page
    driver.get(f"http://www.instagram.com/{target_username}")

    # Get the photos
    image_elements = WebDriverWait(driver, 10).until(lambda d: d.find_elements(By.CSS_SELECTOR, "article img")[:max_count])
    image_urls = [img.get_attribute("src") for img in image_elements]

    driver.quit()

    return image_urls

