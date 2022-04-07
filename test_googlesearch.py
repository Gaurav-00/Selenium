import time


from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Harman")  #to searh a  word in google
time.sleep(5)   #time is given to hold for 5 sec
driver.close()
print("testcase successfully completed")





