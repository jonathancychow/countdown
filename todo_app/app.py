from flask import Flask, render_template, request

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    items = get_items()
    title = request.form.get('title')
    done_item = request.form.get('title2')

    all_itmes = get_items()

    if done_item:
        for this_item in all_itmes:
            if this_item['title'] == done_item:
                this_item['status'] = 'Done'
                save_item(this_item)
    if title:
        add_item(title)

    items = sorted(items, key=lambda i: i['status'], reverse=True)
    return render_template('index.html', items = items)

if __name__ == '__main__':
    app.run()
