from flask import Flask, render_template, request, redirect, url_for
from countdown.flask_config import Config
import logging
from countdown.clock import Clock

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
    # print(f"Start time: {start_time}")
    base_url = 'https://jonathancychow.github.io/countdown/'
    param = '?time=35&alert=30'
    # clock = Clock('http://hurry-app.appspot.com/12:34/Final')
    clock = Clock(base_url + param)
    logging.info(f"Start Counting Down")
    clock.start_clock()
    return redirect(url_for('index'))

# @app.route('/items/new', methods=['POST'])
# def add_item():
#     title = request.form['title']
#     description = request.form['description']
#     create_card(title, description)
#     return redirect(url_for('index'))


# @app.route('/items/complete', methods=['POST'])
# def complete_item():
#     done_item = request.form.get('title2')
#     items = get_todo()

#     for this_item in items:
#         if this_item['name'] == done_item:
#             update_card(this_item['id'])

#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
