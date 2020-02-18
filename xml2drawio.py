from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.draw.io")

element = driver.find_element_by_xpath("/html/body/div[14]/div/div[3]/div/a[3]").click()

element = driver.find_element_by_xpath("/html/body/div[14]/div/div[2]/button[1]").click()

element = driver.find_element_by_xpath("/html/body/div[15]/div/div[4]/button[4]").click()

element = driver.find_element_by_xpath("/html/body/div[3]/div[1]/a[5]").click()

element = driver.find_element_by_xpath("/html/body/div[14]/table/tbody/tr[13]/td[2]").click()

element = driver.find_element_by_xpath("/html/body/div[15]/div/textarea").click()

element = driver.find_element_by_xpath("/html/body/div[15]/div/textarea").clear()

element = driver.find_element_by_xpath("/html/body/div[15]/div/textarea").send_keys(Keys.CONTROL+"V")

element = driver.find_element_by_xpath("/html/body/div[15]/div/button[2]").click()
