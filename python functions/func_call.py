from json import tool
import os
from dotenv import load_dotenv
import openai
from pydantic import BaseModel
from rich import print
import json
from bs4 import BeautifulSoup

# Load environment variables from .env file
load_dotenv()

token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = openai.OpenAI(
    api_key=token,
    base_url=endpoint)

import requests

def get_city_info(Cusco):
    response = requests.get(f"https://en.wikipedia.org/wiki/Cusco")
    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = soup.get_text(strip=True)
    return page_text[:5000]  # Return the first 5000 characters of the page text

tools = [{
    "type": "function",
    "function": {
        "name": "get_city_info",
        "description": "get information about a city from Wikipedia.",
            },
}]

user_question = input("What you want to know about Cusco?")

messages = [{"role": "user", "content": user_question}]

completion = client.chat.completions.create(
    model=model,
    messages=messages,
    tools=tools,
)

#tool_call = completion.choices[0].message.tool_calls[0]
#args = json.loads(tool_call.function.arguments)

result = get_city_info()

messages.append(completion.choices[0].message)
messages.append({  # append tool call message               
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": str(result)
})
 

completion_2 = client.chat.completions.create(
    model=model,
    messages=messages,
    tools=tools,
)

print(completion_2.choices[0].message.content)