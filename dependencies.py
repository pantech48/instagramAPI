"""
This module contains functions to interact with Instagram using Selenium.
"""
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import Config


def get_instagram_photos(username: str, password: str, target_username: str, max_count: int) -> list:
    """
    Gets the URLs of the user's Instagram photos.

    Args:
        username (str): Instagram username to log in.
        password (str): Instagram password to log in.
        target_username (str): Instagram username to get photos of.
        max_count (int): Maximum number of photo URLs to return.

    Returns:
        list: A list of URLs of the user's Instagram photos.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')

    with webdriver.Chrome(options=options) as driver:
        instagram_login(password, username, driver)
        driver.get(f"{Config.INSTAGRAM_URL}{target_username}")

        image_elements = WebDriverWait(driver, 10).until(
            lambda d: d.find_elements(By.CSS_SELECTOR, "article img")[:max_count])

        image_urls = get_photo_urls(image_elements)

    return image_urls


def instagram_login(password: str, username: str, driver: webdriver.Chrome) -> None:
    """
    Logs in to Instagram.

    Args:
        password (str): Instagram password to log in.
        username (str): Instagram username to log in.
        driver (webdriver.Chrome): ChromeDriver instance.
    """
    driver.get(Config.INSTAGRAM_URL)

    find_and_click(driver, By.XPATH, '//button[contains(text(), "Allow all cookies")]', "Cookies button not found")

    find_and_send_keys(driver, By.CSS_SELECTOR, "input[name='username']", username)
    find_and_send_keys(driver, By.CSS_SELECTOR, "input[name='password']", password)

    find_and_click(driver, By.CSS_SELECTOR, "button[type='submit']")

    find_and_click(driver, By.XPATH, '//button[contains(text(), "Not Now")]', "Not Now button not found")


def find_and_click(driver: webdriver.Chrome, by: By, value: str, message: str = "") -> None:
    """
    Finds an element and clicks on it. Handles TimeoutException.

    Args:
        driver (webdriver.Chrome): ChromeDriver instance.
        by (By): Method to locate elements.
        value (str): The value of the CSS/XPath selector.
        message (str, optional): Message to print if TimeoutException is raised. Defaults to "".
    """
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((by, value))).click()
    except TimeoutException:
        if message:
            print(message)


def find_and_send_keys(driver: webdriver.Chrome, by: By, value: str, keys: str) -> None:
    """
    Finds an element and sends keys to it. Handles TimeoutException.

    Args:
        driver (webdriver.Chrome): ChromeDriver instance.
        by (By): Method to locate elements.
        value (str): The value of the CSS/XPath selector.
        keys (str): The keys to send.
    """
    try:
        field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        field.clear()
        field.send_keys(keys)
    except TimeoutException:
        print(f"Element with {by} = {value} not found.")


def get_photo_urls(image_elements: list) -> list:
    """
    Gets the URLs of the Instagram photos from the image elements.

    Args:
        image_elements (list): A list of image elements.

    Returns:
        list: A list of URLs of the Instagram photos.
    """
    return [img.get_attribute("src") for img in image_elements]




