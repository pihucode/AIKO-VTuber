# from audio_utils import record_mic_audio, play_recording
from deepgram_test import speech_to_text
from deepl_tutorial import translate
from voicevox_tut import text_to_speech
import asyncio
from playsound import playsound
import sounddevice as sd
import soundfile as sf


async def main():
    # record_mic_audio()
    # text = speech_to_text()
    # # text = 'The best ramen is free ramen!'
    # translated_txt = translate(text, target_lang='JA')
    # print(translated_txt)

    # await text_to_speech(translated_txt)
    # playsound('voicevox_output.wav')

    filename = 'voicevox_output.wav'
    data, fs = sf.read(filename, dtype='float32')
    sd.default.device = [3, 5]
    sd.play(data, samplerate=fs, device=3, blocking=False)
    status = sd.wait()  # Wait until file is done playing
    sd.play(data, samplerate=fs, device=5, blocking=False)

    # Define the output stream with the specified devices
    # with sd.OutputStream(device=[3,5], channels=2, samplerate=fs) as out_stream:
    #     # Play the audio data through the output stream
    #     out_stream.write(data)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
