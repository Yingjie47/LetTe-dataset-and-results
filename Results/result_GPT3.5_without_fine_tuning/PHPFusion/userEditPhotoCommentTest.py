from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/PHPFusion-9.10.30/")
driver.find_element(By.XPATH, '(//*[@name="user_name"])[2]').send_keys("admin")
driver.find_element(By.XPATH, '(//*[@name="user_pass"])[2]').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="login"]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="main-menu_menu"]/ul[2]/li[6]/a').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[2]/a').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/a').click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/ul/li[1]/div[2]/div[3]/small/a[2]').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/div[2]/div/div/div[2]/textarea').send_keys("123")
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/input').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/img[10]').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/div[2]/button').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="user-menu"]').click()
driver.find_element(By.XPATH, '//*[@id="user-info"]/ul/li[7]/a').click()
driver.close()
driver.quit()