import requests
import json
import os

#Server IP Address from System environment variable
server_ip = os.getenv("OLLAMA_HOST")

#Endpoint
url = f"http://{server_ip}:11434/api/generate"

#Adjust the prompt value with your ask or comment.
data = {
    "model": "llama3",
    "prompt": "How are you?",
    "stream": False
}

#Ollama requires a JSON encoded payload, does not work without this line.
json_data = json.dumps(data)

#HTTP Request
response = requests.post(url, data=json_data).json()

#Target the requests text only.
print(response["response"])