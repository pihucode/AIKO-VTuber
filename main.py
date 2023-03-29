from audio_utils import record_mic_audio
from deepgram_test import speech_to_text
from deepl_tutorial import translate
from openai_utils import generate_response
from voicevox_tut import text_to_speech
import asyncio
from playsound import playsound
import sounddevice as sd
import soundfile as sf
from threading import Thread

VOICEVOX_FILENAME = 'voicevox_output.wav'


async def main():
    record_mic_audio()
    prompt = speech_to_text()
    response_text = generate_response(prompt)
    print(response_text)
    translated_txt = translate(response_text, target_lang='JA')
    print(translated_txt)
    await text_to_speech(translated_txt)

    Thread(target=play_vtube_speakers).start()
    Thread(target=play_main_speakers).start()

    await main()


def play_vtube_speakers():
    data1, fs1 = sf.read(VOICEVOX_FILENAME, dtype='float32')
    sd.play(data1, fs1, device=5)
    sd.wait()


def play_main_speakers():
    data2, fs2 = sf.read(VOICEVOX_FILENAME, dtype='float32')
    sd.play(data2, samplerate=fs2, device=11)
    sd.wait()


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
