from flask import Flask, render_template, request, redirect, url_for
from countdown.flask_config import Config
import logging
# from countdown.clock import Clock
from countdown.utils import get_clock_path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)

options = Options()
chromium_path = '/usr/bin/chromium-browser'
options.binary_location = chromium_path
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/start_countdown', methods=['POST'])
def start_countdown():
    
    start_time = request.form.get('starttime')

    logging.info(f"Received Start Time: {start_time}")

    base_url = get_clock_path()

    # clock = Clock(base_url, start_time, '')

    logging.info(f"Start Counting Down")
    
    # clock.start_clock()
    # clock.start_clock_chromium()
    driver.get('http://www.google.com')
    driver.fullscreen_window()


    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    
    logging.info("Received message : %s", message)
    
    base_url = get_clock_path()

    # clock = Clock(base_url, '', message)

    # clock.start_clock_chromium()
    driver.get('file:///home/jonathan/Documents/Repo/countdown/index.html?message=hello')
    driver.fullscreen_window()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
