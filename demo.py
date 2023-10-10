from genericpath import exists
import time, platform

import undetected_chromedriver as uc
from selenium import webdriver
import re, requests, json, base64

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementClickInterceptedException,
    WebDriverException,
    TimeoutException,
)

# options = webdriver.ChromeOptions()
# # options.binary_location = "C:\\Users\\ROG\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
# # options.binary_location = "C:\\Users\\ROG\\Documents\\Chromium-Portable-win64-codecs-sync-oracle\\bin\\chrome.exe"
# # options.add_argument("--window-size=640,480")
# options.add_argument("--start-maximized")
# # options.add_argument('--headless')
# # options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# if platform.system().startswith('Windows'):
#     if use_subprocess_error:
#         driver = uc.Chrome(options=options)
#     else:
#         driver = uc.Chrome(options=options, use_subprocess=True)
# else:
#     driver = uc.Chrome(options=options)


from selenium import webdriver

# Path to the .crx file of the extension
extension_path = '/home/taj/workspace/projects/btech/JNTUA_RTOE_AUTO_SOLVE_CAPTCHA/noai_new.crx'
chrome_driver_path = '/home/taj/workspace/projects/btech/JNTUA_RTOE_AUTO_SOLVE_CAPTCHA/driver/chromedriver'

# Create ChromeOptions object
options = webdriver.ChromeOptions()

# Add the extension using the add_extension method
options.add_extension(extension_path)

# Create a Chrome driver with the configured options
driver = uc.Chrome(options=options)
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Your Selenium code here
# For example, you can use driver.get('https://example.com') to navigate to a website.
time.sleep(60)
# Close the browser when done
driver.quit()