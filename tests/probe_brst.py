from selenium import webdriver

capabilities = {
    "browserName": "firefox",
    "version": "79.0",
    "enableVNC": True,
    "enableVideo": False
}

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    desired_capabilities=capabilities
)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()