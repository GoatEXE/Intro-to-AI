import requests
import json

class AI():

    def __init__(self, **kwargs):
        #TODO: Create a validator function
        self.server_ip = kwargs.get("server_ip", "127.0.0.1:11434")
        self.url = f"http://{self.server_ip}/api/chat"
        self.data_form_factor = kwargs.get("data_form_factor", str())
        self.data_type = kwargs.get("data_type", str())
        self.validating_modifier = kwargs.get("validating_modifier", str())


    def arrange_line(self, line):
        

        background = f"""You are a data organizer with a specific task. 
        Your role is to rearrange provided pieces of information into a single line format, following a precise order and punctuation rules. 
        Organize the data in this sequence: {self.data_form_factor}. Use commas only to separate the elements where indicated. 
        Return only the organized data in one line."""

        data = {
            "model": "llama3",
            "messages": [
                {"role": "assistant",
                "content": background + self.data_form_factor
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

        message = self.validate(self.data_form_factor, response["message"]["content"])
        return message    
    
    
    def validate(self, order_of_operations, content):
        """
        Given a form factor that data is to adhere do, AI validates that the given data matches the form factor.
        AI is given permission to adjust the content as needed in order to adjust to the form factor.
        """
        background = f"""You are a data validator. Data given to you must match this rule set: {order_of_operations}.
        Modify text and punctuation as needed. If multiple {self.data_type}s are found, return one on a separate line.
        Return only the validated {self.data_type} and say nothing else.

        {self.validating_modifier}"""

        url = f"http://{self.server_ip}/api/chat"


        data = {
            "model": "llama3",
            "messages": [
                {"role": "assistant",
                "content": background
                },
                {
                "role": "user",
                "content": content
                }
        ],
            "stream": False
        }

        #Ollama requires a JSON encoded payload
        json_data = json.dumps(data)

        #HTTP Request
        response = requests.post(url, data=json_data).json()

        message = response["message"]["content"]
        print(message)

        return message
    

    def gather_nondata(self, content):
        background = f"""Identify and extract all strings from the dataset that is not a {self.data_type}.
        Provide that each item on its own line. Say nothing else."""

        url = f"http://{self.server_ip}/api/chat"


        data = {
            "model": "llama3",
            "messages": [
                {"role": "assistant",
                "content": background
                },
                {
                "role": "user",
                "content": content
                }
        ],
            "stream": False
        }

        #Ollama requires a JSON encoded payload
        json_data = json.dumps(data)

        #HTTP Request
        response = requests.post(url, data=json_data).json()

        message = response["message"]["content"]
        print(message)

        return message
    