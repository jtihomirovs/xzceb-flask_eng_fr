"""

Translator backend using Flask framework

"""
from flask import Flask, render_template, request
from machinetranslation import translator
#import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """ Translate text from english to french """
    text_to_translate = request.args.get('textToTranslate')
    return translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def french_to_english():
    """ Transate text from french to english """
    text_to_translate = request.args.get('textToTranslate')
    return translator.french_to_english(text_to_translate)

@app.route("/")
def render_index_page():
    """ Route requests to index.html page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
