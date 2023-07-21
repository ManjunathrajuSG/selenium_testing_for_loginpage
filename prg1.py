import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Lab\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://bmsitm.gnums.in/Login.aspx")
driver.find_element(By.NAME,"txtUsername").send_keys("7676719005")
driver.find_element(By.NAME,"txtPassword").send_keys("SGMD@1234")
driver.find_element(By.ID,"btnLogin").click()

act_title=driver.title
exp_title="BMS Institute of Technology & Management"

if act_title==exp_title:
    print("test passed")
else:
    print("test failed")

time.sleep(60)

