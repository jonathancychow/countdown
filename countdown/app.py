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

driver = ClockDriver.start_clock_chromium()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_countdown', methods=['POST'])
def start_countdown():
    
    start_time = request.form.get('starttime')
    logging.info(f"Received Start Time: {start_time}")

    message_url = ClockMessage(start_time, '').set_url()

    logging.info(f"Start Counting Down")
    driver.get(message_url)
    driver.fullscreen_window()

    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():

    message = request.form['message']
    logging.info("Received message : %s", message)
    
    message_url = ClockMessage('', message).set_url()

    logging.info(f"Message sent to screen")
    driver.get(message_url)
    driver.fullscreen_window()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
