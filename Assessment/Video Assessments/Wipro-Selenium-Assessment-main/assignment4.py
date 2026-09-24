"""
Assignment 4: Child Nodes Using CSS
Locate and interact with a nested (child) web element using
a CSS child selector.
"""

import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- Setup ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
file_url = Path("demo_page.html").resolve().as_uri()
driver.get(file_url)
driver.maximize_window()
time.sleep(1)

# CSS child selector: selects the <button> that is a direct child of #profile-card
view_profile_btn = driver.find_element(By.CSS_SELECTOR, "#profile-card > button")

print(f"Button located inside div using CSS child selector: '{view_profile_btn.text}'")
view_profile_btn.click()
print("Button clicked successfully.")

time.sleep(2)
driver.quit()