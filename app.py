from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client =genai.Client(api_key=os.getenv("API_KEY"))

response=client.models.generate_content(model="gemini-2.5-flash", contents=" Explain python loops to a 10 year old in 100 words")

print(response.text)