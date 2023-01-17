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
  driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
Traceback (most recent call last):
  File "//main.py", line 27, in <module>
    driver = webdriver.Chrome(executable_path='usr/bin/chromedriver', options=options)
  File "/venv/lib/python3.10/site-packages/selenium/webdriver/chrome/webdriver.py", line 69, in __init__
    super().__init__(DesiredCapabilities.CHROME['browserName'], "goog",
  File "/venv/lib/python3.10/site-packages/selenium/webdriver/chromium/webdriver.py", line 92, in __init__
    super().__init__(
  File "/venv/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 277, in __init__
    self.start_session(capabilities, browser_profile)
  File "/venv/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 370, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/venv/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 435, in execute
    self.error_handler.check_response(response)
  File "/venv/lib/python3.10/site-packages/selenium/webdriver/remote/errorhandler.py", line 247, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: crashed.
  (chrome not reachable)
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
#16 0x004002aa5b43 <unknown>
```

In Docker:

```bash
(venv) root@aa41c89ea2ec:/usr/bin# google-chrome --no-sandbox
qemu: uncaught target signal 5 (Trace/breakpoint trap) - core dumped
qemu: uncaught target signal 5 (Trace/breakpoint trap) - core dumped
[1532:1532:0117/194130.412767:ERROR:nacl_fork_delegate_linux.cc(313)] Bad NaCl helper startup ack (0 bytes)
qemu: uncaught target signal 5 (Trace/breakpoint trap) - core dumped
[1497:1542:0117/194130.528985:ERROR:file_path_watcher_inotify.cc(331)] inotify_init() failed: Function not implemented (38)
```


Other command in Docker:

```bash
apt-get install xvfb
apt-get install libexif-dev
python3 -m venv venv
source venv/bin/activate 
pip3 install -r requirements.txt
```

