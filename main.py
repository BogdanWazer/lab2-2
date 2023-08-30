import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"google-key.json"

# def TransLate(lang: str, strr: str) -> dict:
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     if isinstance(strr, bytes):
#         text = strr.decode("utf-8")

#     result = translate_client.translate(strr, target_language=lang)

#     print("Text: {}".format(result["input"]))
#     print("Translation: {}".format(result["translatedText"]))
#     print("Detected source language: {}".format(result["detectedSourceLanguage"]))

#     return result


# TransLate((input('Введіть мову стандартом: ')), input('Введіть текст для перекладу:'))

# def LangDetect(txt: str) -> dict:
#     """Detects the text's language."""
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     result = translate_client.detect_language(txt)

#     print("Confidence: {}".format(result["confidence"]))
#     print("Language: {}".format(result["language"]))

#     return result


# LangDetect(input('Введіть текст для детекту мови: '))


#
#
def CodeLang(lang: str) -> dict:

    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    results = translate_client.get_languages(target_language=lang)

    for language in results:
        print("{name} ({language})".format(**language))

    return results
CodeLang(input('Введіть код мови: '))

#
# #
# def CodeLang(text: str) -> dict:
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()
    
#     result = translate_client.detect_language(text)
#     print(f"Text: {text}")
#     print("Confidence: {}".format(result["confidence"]))
#     print("Language: {}".format(result["language"]))

#     return result
# CodeLang(input("Введіть код мови: " ))

# import os
# from google.cloud import translate_v2 as translate

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"google-key.json"

# import os
# from google.cloud import translate_v2 as translate

# # Встановив шлях до файлу з ключем для Google Cloud Translation API
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"google-key.json"

# # Створення функції для обробки тексту, включаючи переклад та визначення мови
# def ProcessText(text: str, lang=None):
#     translate_client = translate.Client()

#     # Якщо надано мову для перекладу, виконуємо переклад
#     if lang:
#         translation = translate_client.translate(text, target_language=lang)
#         detected_language = lang
#     else:
#         # Якщо мова не надана, виконуємо автоматичне визначення мови та переклад
#         translation = translate_client.translate(text)
#         detected_language = translation["detectedSourceLanguage"]

#     # Визначення мови тексту
#     language_detection = translate_client.detect_language(text)

#     # Усі потрібні прінти результатів
#     print("Text: {}".format(text))
#     print("Detected Source Language: {}".format(detected_language))
#     print("Translation: {}".format(translation["translatedText"]))
#     print("Confidence: {}".format(language_detection["confidence"]))
#     print("Language: {}".format(language_detection["language"]))

# if __name__ == "__main__":
#     # Логіка вибору користувачем необхідного функціоналу:
#     choice = input("Оберіть дію (1 - переклад тексту, 2 - визначення мови): ")

#     if choice == "1":
#         text = input("Введіть текст для перекладу: ")
#         target_lang = input("Введіть мову стандартом (або залиште порожньо для автоматичного визначення): ")
#         ProcessText(text, lang=target_lang)
#     elif choice == "2":
#         text = input("Введіть текст для визначення мови: ")
#         ProcessText(text)
#     else:
#         print("Невірний вибір дії.")
