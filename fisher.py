"""
created by huan on 2021-02-16
"""
import json

from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook


app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q: 普通关键字 isbn
    page
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return json.dumps(result), 200, {'content-type': 'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

