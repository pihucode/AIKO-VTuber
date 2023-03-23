import deepl
import os
from dotenv import load_dotenv

load_dotenv()

DEEPL_AUTH_KEY = os.getenv('DEEPL_AUTH_KEY')
translator = deepl.Translator(DEEPL_AUTH_KEY)
usage = translator.get_usage()


def translate(text, target_lang):
    if usage.any_limit_reached:
        print('Error. Translation limit reached.')
        return

    result = translator.translate_text(
        text, source_lang='EN', target_lang=target_lang)
    return result.text


def main():
    eng_text = "i like watching anime"
    jpn_text = translate(eng_text, target_lang='JA')
    print(jpn_text)


if __name__ == "__main__":
    main()
