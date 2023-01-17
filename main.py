from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 800))
display.start()

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage") # must - fix: unknown error: DevToolsActivePort file doesn't exist
options.add_argument("--disable-popup-blocking")
options.add_argument("--remote-debugging-port=9222")
# options.add_argument(f"crash-dumps-dir={os.path.expanduser('~/tmp/Crashpad')}")
options.binary_location = "usr/bin/google-chrome"
# options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

url = "https://www.google.com"
driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
driver.get(url)
print(driver.page_source())

driver.get(url)

driver.close()
