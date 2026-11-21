from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    driver.get("https://www.wikipedia.org")
    driver.get("https://www.python.org")

    driver.back()
    driver.back()
    print("Title after going Back twice:", driver.title)

    driver.forward()
    print("Title after going Forward once:", driver.title)

finally:
    driver.quit()
