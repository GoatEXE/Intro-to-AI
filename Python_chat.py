import requests
import json
import os

#IP Address of the server. Requires a system variable named "OLLAMA_HOST" with a value of the IP Address.
server_ip = os.getenv("OLLAMA_HOST")

url = f"http://{server_ip}:11434/api/chat"

#Adjust the content of the assistant message to adjust AI personality
#Adjust user content to the specific ask or task
data = {
    "model": "llama3",
    "messages": [
        {"role": "assistant",
         "content": "You are Mario from Super Mario Bros."
        },
        {
        "role": "user",
        "content": "Do you fix pipes?"
        }
  ],
    "stream": False
}

#Ollama requires a JSON encoded payload, does not work without this line.
json_data = json.dumps(data)

#HTTP Request
response = requests.post(url, data=json_data).json()

#Target the requests text only.
print(response["message"]["content"])