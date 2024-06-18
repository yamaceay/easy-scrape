from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

def new_driver(url, path='/usr/local/bin/chromedriver'):
    # Set up the WebDriver
    service = Service(path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Open the URL
    driver.get(url)

    return driver

class Driver:
    def __init__(self, *args, **kwargs):
        self.driver = new_driver(*args, **kwargs)
    def __enter__(self):
        return self.driver
    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()