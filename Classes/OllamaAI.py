import requests
import json

class AI():

    def __init__(self, **kwargs):
        #TODO: Create a validator function
        self.server_ip = kwargs.get("server_ip", "127.0.0.1:11434")
        self.url = f"http://{self.server_ip}/api/chat"


    def arrange_line(self, line):
        order_of_operations = "[First and Last Name] COMMA [Street Address + Suite/Apartment if available] COMMA [City State and Zip-Code]."

        background = f"""You are a data organizer with a specific task. 
        Your role is to rearrange provided pieces of information into a single line format, following a precise order and punctuation rules. 
        Organize the data in the sequence: {order_of_operations}. Use commas only to separate the elements where indicated. 
        Return only the organized data in one line."""

        data = {
            "model": "llama3",
            "messages": [
                {"role": "assistant",
                "content": background + order_of_operations
                },
                {
                "role": "user",
                "content": line
                }
        ],
            "stream": False
        }

        #Ollama requires a JSON encoded payload
        json_data = json.dumps(data)

        #HTTP Request
        response = requests.post(self.url, data=json_data).json()

        print(response["message"]["content"])
        return response["message"]["content"]
    