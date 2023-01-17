from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.google.com/search?q=hello+world"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-dev-shm-usage") # must - fix: unknown error: DevToolsActivePort file doesn't exist
# options.add_argument("--remote-debugging-port=9222")  # this


# s = Service(ChromeDriverManager().install())
# skip service=s

try:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=s)
    driver.get(url)
    html = driver.page_source
    print(html)
except:
    try:    
        print('try another way')
        driver = webdriver.Chrome('chromedriver_linux64/chromedriver', options=options)
    except:
        print('try another another way')
        driver = webdriver.Chrome('usr/bin/chromium', options=options)

driver.close()
