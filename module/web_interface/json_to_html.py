from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)


@app.route("/")
def index():
    fpath = Path('data/articles.json').resolve()
    df = pd.read_json(fpath)
    df['date'] = pd.to_datetime(df['date']).dt.date
    content_df = df.to_dict('records')
    column_names = df.columns.values
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=content_df.__len__(), record_name='records', per_page=5)
    return render_template('record.html', records=df, content=content_df, colnames=column_names, pagination=pagination)


@app.route("/content")
def content():
    return render_template('content.html')


@app.route("/comments")
def comments():
    return render_template('comments.html')


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
