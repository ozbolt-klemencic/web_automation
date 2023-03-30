import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome driver
os.environ['PATH'] += "path to drivers"
driver = webdriver.Chrome()

# Navigate to the Instagram login page and wait for the page to load
driver.get('https://www.instagram.com/accounts/login/')

#wait for elements to load
driver.implicitly_wait(5)

# Click the "Allow cookies" button, if it exists
try:
    cookies = driver.find_element(By.CSS_SELECTOR,'button._a9--._a9_0').click()

except:
    print("No cookies button found")

# Enter the username and password into the appropriate input fields on the login form
username = "your_username"
password = "your_password"
username_element = driver.find_element(By.NAME, 'username').send_keys(username)
password_element = driver.find_element(By.NAME, 'password').send_keys(password)

# Click the "Log in" button to submit the form
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()

# keeps the browser open
while True:
    time.sleep(1)

# if you want to close browser use this command instead
driver.quit()
