from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/PHPFusion-9.03.90/")
driver.find_element(By.XPATH, '(//*[@name="user_name"])[2]').send_keys("admin")
driver.find_element(By.XPATH, '(//*[@name="user_pass"])[2]').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="login"]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="ddlink13"]').click()
driver.find_element(By.XPATH, '//*[@id="menu-13"]/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="s2id_forum_id"]/a').click()
driver.find_element(By.XPATH, '//*[@id="select2-results-1"]').click()
driver.find_element(By.XPATH, '//*[@id="thread_subject"]').send_keys("test")
driver.find_element(By.XPATH, '//*[@id="s2id_autogen2"]').click()
driver.find_element(By.XPATH, '//*[@id="select2-drop"]/ul').click()
driver.find_element(By.XPATH, '//*[@id="post_message"]').send_keys("test")
driver.find_element(By.XPATH, '//*[@id="post_message-field"]/div/div[1]/div/div/div/div/input').click()
driver.find_element(By.XPATH, '//*[@id="post_message-field"]/div/div[1]/div/div/div/div/div/img[5]').click()
driver.find_element(By.XPATH, '//*[@id="notify_me-field"]/label').click()
driver.find_element(By.XPATH, '//*[@id="post_newthread"]').click()
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="user-menu"]').click()
driver.find_element(By.XPATH, '//*[@id="user-info"]/ul/li[7]/a').click()
driver.close()
driver.quit()