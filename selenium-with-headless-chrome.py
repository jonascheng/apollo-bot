import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 5

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

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

    # submit form
    form.submit()

def WantClockInOut1stLevel():
    print("%s | WantClockInOut1stLevel" % driver.title)

    # wait for page loading
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'link-item__title')))
    except TimeoutException:
        print("Timed out waiting for page to load")

    # link items
    link_item = driver.find_element(By.LINK_TEXT, '我要打卡')
    link_item.click()

def WantClockInOut2ndLevel():
    print("%s | WantClockInOut2ndLevel" % driver.title)

    # wait for page loading
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'ta_btn_cancel')))
    except TimeoutException:
        print("Timed out waiting for page to load")

    # link_items = driver.find_elements(By.CLASS_NAME, 'ta-link-name')
    # for link_item in link_items:
    #     if link_item.text == '我要打卡':
    #         print(link_item.text)
    #         link_item.click()

    link_items = driver.find_elements(By.CLASS_NAME, 'ta_btn_cancel')
    for link_item in link_items:
        if link_item.text != '休息開始':
            print("你已經 %s 了" % link_item.text)
            link_item.click()

# login page
Login()
# want to clock in/out
WantClockInOut1stLevel()
WantClockInOut2ndLevel()

driver.save_screenshot('screenshot.png')
