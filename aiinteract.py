from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

client.api_key = os.getenv('OPENAI_API_KEY')

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Puedes responder un hola mundo?"
        }
    ]
)

print(completion.choices[0].message)