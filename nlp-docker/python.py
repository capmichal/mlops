from flask import Flask, request, make_response, send_file
from stemming.porter2 import stem

app = Flask(__name__)

def cleanse_text(text):
    if text:
        # whitespaces
        clean = " ".join(text.split()) 

        # Stemming
        reduced_text = [stem(word) for word in clean.split()] # doesnt have to split ?

        return " ".join(reduced_text)

    else:
        return text         
    

print(cleanse_text("siema   anie asdas effictien"))