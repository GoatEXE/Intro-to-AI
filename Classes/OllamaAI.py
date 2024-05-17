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
        background = f"""
        Organize data into a single line format following this sequence: {self.data_form_factor}.
        Use commas to separate the elements where shown in the sequence.
        Return only the organized data and say nothing else."""

        data = {
            "model": "phi3",
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
        background = f"""You are responsible for conforming data to a sequence.
        Validate that the given data is in this sequence: {order_of_operations}.
        Modify text or punctuation as necessary.
        Return the result and say nothing else.
        {self.validating_modifier}
        """

        url = f"http://{self.server_ip}/api/chat"


        data = {
            "model": "phi3",
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
            "model": "phi3",
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
    