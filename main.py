from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = "https://www.google.com/search?q=hello+world"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage") # must - fix: unknown error: DevToolsActivePort file doesn't exist
options.add_argument("--disable-popup-blocking")
options.add_argument("--remote-debugging-port=9222")  # this
options.binary_location = "usr/bin/google-chrome"

#try:
#    s = Service(ChromeDriverManager().install())
#    driver = webdriver.Chrome(options=options, service=s)
#    driver.get(url)
#    html = driver.page_source
#    print(html)
#except:
#    try:
#        print('try another way')
#        driver = webdriver.Chrome('chromedriver_linux64/chromedriver', options=options)
#    except:
#        try:
#            print('try another another way')
#            driver = webdriver.Chrome('usr/bin/chromium', options=options)
#        except:
#            print('try another another another way')
#            driver = webdriver.Chrome('usr/bin/chromedriver', options=options)

#try:
#    driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
#    driver.get(url)
#except:
#    s = Service(ChromeDriverManager().install())
#    driver = webdriver.Chrome(options=options, service=s)
#    driver.get(url)


driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
driver.get(url)
print(driver.page_source())

driver.get(url)

driver.close()
