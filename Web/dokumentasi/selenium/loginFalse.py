from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://localhost/bigproject_web/")
driver.find_element_by_name("email").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")

driver.find_element_by_id("submit").click()