from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/PHPFusion-9.03.90/")
driver.find_element(By.XPATH, '(//*[@name="user_name"])[2]').send_keys("admin")
driver.find_element(By.XPATH, '(//*[@name="user_pass"])[2]').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="login"]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="navigation-user"]/ul/li[5]/a').click()
driver.find_element(By.XPATH, '//*[@id="admin_password"]').send_keys("root1234")
driver.find_element(By.XPATH, '//*[@id="admin-login-form"]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="adl"]/li[2]/a').click()
sleep(1)
driver.find_element(By.XPATH, '//a[contains(text()," News")]').click()
driver.find_element(By.XPATH, '//*[@id="news_admin"]/li[2]/a').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div/form/div/table/tbody/tr[16]/td[7]/div/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="news_cat_name"]').send_keys("123")
driver.find_element(By.XPATH, '//*[@id="news_cat_draft-field"]/label').click()
driver.find_element(By.XPATH, '//*[@id="news_cat_sticky-field"]/label').click()
driver.find_element(By.XPATH, '//*[@id="s2"]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="dduser"]').click()
driver.find_element(By.XPATH, '(//a[contains(text(),"Logout")])[2]').click()
driver.close()
driver.quit()