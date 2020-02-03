from selenium import webdriver
from time import sleep

user_name = ''
password = ''


chromedriver_path = './chromedriver'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username_field = webdriver.find_element_by_name('username')
username_field.send_keys(user_name)
password_field = webdriver.find_element_by_name('password')
password_field.send_keys(password)

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector(
    'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm'
)
notnow.click()