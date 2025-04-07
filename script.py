# Authors: Avyrie Fellows, Lydia Porter, Melanie Jensen, Cooper Gale, Cierra Loepker

# imports
from abc import ABC, abstractmethod
import os

os.system("pip install requests transformers")
from textblob import TextBlob

import requests

# Flask is used to create the html page
from flask import Flask, render_template, request

app = Flask(__name__)

# Class Bias
class ClassBiased(ABC):
    @abstractmethod
    def determine_bias(self):
        pass

class ExBias(ClassBiased):
    def determine_bias(self):
        return "This article seems to have an extreme bias"

class HighBias(ClassBiased):
    def determine_bias(self):
        return "This article seems to have a high bias"

class ModerateBias(ClassBiased):
    def determine_bias(self):
        return "This article seems to have a moderate bias"

class LowBias(ClassBiased):
    def determine_bias(self):
        return "This article seems to have a low bias"
        
class ExLowBias(ClassBiased):
    def determine_bias(self):
        return "This article seems to have an extremely low bias"

class BiasFactory:
    @staticmethod
    def determine_bias(bias):
        if bias == "ExBias":
            return ExBias()
        elif bias == "HighBias":
            return HighBias()
        elif bias == "ModerateBias":
            return ModerateBias()
        elif bias == "LowBias":
            return LowBias()
        elif bias == "ExLowBias":
            return ExLowBias()
        else:
            return None


# Class Polarity
class Polarity(ABC):
    @abstractmethod
    def determine_polarity(self):
        pass

class Positive(Polarity):
    def determine_polarity(self):
        return "This text expresses positive attitudes toward the main idea."

class Neutral(Polarity):
    def determine_polarity(self):
        return "This text is neutral."

class Negative(Polarity):
    def determine_polarity(self):
        return "This text expresses negative attitudes toward the main idea."

class PolarityFactory:
    @staticmethod
    def determine_polarity(polarity):
        if polarity == "Positive":
            return Positive()
        elif polarity == "Neutral":
            return Neutral()
        elif polarity == "Negative":
            return Negative()
        else:
            return None


# Class Fake News
class FakeNews(ABC):
   @abstractmethod
   def determine_fake(self):
       pass

class Fake(FakeNews):
   def determine_fake(self):
       return "The API suspects this is Fake."

class Real(FakeNews):
   def determine_fake(self):
       return "The API suspects this is Real."

class FakeNewsFactory:
   @staticmethod
   def determine_fake(prediction):
       if prediction == "Fake News":
           return Fake()
       elif prediction == "Not Fake News":
           return Real()
       else:
           return None


# Class Ai-decision (API)

API_URL = "https://api-inference.huggingface.co/models/roberta-base-openai-detector"
api_key = input("Enter your Hugging Face API key: ")

def detect_fake_news(text):
   headers = {"Authorization": f"Bearer {api_key}"}
   response = requests.post(API_URL, headers=headers, json={"inputs": text})

   if response.status_code == 200:
       result = response.json()

       if isinstance(result, list) and len(result) > 0 and isinstance(result[0], list):
           prediction = result[0][0]
           label = prediction.get('label', 'Unknown').lower()  # Convert to lowercase

           if label == "fake":
               return "Fake News"
           elif label == "real":
               return "Not Fake News"
       return "Unknown Label"
   else:
       return f"API Error: {response.status_code}"


# Method/class calls
# blob = TextBlob(user_input)
# blob.sentiment
# bias = blob.sentiment.subjectivity # Number for Subjectivity (Bias)
# polarity = blob.sentiment.polarity # Number for Polarity (+/-)
# prediction = detect_fake_news(user_input)


def analysis(input):
    blob = TextBlob(input)
    blob.sentiment
    bias = blob.sentiment.subjectivity # Number for Subjectivity (Bias)
    polarity = blob.sentiment.polarity # Number for Polarity (+/-)
    prediction = detect_fake_news(input)

    # if statements for bias/polarity/news
    # Bias
    if 0 <= bias < .2:
        determined_bias = BiasFactory.determine_bias("ExLowBias")
    elif .2 <= bias < .4:
        determined_bias = BiasFactory.determine_bias("LowBias")
    elif .4 <= bias < .6:
        determined_bias = BiasFactory.determine_bias("ModerateBias")
    elif .6 <= bias < .8:
        determined_bias = BiasFactory.determine_bias("HighBias")
    elif .8 <= bias <= 1:
        determined_bias = BiasFactory.determine_bias("ExBias")

    # Polarity
    if -1 <= polarity < -0.333:
        determined_polarity = PolarityFactory.determine_polarity("Negative")
    elif -0.333 <= polarity < 0.333:
        determined_polarity = PolarityFactory.determine_polarity("Neutral")
    elif 0.333 <= polarity <= 1:
        determined_polarity = PolarityFactory.determine_polarity("Positive")

    # News
    if prediction == "Fake News":
        determined_prediction = FakeNewsFactory.determine_fake("Fake News")
    elif prediction == "Not Fake News":
        determined_prediction = FakeNewsFactory.determine_fake("Not Fake News")


    return determined_bias.determine_bias(), determined_polarity.determine_polarity(), determined_prediction.determine_fake()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():

    if request.method == 'POST':
        user_input = request.form['user_input']
        bias, polarity, prediction = analysis(user_input)

    context = {
    'bias': bias,
    'polarity': polarity,
    'prediction': prediction
    }

    return render_template("results.html", **context)


# UNIT TEST SUITE
# import sys

# def test(did_pass):
#     """ Print the result of a test. """
#     linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
#     if did_pass:
#         msg = "Test at line {0} ok.".format(linenum)
#     else:
#         msg = ("Test at line {0} FAILED.".format(linenum))
#     print(msg)

# def test_suite():
#     # bias
#     test(ClassBiased("The moon landing was fake") == ClassBiased(ExBias))
#     test(user_input(123456789) == None)

#     # polarity
#     test(user_input("I love unicorns so much") == Positive)
#     test(user_input("The moon landing was fake") == Neutral)
#     test(user_input(123456789) == None)

#     # fake news
    
# #test()
# test_suite()