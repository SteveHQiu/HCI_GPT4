#%%
import time

# Webscraper 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # By variable is used in subsequent finders
from selenium.webdriver.chrome.options import Options # Needed to run chrome headless
from selenium.common.exceptions import TimeoutException # Needed to catch timeouts
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def initChrome(url="https://yep.com/"):
    chrome_options = Options()
    chrome_options.add_argument("enable-automation")
    # chrome_options.add_argument("--headless");
    # chrome_options.add_argument("--window-size=1920,1080");
    # chrome_options.add_argument("--no-sandbox");
    # chrome_options.add_argument("--disable-extensions");
    # chrome_options.add_argument("--dns-prefetch-disable");
    chrome_options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service, options=chrome_options) # Embedded CromeDriverManager is imported separately from Selenium 
    driver.get(url)
    return driver

driver = initChrome()
html_out = driver.page_source
time.sleep(3)
with open("ztest.html", "w+", encoding="utf-8") as file:
    file.write(html_out)
    
#%%