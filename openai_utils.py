import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def generate_response(prompt):
    print('Generating response...')
    chat_history = [
        {"role": "system", "content": read_file('prompt_chat.txt')},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=0.8,
        max_tokens=256,
        frequency_penalty=0.5,
        presence_penalty=.2,
        stop=None,
    )
    text = response['choices'][0]['message']['content']
    print(text)
    return text


# prompt = 'What do you like to do?'
# generate_response(prompt)
