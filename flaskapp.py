from __future__ import print_function
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
import sys
import requests

app = Flask(__name__)
CORS(app)

API_URL = "https://api-inference.huggingface.co/models/openchat/openchat-3.5-0106"
headers = {"Authorization": "Bearer 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"}

@app.route('/api/call', methods=['POST'])
def api_call():
    data = request.get_json()['message']
    # response_data = {'message': 'API call successful!', 'input_data': data}
    # response_data = query()
    payload = {
        "inputs": data,
        "parameters": {
            "max_new_tokens": 1024,
            "temperature": 0.6,
            "top_p": 0.9,
            "do_sample": False,
            "return_full_text": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]


if __name__ == '__main__':
    app.run(debug=True)




