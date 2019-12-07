from Summarizer_Service.text_summarizer import summarize_text

from flask import Flask, request, json

app = Flask(__name__)

@app.route('/sumarizeText', methods=['POST'])
def sumarizeText ():
    data = request.get_json ()
    text = data['text']
    num_sent = data['num_sent']

    summary = summarize_text (text, num_sent)
    # summary = ' '.join(summary)

    response = {
        'summary': summary
    }

    return json.dumps (response)

@app.route('/', methods=['GET'])
def homeRoute ():
    return ('<h1>Hello world</h1>')
