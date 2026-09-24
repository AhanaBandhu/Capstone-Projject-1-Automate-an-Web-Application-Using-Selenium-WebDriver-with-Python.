"""
Assignment 3: CSS Selector Challenge
Locate elements using CSS Selectors, including wildcard selectors
for elements with dynamic attribute values.
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

# CSS wildcard selector: matches any element whose id STARTS WITH "user_"
user_cards = driver.find_elements(By.CSS_SELECTOR, "[id^='user_']")

print(f"Found {len(user_cards)} user profile elements using wildcard selector:\n")
for card in user_cards:
    print(f"ID: {card.get_attribute('id')}  ->  Text: {card.text}")

time.sleep(2)
driver.quit()