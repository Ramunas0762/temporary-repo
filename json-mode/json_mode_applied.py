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

# Complaint letter recognizer

#Generate me a mock complaint letter
complaint_letter = """Dear Customer Service,
I am writing to express my complaint with the recent purchase I made from your store.
 The product arrived damaged and did not match the description provided on your website. 
 I expected a much higher quality based on the price I paid.
I would like to request a full refund for this item, as I believe it does not meet the standards promised. 
Please let me know how to proceed with the return process.
Thank you for your attention to this matter.
Sincerely, John Doe
    """
love_letter = """Dear [Name],
I hope this letter finds you well. I wanted to take a moment to express my feelings for you.
You have brought so much joy and happiness into my life, and I am truly grateful for that.
"""
client = openai.OpenAI(
    api_key=token,
    base_url=endpoint)

response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system","content": """You are a helpful assistant that recognizes complaint letters. Please let me know if the letter is a complaint or not.
             Please respond with True or False."""},
            {"role": "user","content": complaint_letter},
        ],
        temperature=0.7,
        
        )

print(response.choices[0].message.content)

text = response.choices[0].message.content
if "true" in text.lower():
    print("[bold red] This is Complaint letter.[/bold red]")
else:
    print("[bold green]Not a complaint letter.[/bold green]")

