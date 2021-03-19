from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ['ENV_EMAIL']
PW = os.environ['ENV_PW']

#establish chrome webdriver, navigate to tinder
driver = webdriver.Chrome(executable_path=r'C:\Users\josep\dev\chromedriver')

driver.get('https:/tinder.com')

login_button = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

# establish landing page handle such that you can travel to and fro
main_handle = driver.current_window_handle

# sleep commands allow selenium to catch up--without them it may struggle to locate elements
time.sleep(5)

# choose login option
with_google_button = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
with_google_button.click()

# alternatively, make driver wait until clickable?
time.sleep(5)

# now that there is a pop-up, log all windows
current_handles = driver.window_handles

for handle in current_handles:
    if handle != main_handle:
        # switch to login pop-up
        driver.switch_to.window(handle)
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(EMAIL)
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(PW)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(Keys.RETURN)



