import nltk
import pickle
import pandas as pd
import keras
import tensorflow
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from flask import Flask, request
import numpy as np
import flasgger
from flasgger import Swagger
from flask_ngrok import run_with_ngrok
from keras.preprocessing.text import Tokenizer

"""### Data Loading and Preprocessing"""

#Dataset Loading
dataset = pd.read_csv('spam1.csv',names=['sentiment','statement'])
dataset

def cleanString(incomingString):
    newstring = incomingString
    newstring = newstring.replace("!","")
    newstring = newstring.replace("@","")
    newstring = newstring.replace("#","")
    newstring = newstring.replace("$","")
    newstring = newstring.replace("%","")
    newstring = newstring.replace("^","")
    newstring = newstring.replace("&","and")
    newstring = newstring.replace("*","")
    newstring = newstring.replace("(","")
    newstring = newstring.replace(")","")
    newstring = newstring.replace("+","")
    newstring = newstring.replace("=","")
    newstring = newstring.replace("?"," ")
    newstring = newstring.replace("\'","")
    newstring = newstring.replace("\"","")
    newstring = newstring.replace("'","")
    newstring = newstring.replace("'m","am")
    newstring = newstring.replace("}","")
    newstring = newstring.replace("[","")
    newstring = newstring.replace("]","")
    newstring = newstring.replace("<","")
    newstring = newstring.replace(">","")
    newstring = newstring.replace("~","")
    newstring = newstring.replace("`","")
    newstring = newstring.replace(":","")
    newstring = newstring.replace(";","")
    newstring = newstring.replace("|","")
    newstring = newstring.replace("\\","")
    newstring = newstring.replace("/","") 
    newstring = newstring.replace("0","")
    newstring = newstring.replace("1","")
    newstring = newstring.replace("2","")
    newstring = newstring.replace("3","")
    newstring = newstring.replace("4","")
    newstring = newstring.replace("5","")
    newstring = newstring.replace("6","")
    newstring = newstring.replace("7","")
    newstring = newstring.replace("8","")
    newstring = newstring.replace("9","")  
    newstring = newstring.replace(".","")
    newstring = newstring.replace(",","")
    return newstring



id = dataset['statement']
model = Tokenizer()
model.fit_on_texts(list(id))
print("Model Trained Successfully ! ")


#Creating the classifier function for queries
def classifier(text):
  print(text)
  text_ = cleanString(text)
  text_tokens = word_tokenize(text_)
  tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
  text = (" ").join(tokens_without_sw)
  vec = model.texts_to_matrix([text], mode='count')
  print(vec)
  return gnb.predict(vec)


##FLASK FRONTEND DEV
app = Flask(__name__)
run_with_ngrok(app) 
Swagger(app)


@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_spam_ham():
    """Let's predict Ham/Spam texts 
    ---
    parameters:  
      - name: text
        in: query
        type: string
        required: true
    responses:
        200:
            description: The output values      
    """
    text = request.args.get("text")
    print(text)
    prediction = classifier(str(text))
    print(prediction)
    return "The type of the text is : " + str(prediction)

app.run()