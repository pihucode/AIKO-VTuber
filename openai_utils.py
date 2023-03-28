import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(prompt, max_tokens=50):
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=max_tokens)
    return response['choices'][0]['text']


# res = generate_response("What is the weather today in NJ?", max_tokens=50)
# print(res['choices'][0]['text'])
