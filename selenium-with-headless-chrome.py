import os
import time
import platform

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

now = datetime.now()
current_time = now.strftime("%H-%M-%S")

timeout = 10

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-remote-fonts")
chrome_options.add_argument("--lang=zh-TW")

screenshots_path = '/screenshots/'
if platform.system() == 'Windows':
  driver = webdriver.Chrome(r'chromedriver', chrome_options=chrome_options)
  screenshots_path = 'c:\\windows\\temp\\'
else:
  driver = webdriver.Chrome(r'/opt/chrome/chromedriver', chrome_options=chrome_options)

driver.fullscreen_window()
driver.get("https://asiaauth.mayohr.com/HRM/Account/Login")

def Login():
    print("%s | Login" % driver.title)

    # wait for page loading
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'loginform')))
    except TimeoutException:
        print("Timed out waiting for page to load")

    # debug purpose
    # html = driver.page_source
    # print(html)

    # form
    form = driver.find_element(By.CLASS_NAME, 'loginform')

    # input company code
    company_code_input = driver.find_element(By.NAME, 'companyCode')
    company_code_input.send_keys('TXOne')

    # input employee no
    employee_no_input = driver.find_element(By.NAME, 'employeeNo')
    employee_no_input.send_keys(os.environ['EMPLOYEE_NO'])

    # input password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(os.environ['PSWD'])

    # debug purpose
    if not driver.save_screenshot('%s%s-Login.png' % (screenshots_path, current_time)):
        print('save Login failed')

    # submit form
    form.submit()

def WantClockInOut1stLevel():
    print("%s | WantClockInOut1stLevel" % driver.title)

    # wait for page loading
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'link-item__title')))
    except TimeoutException:
        print("Timed out waiting for page to load")

    # debug purpose
    if not driver.save_screenshot('%s%s-WantClockInOut1stLevel.png' % (screenshots_path, current_time)):
        print('save WantClockInOut1stLevel failed')

    # link items
    try:
        link_item = driver.find_element(By.LINK_TEXT, '我要打卡')
    except:
        # fall back to English
        link_item = driver.find_element(By.LINK_TEXT, 'Check in/out')
    link_item.click()

def WantClockInOut2ndLevel():
    print("%s | WantClockInOut2ndLevel" % driver.title)

    # wait for page loading
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'ta_btn_cancel')))
    except TimeoutException:
        print("Timed out waiting for page to load")

    # debug purpose
    if not driver.save_screenshot('%s%s-WantClockInOut2ndLevel.png' % (screenshots_path, current_time)):
        print('save WantClockInOut2ndLevel failed')

    link_items = driver.find_elements(By.CLASS_NAME, 'ta_btn_cancel')
    for link_item in link_items:
        if link_item.text not in ['休息開始', 'break end']:
            print("你已經點擊 [ %s ]" % link_item.text)
            link_item.click()

    # check if need to overwrite clock out record
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'win-box-button-bar')))
    except TimeoutException:
        print("Timed out, no need to overwrite clock out record")
        return

    btn_item = driver.find_element(By.CSS_SELECTOR, "button[class='ta_btn new__btn--fixed-height']")
    btn_item.click()

def SaveResult():
    print("%s | SaveResult" % driver.title)

    # wait for page loading
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'new-window-title')))
    except TimeoutException:
        print("Timed out waiting for page to load")

    time.sleep(timeout)
    if not driver.save_screenshot('%s%s-Result.png' % (screenshots_path, current_time)):
        print('save Result failed')

# login page
Login()
# want to clock in/out
WantClockInOut1stLevel()
WantClockInOut2ndLevel()
# save result
SaveResult()

# terminate driver session and close all windows
driver.quit()
