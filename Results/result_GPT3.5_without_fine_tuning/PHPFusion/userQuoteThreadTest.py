from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/PHPFusion-9.10.30/")
driver.find_element(By.XPATH, '(//*[@name="user_name"])[2]').send_keys("admin")
driver.find_element(By.XPATH, '(//*[@name="user_pass"])[2]').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="login"]').click()
# sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr/td[2]/a[1]').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[3]/div[1]/div[2]/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="post_message-field"]/label').click()  # Updated XPath
driver.find_element(By.XPATH, '//*[@id="post_message"]').send_keys("test")
driver.find_element(By.XPATH, '//*[@id="post_reply"]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="user-menu"]').click()
driver.find_element(By.XPATH, '//*[@id="user-info"]/ul/li[7]/a').click()
driver.close()
driver.quit()