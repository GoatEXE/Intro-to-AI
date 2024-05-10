# Ollama-Private-API
 Instructions and and setup for API access to a private language model.

## Installation
 - Install Ollama Windows preview from `https://ollama.com/`
 - From command line: `ollama pull llama3`
 - Other commands, LLMs, and references found here `https://github.com/ollama/ollama`

## Usage
 - `ollama run llama3` will access a chat interface via command line.

## Server Spinup
 - `ollama serve` will start a server instance 
 - You must first create a SYSTEM environment variable titled "OLLAMA_HOST" with a value of the IP address of the server device: `https://github.com/ollama/ollama/blob/main/docs/faq.md#how-can-i-expose-ollama-on-my-network`
 - An error `localhost:11434: bind: adddress already in use` can populate if there's more than one Ollama service running in the background:
   - Launch command prompt as admin
   - `netstat -aon | findstr :11434`
   - `taskkill /F /PID <PID>`