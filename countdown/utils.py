from pathlib import Path
from pathlib import PurePath

def get_clock_path():
    current_path = Path.cwd()

    # FIXME: hardcode for linux file system
    local_html = 'file://' + str(PurePath(current_path,'index.html'))
    web_url = 'https://jonathancychow.github.io/countdown/'

    # FIXME: hardcode for reading local html
    url = local_html
    return url 