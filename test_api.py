from openai import OpenAI
import os
from dotenv import load_dotenv
import httpx

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=httpx.Client(verify=False)
)

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello"}
        ],
        max_tokens=10
    )
    print("API works:", response.choices[0].message.content)
except Exception as e:
    print("Error:", e)
