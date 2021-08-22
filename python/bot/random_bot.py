from selenium import webdriver as wd
import chromedriver_py
import random
import time

wd = wd.Chrome()
wd.implicitly_wait(10) 
wd.get("https://www.daraz.com.bd/")

search_bar = wd.find_element_by_xpath('//*[@id="q"]') 
search_bar.send_keys('microphone')
random_wait_time = random.randrange(10.0,15.0)

search_glass= wd.find_element_by_xpath('//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button')
search_glass.click()

random_wait_time = random.randrange(10.0,20.0)
fantech_mic = wd.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/a/img')
fantech_mic.click()

random_wait_time = random.randrange(8.0,10.0)
add_cart= wd.find_element_by_xpath('//*[@id="module_add_to_cart"]/div/button[2]')
add_cart.click()

#random_wait_time = random.randrange(10.0,11.0)
#phone_email = wd.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/form/div/div[1]/div[1]/input')
#phone_email.click()
#phone_email.send_keys('nabil') 

#random_wait_time = random.randrange(7.0,10.0)
#pass_forlogin= wd.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/form/div/div[1]/div[2]/input')
#pass_forlogin.click()
#pass_forlogin.send_keys('weed is real')

#random_wait_time = random.randrange(3.0,7.0)
#login= wd.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/form/div/div[2]/div[1]/button')
#login.click()