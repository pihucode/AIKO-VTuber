import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


class Chatbot:
    def __init__(self):
        self.message_history = [
            {"role": "system", "content": read_file('prompt_chat.txt')},
        ]

    def generate_response(self, prompt):
        print('Generating response...')

        message = {"role": "user", "content": prompt}
        self.message_history.append(message)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message_history,
            temperature=0.65,
            max_tokens=256,
            frequency_penalty=0.9,
            presence_penalty=0.4,
            stop=None,
        )
        response_text = response['choices'][0]['message']['content']
        print(response_text + '\n')

        response_message = {
            "role": "assistant",
            "content": response_text,
        }
        self.message_history.append(response_message)

        return response_text


# prompt = 'What do you like to do?'
# generate_response(prompt)
