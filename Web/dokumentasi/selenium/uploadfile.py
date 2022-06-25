from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/bigproject_web/")
driver.find_element_by_name("email").send_keys("admin")
driver.find_element_by_name("password").send_keys("1234")

driver.find_element_by_id("submit").click()
driver.get("http://localhost/bigproject_web/images/tambah/")
driver.find_element_by_name("plat").send_keys("E:/1.jpg")
