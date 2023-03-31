from voicevox import Client
import asyncio

# Voicevox Wrapper Documentation: https://voicevox-client.tuna2134.jp/


async def getSpeakerInfo():
    async with Client() as client:
        speakers = await client.fetch_speakers()

        for speaker in speakers:
            print(speaker.name)
            styles = speaker.styles

            for style in styles:
                print("     ", style.id, style.name)

            print()


async def text_to_speech(text):
    speaker_id = 3
    async with Client() as client:
        audio_query = await client.create_audio_query(text, speaker=speaker_id)
        with open("voicevox_output.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=speaker_id))

# if __name__ == '__main__':
#     # asyncio.run(getSpeakerInfo())
#     asyncio.run(text_to_speech('こんにちは'))
