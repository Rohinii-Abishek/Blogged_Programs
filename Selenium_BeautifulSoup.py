from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import Counter
import re
from bs4 import BeautifulSoup
# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Find all <a> elements on the webpage
input_field = driver.find_element(By.NAME,'q') 
text_to_type = "oswald"  
input_field.send_keys(text_to_type)

input_field.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='search']")))

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

page_text = soup.get_text()
# page_text = driver.find_element(By.TAG_NAME,'body').text

driver.quit()

words = re.findall(r'\b\w+\b', page_text.lower())
word_count = Counter(words)[text_to_type]
print(f"The text '{text_to_type}' appears {word_count} times on the webpage.")