import os
from openai import OpenAI
from dotenv import load_dotenv

with open("birzai.txt", "r", encoding="utf-8") as f:
    birzai_text = f.read()

# Load environment variables from .env file
load_dotenv()
token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
print("Sveiki, uzduokite klausima apie Birzus")

while True:
    question = input ("Klausimas apie Biržus:   ")
    if question.lower() == "exit":
        print("Atsisveikiname!")
        break
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": f"Answer the question about Biržai based on the following text: {birzai_text} Question: {question}",
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    print(response.choices[0].message.content)
    print("Jei norite baigti, įveskite 'exit'.")
    print("Jei norite užduoti kitą klausimą, įveskite naują klausimą.") 