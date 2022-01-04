"""

Translator module uses IBM Watson Language translator and provides 2 functions:
1. englishToFrench - function takes in the englishText as a string argument and
return the French text

2. frenchToEnglish - function takes in the frenchText as a string argument and
return the English text

"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']


authenticator = IAMAuthenticator(apikey)

# create an instance of the IBM Watson Language translator
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """
    Function takes in the englishText as a string argument and return the French text
    """

    if english_text == '':
        return 'Text to be translated not provided'
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']


def french_to_english(french_text):
    """
    Function takes in the frenchText as a string argument and return the English text
    """

    if french_text == '':
        return 'Text to be translated not provided'
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']
