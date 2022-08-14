from selenium import webdriver
import pickle
import time
driver = webdriver.Chrome()
driver.get('https://members.helium10.com/user/signin')  #load websites
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)   #load cookies, it can automatically login, similar to remember user and user passward
driver.get('https://members.helium10.com/user/signin')