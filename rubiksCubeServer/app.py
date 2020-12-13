from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import url_for
import json
import types
app=Flask(__name__)
from tools import getResults
import ast
from flask_cors import CORS, cross_origin

@app.route('/solve', methods=['POST'])
def solve():
    if request.method == 'POST':
        rev = request.form
        for i in rev:
            print(i)

        state = i
        state = state.replace('"', '')
        print("rev: ", rev)
        print("Computing...")
        # state = rev['state']
        print("State: ", state)
        res, success = getResults(state)
        if success:
            print("Complete!")
        else:
            print("Failed!")
        print("result: ", res)
        return jsonify(res)

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True)
    