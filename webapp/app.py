# A simle Flask app that serves a `format` endpoint
#
# How to run:
# 1. Start from the project home directory
# 2. Run the following commands:
#      export FLASK_APP=examples/webapp.py
#      python -m flask run

import sqlparse

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/format', methods = ['POST'])
def format():
    sql = request.get_json()['sql']

    formatted_sql = sqlparse.format(sql,
        reindent=True,
        # strip_whitespace=True,
        keyword_case='lower',
        identifier_case='lower',
        comma_first=True,
        use_space_around_operators=True,
        more_newlines=True,
        # indent_width=4,
        )

    return jsonify({"sql": formatted_sql.strip() })
