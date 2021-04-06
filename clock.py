from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Clock():
    def __init__(self):
        self.chrome_location = '/usr/bin/google-chrome'

    def start_clock(self):
        driver = webdriver.Chrome(self.chrome_location)
        driver.get("http://www.python.org")

# clock = Clock()
# clock.start_clock()


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# caps = options.to_capabilities()
# driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=caps)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)


driver.get('http://hurry-app.appspot.com/12:34/Final')
driver.fullscreen_window()

# see this link 
# https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path


a= 1 
