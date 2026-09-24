"""
Assignment 1: Web Element Identification
Locate different web elements using By.ID, By.NAME, By.TAG_NAME,
By.LINK_TEXT, and By.CLASS_NAME.
"""

import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
file_url = Path("demo_page.html").resolve().as_uri()
driver.get(file_url)
driver.maximize_window()
time.sleep(1)

# 1. Locate username field by ID
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("ahana_dev")
print("Username field located by ID and text entered.")

# 2. Locate password field by NAME
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("mypassword123")
print("Password field located by NAME and text entered.")

# 3. Locate the page heading by TAG_NAME
heading = driver.find_element(By.TAG_NAME, "h1")
print(f"Heading located by TAG_NAME: '{heading.text}'")

# 4. Locate the 'Forgot Password?' link by LINK_TEXT
forgot_link = driver.find_element(By.LINK_TEXT, "Forgot Password?")
print(f"Link located by LINK_TEXT: '{forgot_link.text}'")

# 5. Locate the login button by CLASS_NAME
login_btn = driver.find_element(By.CLASS_NAME, "login-btn")
print(f"Button located by CLASS_NAME: '{login_btn.text}'")

time.sleep(2)
driver.quit()