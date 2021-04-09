from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dateutil import parser
from datetime import datetime
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

class ClockDriver():
    # def __init__(self, url:str, target_time:str, message:str):
    #     self.chrome_location = '/usr/bin/google-chrome'
    #     self.clock_url = url
    #     self.target_time = target_time
    #     self.message = message

    def start_clock_chrome():
        from webdriver_manager.chrome import ChromeDriverManager
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        # driver.get('http://hurry-app.appspot.com/12:34/Final')
        # driver.get(self.set_url())
        driver.fullscreen_window()
    
    def start_clock_chromium():
        options = Options()
        chromium_path = '/usr/bin/chromium-browser'
        options.binary_location = chromium_path
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=options)
        # driver.get(self.set_url())
        driver.fullscreen_window()
        return driver

class ClockMessage():
    def calculate_time(self):
        print(self.target_time)
        target_datetime = parser.parse(self.target_time)
        now_datetime = datetime.now()
        time_delta = target_datetime - now_datetime
        return time_delta.seconds
    
    def set_url(self):
        if self.target_time != '':
            second = self.calculate_time()
            url = self.clock_url + '?time='+ str(second) + '&alert=30'
        if self.message != '':
            url = self.clock_url + '?message='+ self.message

        logging.info("Clock URL: %s", url)
        return url
        
if __name__ == '__main__':
    # base_url = 'https://jonathancychow.github.io/countdown/'
    base_url = 'file:///home/jonathan/Documents/Repo/countdown/index.html'
    # param = '?time=35&alert=30'
    target = '2021-04-07T13:30'
    # clock = Clock('http://hurry-app.appspot.com/12:34/Final')
    clock = Clock(base_url, '','hello')
    # sec = clock.set_url()
    # print(sec)
    clock.start_clock_chromium()
    # from selenium.webdriver.chrome.options import Options
    # options = Options()
    # # chromium_path = '/snap/bin/chromium'
    # chromium_path = '/usr/bin/chromium-browser'
    # options.binary_location = chromium_path
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(chrome_options=options)
    # driver.get(base_url)
    # driver.fullscreen_window()






# see this link 
# https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
