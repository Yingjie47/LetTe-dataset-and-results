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
driver.find_element(By.XPATH, '//*[@id="contentwrapper"]/div[1]/ul/li[3]/a').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[2]/table/tbody[1]/tr[1]/td[4]/a').click()
sleep(1)
driver.switch_to.alert.accept()
driver.switch_to.default_content()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="mainmenue"]/li[4]/a').click()
driver.close()
driver.quit()