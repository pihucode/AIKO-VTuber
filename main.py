from audio_utils import record_mic_audio
from deepgram_test import speech_to_text
from deepl_tutorial import translate
from openai_utils import generate_response
from voicevox_tut import text_to_speech
import asyncio
import sounddevice as sd
import soundfile as sf
from threading import Thread
from subtitles_app import SubtitleApp

VOICEVOX_FILENAME = 'voicevox_output.wav'

subtitle_app = SubtitleApp()
subtitle_app.start()


async def main():
    subtitle_app.set_text('Hold down R to record audio')
    # record_mic_audio()
    # prompt = speech_to_text()
    prompt = 'What do you like doing?'
    print('Prompt: ' + prompt + '\n')

    response_text = generate_response(prompt)

    translated_txt = translate(response_text, target_lang='JA')
    subtitle_app.set_text('Generating voice...')

    await text_to_speech(translated_txt)
    subtitle_app.set_text(response_text)

    Thread(target=play_vtube_speakers).start()
    Thread(target=play_main_speakers).start()

    # await main()


def play_vtube_speakers():
    data1, fs1 = sf.read(VOICEVOX_FILENAME, dtype='float32')
    sd.play(data1, fs1, device=6)
    sd.wait()


def play_main_speakers():
    data2, fs2 = sf.read(VOICEVOX_FILENAME, dtype='float32')
    sd.play(data2, samplerate=fs2, device=11)
    sd.wait()


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
