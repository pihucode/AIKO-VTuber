from deepgram import Deepgram
import json
import os
from dotenv import load_dotenv

load_dotenv()

DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')
PATH_TO_FILE = 'microphone_audio.wav'


def speech_to_text():
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    # Open the audio file
    with open(PATH_TO_FILE, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = deepgram.transcription.sync_prerecorded(
            source, {'punctuate': True})
        # get transcript
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        print(transcript)
        return transcript


# speech_to_text()
