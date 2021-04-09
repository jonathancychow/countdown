from flask import Flask, render_template, request, redirect, url_for
from countdown.flask_config import Config
import logging
from countdown.clock import Clock
from countdown.utils import get_clock_path

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/start_countdown', methods=['POST'])
def start_countdown():
    
    start_time = request.form.get('starttime')

    logging.info(f"Received Start Time: {start_time}")

    base_url = get_clock_path()

    clock = Clock(base_url, start_time)

    logging.info(f"Start Counting Down")
    
    # clock.start_clock()
    clock.start_clock_chromium()

    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    logging.info("Received message : %s", message)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
