from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.python.org")

    title_before_refresh = driver.title
    print("Title before refresh:", title_before_refresh)

    driver.refresh()

    title_after_refresh = driver.title
    print("Title after refresh:", title_after_refresh)

    if title_before_refresh == title_after_refresh:
        print("Verification: The page title remained the same.")
    else:
        print("Verification: The page title changed.")

finally:
    driver.quit()
