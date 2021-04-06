from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Clock():
    def __init__(self, url):
        self.chrome_location = '/usr/bin/google-chrome'
        self.clock_url = url

    def start_clock(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        # driver.get('http://hurry-app.appspot.com/12:34/Final')
        driver.get(self.clock_url)
        driver.fullscreen_window()

if __name__ == '__main__':
    clock = Clock('http://hurry-app.appspot.com/12:34/Final')
    clock.start_clock()



# see this link 
# https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
