from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Set up the browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.python.org/")

print(driver.title)

# Search for something
search_box = driver.find_element(By.NAME, "q") # the search input field has name="q".
search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
