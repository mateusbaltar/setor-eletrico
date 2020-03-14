from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def download_ipdo(driver):
    driver.get('ipdo_path')

def chrome_driver():
    CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    CHROMEDRIVER_PATH = 'C:/Users/Mateus Mendonca/Downloads/chromedriver.exe'
    WINDOW_SIZE = "1920,1080"

    options = Options()
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    options.binary_location = CHROME_PATH

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)  

    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    # driver = webdriver.Chrome(executable_path='C:/Users/mateus.mendonca/Downloads/chromedriver.exe', chrome_options=options)

    driver.get('https://sintegre.ons.org.br/')
    assert 'ONS' in driver.title

    elem = driver.find_element_by_name('username')
    elem.send_keys('mateus.mendonca')
    elem = driver.find_element_by_name('password')
    elem.send_keys('Energia2019')
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
    login_attempt.click()

    download_ipdo(driver)

    input('Aguarde...')

    driver.quit()


chrome_driver()