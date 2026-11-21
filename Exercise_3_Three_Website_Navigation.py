from selenium import webdriver
import time

driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Open Wikipedia
driver.get("https://www.wikipedia.org")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Open Python
driver.get("https://www.python.org")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Go Back twice
driver.back()
time.sleep(2)

driver.back()
print("After Back:", driver.title)
time.sleep(2)

# Go Forward once
driver.forward()
print("After Forward:", driver.title)
time.sleep(2)

# Close browser
driver.quit()