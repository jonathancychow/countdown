from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dateutil import parser
from datetime import datetime
import logging
from countdown.utils import get_clock_path
from shutil import which

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

class ClockDriver():

    # FIXME: duplicate code for chrome and chromium

    def start_clock_chrome():
        from webdriver_manager.chrome import ChromeDriverManager
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        driver.fullscreen_window()
    
    def start_clock_chromium():
        options = Options()
        options.binary_location = which('chromium-browser')
        if options.binary_location == None:
            logging.warning("Chromium-browser not found, add browser binary to path")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(chrome_options=options)
        driver.fullscreen_window()
        return driver

class ClockMessage():
    def __init__(self, target_time:str, message:str):
        self.clock_url = get_clock_path()
        self.target_time = target_time
        self.message = message

    def calculate_time(self):
        logging.info("Target time: %s", self.target_time)

        target_datetime = parser.parse(self.target_time)
        now_datetime = datetime.now()
        time_delta = target_datetime - now_datetime
        return int(time_delta.total_seconds())
    
    def set_url(self):
        url = ''
        if self.target_time != '':
            second = self.calculate_time()
            url = self.clock_url + '?time='+ str(second) + '&alert=30'
        if self.message != '':
            url = self.clock_url + '?message='+ self.message

        logging.info("Clock URL: %s", url)
        return url
        
if __name__ == '__main__':
    # base_url = 'https://jonathancychow.github.io/countdown/'
    # param = '?time=35&alert=30'
    target = '2021-04-11T16:39'
    url = ClockMessage(target,'').set_url()
    print(url)





# see this link 
# https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
