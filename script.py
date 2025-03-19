# Authors: Avyrie Fellows, Lydia Porter, Melanie Jensen, Cooper Gale, Cierra Loepker

# imports
from abc import ABC, abstractmethod
import os

os.system("pip install requests transformers")
from textblob import TextBlob


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
    def determine_bias(Bias):
        if Bias == "ExBias":
            return ExBias()
        elif Bias == "HighBias":
            return HighBias()
        elif Bias == "ModerateBias":
            return ModerateBias()
        elif Bias == "LowBias":
            return LowBias()
        elif Bias == "ExLowBias":
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

# Class Ai-decision (API)

API_URL = "https://api-inference.huggingface.co/models/roberta-base-openai-detector"

headers = {"Authorization": f" "}

def detect_fake_news(text):
    """Send input text to the Hugging Face model and get a prediction."""
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        result = response.json()
        print("Full API Response:", result)  
        
        prediction = result[0]
        label = prediction[0]['label']  
        score = prediction[0]['score']  
        
        print(f"Label: {label}, Score: {score}")  
        
        if label == "Fake":
            return "Fake News"
        elif label == "Real":
            return "Not Fake News"
        else:
            return "Unknown Label"
    else:
        return f"Error: {response.status_code}, {response.text}"  

# Textblob
user_input = input("Enter text: ")

blob = TextBlob(user_input)
blob.sentiment

bias = blob.sentiment.subjectivity # Number for Subjectivity (Bias)

polarity = blob.sentiment.polarity # Number for Polarity (+/-)

# Method/class calls

# prediction = detect_fake_news(user_input) # Prediction (Fake News/Not Fake News) from AI

# if statements for bias/polarity/news
# Bias
if 0 < bias < .2:
    bias = "ExLowBias"
elif .2 < bias < .4:
    bias = "LowBias"
elif .4 < bias < .6:
    bias = "ModerateBias"
elif .6 < bias < .8:
    bias = "HighBias"
elif .8 < bias <= 1:
    bias = "ExBias"

# Polarity
if -1 < polarity < -0.333:
    polarity = "Negative"
elif -0.333 < polarity < 0.333:
    polarity = "Neutral"
elif 0.333 < polarity < 1:
    polarity = "Positive"

# News
# if prediction == 'Fake News':
#     pass 
# elif prediction == 'Not Fake News':
#     pass

# order of operations:

# Passing values into Superclass to determine subclasses
determined_bias = BiasFactory.determine_bias(bias)
determined_polarity = PolarityFactory.determine_polarity(polarity)

print(determined_bias, determined_polarity)