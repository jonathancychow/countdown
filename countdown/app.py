from flask import Flask, render_template, request, redirect, url_for
from countdown.flask_config import Config
# from todo_app.data.session_items import get_items, add_item, save_item
# from todo_app.data.trello import get_todo, get_done, create_card, update_card, get_all, get_list_id
import logging
from countdown.data.busstop import get_bus_info, get_bus_code, get_postcode_info

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    long, lat = get_postcode_info()
    codes = get_bus_code(str(long), str(lat))
    itemsOne = get_bus_info(codes[0])
    itemsTwo = get_bus_info(codes[1])
    return render_template('index.html',
                           itemsOne = itemsOne, itemsTwo = itemsTwo
                           )

@app.route('/add_item', methods=['POST'])
def check_postcode():
    postcode = request.form.get('postcode')
    long, lat = get_postcode_info(postcode)
    codes = get_bus_code(str(long), str(lat))
    itemsOne = get_bus_info(codes[0])
    itemsTwo = get_bus_info(codes[1])
    return render_template('index.html', 
                            itemsOne = itemsOne, 
                            itemsTwo = itemsTwo
                           )
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
