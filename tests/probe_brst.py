from selenium import webdriver

BROWSERSTACK_URL = 'https://maxpopkov1:zgn8XW7s9ZxpknssmYyY@hub-cloud.browserstack.com/wd/hub'

desired_cap = {

    'os': 'Windows',
    'os_version': '10',
    'browser': 'Firefox',
    'browser_version': '70',
    'name': "Max's First Test"

}

driver = webdriver.Remote(
    command_executor=BROWSERSTACK_URL,
    desired_capabilities=desired_cap
)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()