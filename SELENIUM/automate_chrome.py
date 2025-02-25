from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Use raw string for file path or double backslashes
service = Service(executable_path=r"C:\Users\91600\Documents\GitHub\SQL\Python_streak\SELENIUM\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

#This should work as expected now, opening Google, searching for "Today's weather," and then waiting 20 seconds before closing the browser.
search_element = driver.find_element(By.CLASS_NAME,"gLFyf")
search_element.clear()
search_element.send_keys("Todays's weather",Keys.ENTER)

time.sleep(20)

driver.quit()
