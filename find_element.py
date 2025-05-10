from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Set up the browser
driver = webdriver.Chrome()


driver.get("https://www.amazon.in/s?k=phone&crid=358V2TMIFQA8S&sprefix=phon%2Caps%2C307&ref=nb_sb_noss_2")

print(driver.title)


find_element = driver.find_element(By.CLASS_NAME,"puis-card-container")
print(find_element.text)

time.sleep(5)

driver.quit()
