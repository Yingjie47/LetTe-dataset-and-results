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
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/a[1]').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div/form/fieldset/div[4]/input').send_keys("789")
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div/form/fieldset/div[5]/input').send_keys("789")
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div/form/fieldset/div[9]/input').clear()
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div/form/fieldset/div[9]/input').send_keys("100000")
driver.find_element(By.XPATH, '//*[@id="form_editcustomer"]/div/form/fieldset/div[15]/button[1]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="mainmenue"]/li[4]/a').click()
driver.close()
driver.quit()