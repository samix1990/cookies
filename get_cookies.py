from selenium import webdriver
import pickle
import time

###build and download cookies, once you download the cookies, no need to run in the future for the website
driver = webdriver.Chrome()
driver.get("https://members.helium10.com/user/signin")
time.sleep(50)##use this time to log in the website manually, input your username and passward
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb")) ###download the cookies, and save it in files


###use in cralwer data every time need input user name and passwards
