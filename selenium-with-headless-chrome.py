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
print("page title: %s" % driver.title)

def Login():
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

# login page
Login()

driver.save_screenshot('screenshot.png')
