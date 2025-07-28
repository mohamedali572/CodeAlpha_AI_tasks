from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    """
    Translate text using googletrans library
    :param text: The input text to translate
    :param src_lang: The source language code (e.g., 'en', 'ar', 'fr')
    :param dest_lang: The target language code (e.g., 'en', 'ar', 'fr')
    :return: The translated text or an error message
    """
    try:
        translator = Translator()  # Initialize translator
        translated = translator.translate(text, src=src_lang, dest=dest_lang)  # Perform translation
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"  # Return error message if something goes wrong

