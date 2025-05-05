# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.common.keys import Keys
import time
# Pull request

# define url
url1 = "https://google.com"
url2 = "file:///Users/michaelnauman/git/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html"
url3 = "http://python.org"

my_urls = [url1, url2, url3]


# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# load the webpage 
driver.get(my_urls[0])
# find the first name field 
first_name = driver.find_element(By.CLASS_NAME, "gb_X")
first_name.click()
time.sleep(2)
driver.close()


driver= webdriver.Firefox()
# load the webpage 
driver.get(my_urls[1])
# login_form = driver.find_element_by_id('loginForm')
test = driver.find_element(By.ID, "loginForm")
# test = driver.find_element('loginForm')
print("My login form element is:")
print(test)
time.sleep(2)
driver.close()


driver = webdriver.Firefox()
# load the webpage 
driver.get(my_urls[2])
search = driver.find_element(By.NAME, "q")
search.clear
search.send_keys("pycon")
search.send_keys(Keys.RETURN)
time.sleep(2)
driver.close()
