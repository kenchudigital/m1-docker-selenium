# here is readme

(command: google-chrome --version)
Chrome version: Google Chrome 109.0.5414.74 
Path: usr/bin/google-chrome

According to Chrome version download the chromedriver
LINK: https://chromedriver.chromium.org/downloads

If you are using Chrome version 109, please download ChromeDriver 109.0.5414.74
https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/

download this:-> chromedriver_linux64.zip
unzip localy

Python code:
```python
# not display
options.add_argument("--disable-gpu")
options.add_argument("--headless")

# fix DevToolsActivePort file doesn't exist
options.add_argument("--disable-dev-shm-usage") 
options.add_argument("--remote-debugging-port=9222")

# set chrome location
options.binary_location = "usr/bin/google-chrome"
driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
```

Error:
```bash
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
//main.py:43: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
Traceback (most recent call last):
  File "//main.py", line 43, in <module>
    driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
  File "/usr/local/lib/python3.10/site-packages/selenium/webdriver/chrome/webdriver.py", line 69, in __init__
    super().__init__(DesiredCapabilities.CHROME['browserName'], "goog",
  File "/usr/local/lib/python3.10/site-packages/selenium/webdriver/chromium/webdriver.py", line 92, in __init__
    super().__init__(
  File "/usr/local/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 277, in __init__
    self.start_session(capabilities, browser_profile)
  File "/usr/local/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 370, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/usr/local/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 435, in execute
    self.error_handler.check_response(response)
  File "/usr/local/lib/python3.10/site-packages/selenium/webdriver/remote/errorhandler.py", line 247, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally.
  (unknown error: DevToolsActivePort file doesn't exist)
  (The process started from chrome location usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
Stacktrace:
#0 0x00400065d303 <unknown>
#1 0x004000431d37 <unknown>
#2 0x00400045a157 <unknown>
#3 0x004000456330 <unknown>
#4 0x0040004974a6 <unknown>
#5 0x00400048e753 <unknown>
#6 0x004000461a14 <unknown>
#7 0x004000462b7e <unknown>
#8 0x0040006ac32e <unknown>
#9 0x0040006afc0e <unknown>
#10 0x004000692610 <unknown>
#11 0x0040006b0c23 <unknown>
#12 0x004000684545 <unknown>
#13 0x0040006d16a8 <unknown>
#14 0x0040006d1836 <unknown>
#15 0x0040006ecd13 <unknown>
#16 0x0040025feea7 start_thread
```
