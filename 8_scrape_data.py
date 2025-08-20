from selenium import webdriver
import time

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get('https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6')
    time.sleep(5)
    result = driver.find_element('xpath', '/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]').text
    print(f'The value is {result}')

getDriver()