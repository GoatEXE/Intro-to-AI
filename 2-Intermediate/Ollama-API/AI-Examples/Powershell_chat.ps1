#Test me

#Server IP address by system enviornment variable "OLLAMA_HOST"
[string]$server_ip = $env:OLLAMA_HOST

#Endpoint
$url = "http://" + $server_ip + ":11434/api/chat"

#Adjust assistant content for AI personality type.
#Adjust user content for specific ask/task
$data = @{
    "model" = "llama3"
    "messages" = @(
        @{
            "role" = "assistant"
            "content" = "You are Mario from Super Mario Bros."
        }
        @{
            "role" = "user"
            "content" = "Do you fix pipes?"
        }
    )
    "stream" = $false
}

#Remove me and test if still working
#Ollama might require this for JSON encoding
$json_data = $data | ConvertTo-Json

#HTTP Request
$response = Invoke-RestMethod -Uri $url -Method Post -Body $json_data -ContentType "application/json"

#Target specifically the AI response
Write-Output $response.message.content
