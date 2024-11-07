from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/mantisbt-2.26.0/")
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("administrator")
driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/input[2]').click()
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/input[3]').click()
# sleep(1)
driver.find_element(By.LINK_TEXT, '管理').click()
driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/ul/li[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="subprojects"]//button[contains(text(),"新建子项目")]').click()
driver.find_element(By.XPATH, '//*[@id="project-name"]').send_keys("test")
driver.find_element(By.XPATH, '//*[@id="project-description"]').send_keys("test")
driver.find_element(By.XPATH, '//*[@id="manage-project-create-form"]/div/div[3]/input').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="navbar-container"]/div[2]/ul/li[3]/ul/li[4]/a').click()
driver.close()
driver.quit()