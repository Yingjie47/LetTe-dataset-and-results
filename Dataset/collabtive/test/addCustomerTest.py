from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/collabtive-3.0/")
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="loginform"]/fieldset/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="loginform"]/fieldset/div[4]/button').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="mainmenue"]/li[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="contentwrapper"]/div[1]/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="add_butn_customers"]').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="company"]').send_keys("test company")
driver.find_element(By.XPATH, '//*[@id="contact"]').send_keys("test contact")
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("testEmail@gmail.com")
driver.find_element(By.XPATH, '//*[@id="tel1"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[@id="tel2"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[@id="web"]').send_keys("https://test.com")
driver.find_element(By.XPATH, '//*[@id="address"]').send_keys("test")
driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("test")
driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("China")
driver.find_element(By.XPATH, '//*[@id="state"]').send_keys("active")
driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/div/form/fieldset/div[14]/div/span[3]/table/tbody/tr[2]/td/iframe'))
driver.find_element(By.XPATH, '/html/body').send_keys("test")
driver.switch_to.default_content()
driver.find_element(By.XPATH, '//*[@id="form_addcustomer"]/div/form/fieldset/div[16]/button[1]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="mainmenue"]/li[4]/a').click()
driver.close()
driver.quit()