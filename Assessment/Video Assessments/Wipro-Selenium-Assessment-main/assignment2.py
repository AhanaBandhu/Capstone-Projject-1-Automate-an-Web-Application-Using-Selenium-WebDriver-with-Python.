"""
Assignment 2: Multiple Element Identification
Find all links of the same type on a page and print their text.
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

# Find all elements with class "site-link"
links = driver.find_elements(By.CLASS_NAME, "site-link")

print(f"Found {len(links)} links on the page:\n")
for index, link in enumerate(links, start=1):
    print(f"{index}. {link.text}")

time.sleep(2)
driver.quit()