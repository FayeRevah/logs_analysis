#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for, render_template

from logs_analysisdb import get_popular_articles, get_high_errors,
    get_popular_authors

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.title { color: #999 }
    </style>
  </head>
  <body>
    <h1>Logs Analysis</h1>
    <div>
        %s
    </div>
    <div>
        %s
    </div>
    <div>
        %s
    </div>
  </body>
</html>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    dict1 = get_high_errors()
    dict2 = get_popular_authors()
    dict3 = get_popular_articles()
    return render_template('template.html', result=dict3, result2=dict2,
        result3=dict1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
