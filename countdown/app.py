from flask import Flask, render_template, request, redirect, url_for
from countdown.flask_config import Config
import logging
from countdown.clock import ClockDriver, ClockMessage
from countdown.utils import get_clock_path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)

def start_up():
    driver = ClockDriver.start_clock_chromium()
    message_url = ClockMessage('', ' ','',1).set_url()
    logging.info(f"Starting up with url: {message_url}")
    driver.get(message_url)
    driver.fullscreen_window()
    return driver

driver = start_up()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_specific_time', methods=['POST'])
def start_specific_time():
    
    start_time = request.form.get('starttime')
    logging.info(f"Received Start Time: {start_time}")

    message_url = ClockMessage(start_time,'', '',0).set_url()

    logging.info(f"Start Counting Down")
    driver.get(message_url)
    driver.fullscreen_window()

    return redirect(url_for('index'))

@app.route('/start_fixed_time', methods=['POST'])
def start_fixed_time():
    
    start_time = request.form.get('fixtime')
    logging.info(f"Received Start Time: {start_time}")

    message_url = ClockMessage('', '',start_time,0).set_url()

    logging.info(f"Start Counting Down")
    driver.get(message_url)
    driver.fullscreen_window()

    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():

    message = request.form['message']
    logging.info("Received message : %s", message)
    
    message_url = ClockMessage('', message,'',0).set_url()

    logging.info(f"Message sent to screen")
    driver.get(message_url)
    driver.fullscreen_window()

    return redirect(url_for('index'))

@app.route('/show_current', methods=['POST'])
def show_current():

    logging.info("Received request to display current time")
    
    message_url = ClockMessage('', ' ','',1).set_url()

    logging.info(f"Message sent to screen")
    driver.get(message_url)
    driver.fullscreen_window()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
