# Ollama-API
 Instructions and and setup for API access to a private language model. The usage of Ollama within an organization is useful in the case of dealing with customer or sensative data. Since Ollama does not communicate outside the local network, there is no risk of compromising data due to cloud language model learning.

## Installation/First Time Setup
 - Install Ollama Windows preview from https://ollama.com/
 - From command line local host: `ollama pull llama3`
 - Other commands, LLMs, and references found here https://github.com/ollama/ollama

## Usage
 - `ollama run llama3` will access a chat interface via command line.
 - API Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md

## Server Spinup
 - `ollama serve` will start a server instance 
 - You must first create a SYSTEM environment variable titled "OLLAMA_HOST" with a value of the IP address of the server device.
   - https://github.com/ollama/ollama/blob/main/docs/faq.md#how-can-i-expose-ollama-on-my-network
 - A potential error `localhost:11434: bind: adddress already in use` can populate if there's more than one Ollama service running in the background:
   - Close Ollama application is task tray or:
   - Launch command prompt as admin
   - `netstat -aon | findstr :11434`
   - `taskkill /F /PID <PID>`

## Classes
 - `OllamaAI.py` is responsible for interacting with the serving Ollama API. Example calls can be found in the `/AI-Examples` directory.
 - `PDF_Extractor.py` is a non-OCR PDF text extractor. Using several keyword arguements, you can set a delimiter, or even words or phrases you want filtered out. 