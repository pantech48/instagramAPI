import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import Config


def get_instagram_photos(username: str, password: str, target_username: str, max_count: int):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # run in headless mode
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options)
    instagram_login(password, username, driver)

    # Go to the target user's page
    driver.get(f"http://www.instagram.com/{target_username}")

    # Get the photos
    image_elements = WebDriverWait(driver, 10).until(
        lambda d: d.find_elements(By.CSS_SELECTOR, "article img")[:max_count])
    image_urls = [img.get_attribute("src") for img in image_elements]

    driver.quit()

    return image_urls


def instagram_login(password: str, username: str, driver: webdriver.Chrome) -> None:
    # Instagram login page
    driver.get("http://www.instagram.com")
    # Accept cookies
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Allow all cookies")]'))).click()
    except TimeoutException:
        print("Cookies button not found")
        pass
    time.sleep(2)
    # Fill the username and password fields
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username_field.clear()
    username_field.send_keys(username)
    password_field.clear()
    password_field.send_keys(password)
    # Click the login button
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    # Skip the "Save Your Login Info?" and "Turn on Notifications" prompts
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()







