# Authors: Avyrie Fellows, Lydia Porter, Melanie Jensen, Cooper Gale, Cierra Loepker

# imports
from abc import ABC, abstractmethod
import os

os.system("pip install requests transformers")
from textblob import TextBlob

import requests


# Class Bias
class ClassBiased(ABC):
    @abstractmethod
    def determine_bias(self):
        pass

class ExBias(ClassBiased):
    def determine_bias(self):
        print("This article seems to have an extreme bias")

class HighBias(ClassBiased):
    def determine_bias(self):
        print("This article seems to have a high bias")

class ModerateBias(ClassBiased):
    def determine_bias(self):
        print("This article seems to have a moderate bias")

class LowBias(ClassBiased):
    def determine_bias(self):
        print("This article seems to have a low bias")
        
class ExLowBias(ClassBiased):
    def determine_bias(self):
        print("This article seems to have an extremely low bias")

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
        print("This text expresses positive attitudes toward the main idea.")

class Neutral(Polarity):
    def determine_polarity(self):
        print("This text is neutral.")

class Negative(Polarity):
    def determine_polarity(self):
        print("This text expresses negative attitudes toward the main idea.")

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
       print("The API suspects this is Fake.")

class Real(FakeNews):
   def determine_fake(self):
       print("The API suspects this is Real.")

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
user_input = input("Enter text: ")
blob = TextBlob(user_input)
blob.sentiment
bias = blob.sentiment.subjectivity # Number for Subjectivity (Bias)
polarity = blob.sentiment.polarity # Number for Polarity (+/-)
prediction = detect_fake_news(user_input) 

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


determined_bias.determine_bias()
determined_polarity.determine_polarity()
determined_prediction.determine_fake()