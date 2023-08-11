import requests

BASE_URL = 'https://ai.fakeopen.com/v1/chat/completions'

class FakeOpenAI:
    def __init__(self, api_key):
        self.api_key = api_key

    def chat_completion(self, model, messages, max_tokens=1000):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': model,
            'max_tokens': max_tokens,
            'messages': messages
        }

        response = requests.post(BASE_URL, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

        return response.json()

    def create(self, model, messages):
        return self.chat_completion(model, messages)

fake_openai = None

def set_api_key(api_key):
    global fake_openai
    fake_openai = FakeOpenAI(api_key)

def ChatCompletion_create(model, messages):
    if fake_openai is None:
        raise Exception("API key not set. Please set it using set_api_key function.")
    return fake_openai.create(model, messages)
