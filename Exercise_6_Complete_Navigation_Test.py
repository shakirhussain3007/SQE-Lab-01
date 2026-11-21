from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    driver.get("https://www.google.com")
    print("First website title:", driver.title)
    print("First website URL:", driver.current_url)

    driver.get("https://www.wikipedia.org")
    print("\\nSecond website title:", driver.title)
    print("Second website URL:", driver.current_url)

    driver.back()
    print("\\nTitle after Back:", driver.title)

    driver.forward()
    print("Title after Forward:", driver.title)

    driver.refresh()
    print("Title after Refresh:", driver.title)

finally:
    driver.quit()
