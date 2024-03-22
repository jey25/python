import requests
import json

def translate_text(text, target_lang, api_key):
    url = "https://api.deepl.com/v2/translate"
    params = {
        "text": text,
        "target_lang": target_lang,
        "auth_key": api_key
    }

    response = requests.post(url, data=params)
    translation_result = json.loads(response.content.decode('utf-8'))

    if 'translations' in translation_result:
        translated_text = translation_result['translations'][0]['text']
        return translated_text
    else:
        return None

# DeepL API 키
api_key = "b20a8e2c-2976-4da5-be2c-ce24aec809cb:fx"

# 번역할 텍스트
text_to_translate = "Hello, how are you?"

# 번역 대상 언어 코드 (예: 'ko'는 한국어)
target_language = "ko"

# 번역 수행
translated_text = translate_text(text_to_translate, target_language, api_key)

# 번역 결과 출력
if translated_text:
    print("번역 결과:", translated_text)
else:
    print("번역 실패")