import base64
import requests
from os import environ as env


GENERATE_URL = "/generate"


"""
curl -X 'POST' \
  'https://xxxxxx.proxy.runpod.net/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "inputs": "My name is Olivier and I",
  "parameters": {
    "best_of": 1,
    "decoder_input_details": true,
    "details": true,
    "do_sample": true,
    "max_new_tokens": 20,
    "repetition_penalty": 1.03,
    "return_full_text": false,
    "seed": null,
    "stop": [
      "photographer"
    ],
    "temperature": 0.5,
    "top_k": 10,
    "top_p": 0.95,
    "truncate": null,
    "typical_p": 0.95,
    "watermark": true
  }
}'
"""



class TGIAdaptor:
    _initialized = False
    _url = None

    @classmethod
    def init(cls):
        cls._url = 'https://sk9pcvjlbow7re-7860.proxy.runpod.net'
        cls._initialized = True

    @staticmethod
    def models():
        return ["",]

    @classmethod
    @property
    def initialized(cls):
        return cls._initialized

    @classmethod
    def default_system_prompt(cls):
        return "You are a helpful assistant"

    @classmethod
    def get_vector(cls, query):
        pass

    @classmethod
    def send(cls, model, messages, temperature, max_tokens):
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
        }
        data = {"inputs": str(messages),
        }
        #"maxTokens": max_tokens, "temperature": temperature}
        #{
        """
  "parameters": {
    "best_of": 1,
    "decoder_input_details": true,
    "details": true,
    "do_sample": true,
    "max_new_tokens": 20,
    "repetition_penalty": 1.03,
    "return_full_text": false,
    "seed": null,
    "stop": [
      "photographer"
    ],
    "temperature": 0.5,
    "top_k": 10,
    "top_p": 0.95,
    "truncate": null,
    "typical_p": 0.95,
    "watermark": true
  }
}
"""

        print("REQ:", cls._url+GENERATE_URL)
        print("REQ:", data)
        resp = requests.post(
            cls._url + GENERATE_URL,
            headers=headers,
            json=data,
            timeout=20,
            verify=True,
        )

        print("RES:", resp)
        print("RES:", resp.text)
        #RES: {"generated_text":"Oh no, I don't have an umbrella.\n\n### Request:\n"}
        #return {"response": "", "message": "message", "content": "content"}
        resp = resp.json()
        return {"response": resp, "message": resp["generated_text"], "content": resp["generated_text"]}
