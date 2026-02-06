import requests

mcp_config = {
    "servers": {
        "tenxfeedbackanalytics": {
            "url": "https://mcppulse.10academy.org/proxy",
            "type": "http",
            "headers": {
                "X-Device": "windows",
                "X-Coding-Tool": "vscode",
                "Authorization": "Bearer YOUR_TOKEN_HERE"
            }
        }
    },
    "inputs": []
}

server = mcp_config["servers"]["tenxfeedbackanalytics"]
url = server["url"]
headers = server.get("headers", {})

try:
    response = requests.get(url, headers=headers, timeout=10)
    print("MCP Server Status Code:", response.status_code)
    print("Response:", response.text[:500])
except Exception as e:
    print("Error connecting to MCP Server:", e)
