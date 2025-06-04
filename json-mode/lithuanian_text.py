import os
from dotenv import load_dotenv
import openai
from pydantic import BaseModel
from rich import print
# Load environment variables from .env file
load_dotenv()

token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = openai.OpenAI(
    api_key=token,
    base_url=endpoint)

class UserInputLanguage(BaseModel):
    is_lithuanian: bool

def is_lithuanian_text(text: str) -> UserInputLanguage:
    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": """You are a helpful assistant that recognizes Lithuanian text. 
            Please let me know if the text is in Lithuanian or not. Respond with True or False."""},
            {"role": "user", "content": user_input_text},
        ],
        temperature=0.7,
        response_format=UserInputLanguage

    )

    response = response.choices[0].message.parsed
    return response

user_input_text = input("Please enter text: ")

user_language = is_lithuanian_text(user_input_text)

if user_language.is_lithuanian:
    print("[bold green] This is Lithuanian text:[/bold green]")
    followup_question = input("Įveskite klausimą: ")
    # Send the Lithuanian question to the model and print the answer
    answer_response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Atsakyk į klausimą lietuviškai."},
            {"role": "user", "content": followup_question},
        ],
        temperature=0.7
    )
    answer = answer_response.choices[0].message.content
    print(f"Atsakymas: {answer}")
else:
    print("[bold red]Not a Lithuanian text. Kreipkitės lietuviškai:[/bold red]")






