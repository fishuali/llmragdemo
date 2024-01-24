import requests


API_URL = "https://api-inference.huggingface.co/models/openchat/openchat-3.5-0106"
headers = {"Authorization": "Bearer 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"}

def query():
    payload = {
        "inputs": "who owns dallas cowboys",
        "parameters": {
             "max_new_tokens": 1024,
             "temperature": 0.6,
             "top_p": 0.9,
             "do_sample": False,
             "return_full_text": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response)
    return response.json()[0]['generated_text']
print(query())




