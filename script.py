# Authors: Avyrie Fellows, Lydia Porter, Melanie Jensen, Cooper Gale, Cierra Loepker

# Imports
# Imports for classes
from abc import ABC, abstractmethod
import os

# Imports for Textblob (sensitivity and polarity analysis)
os.system("pip install requests transformers")
from textblob import TextBlob

# Import for API Access
import requests

# Import for DeepSeek
from llama_cpp import Llama

# Flask is used to create the html page
from flask import Flask, render_template, request
app = Flask(__name__)

# Class Bias
class ClassBiased(ABC):
    @abstractmethod
    def determine_bias(self):
        pass

# Class ExBias inherits from Class Biased
class ExBias(ClassBiased):
    def determine_bias(self):
        return "Extreme Bias Detected: The text appears to be highly opinionated, indicating that there may be little to no factual basis. This indicates that the text may be strongly subjective, reflecting personal beliefs or persuasive rhetoric."

# Class HighBias inherits from Class Biased
class HighBias(ClassBiased):
    def determine_bias(self):
        return "High Bias Detected: The text appears to be mostly subjective, but may still contain some factual elements. This indicates that the text may contain opinion-driven arguments or interpretations."

# Class ModerateBias inherits from Class Biased
class ModerateBias(ClassBiased):
    def determine_bias(self):
        return "Moderate Bias Detected: he text appears to have a balanced mix of subjective and objective language. This indicates that the text appears to include opinions as well as factual content."

# Class LowBias inherits from Class Biased
class LowBias(ClassBiased):
    def determine_bias(self):
        return "Low Bias Detected: The text appears to be mostly objective, with minor subjective elements. This indicates that the text focuses on facts but may include slight opinions or interpretations."
        
# Class ExLowBias inherits from Class Biased
class ExLowBias(ClassBiased):
    def determine_bias(self):
        return "Extremely Low Bias Detected: The text appears to be highly objective, indicating that it is almost entirely based on factual statements with minimal or no subjectivity."

# Class Factory BiasFactory
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

# Class Positive inherits from Class Polarity
class Positive(Polarity):
    def determine_polarity(self):
        return "Positive Polarity Detected: The text appears to express an overall positive sentiment, indicating that the overall connotation of words and phrases shows optimism, approval, or favorable opinions."

# Class Neutral inherits from Class Polarity
class Neutral(Polarity):
    def determine_polarity(self):
        return "Neutral Polarity Detected: The text does not appear to strongly express positive or negative sentiment. This indicates that text may be factual, balanced, or emotionally neutral."

# Class Negative inherits from Class Polarity
class Negative(Polarity):
    def determine_polarity(self):
        return "Negative Polarity Detected: The text appears to express an overall negative sentiment, indicating that the overall connotation of words and phrases shows criticism, disapproval, or unfavorable opinions."

# Class Factory PolarityFactory
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

# Class Fake inherits from Class FakeNews
class Fake(FakeNews):
   def determine_fake(self):
       return "AI detected 'Fake' News: The AI model classifies the input as likely false or misleading, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output."

# Class Real inherits from Class FakeNews
class Real(FakeNews):
   def determine_fake(self):
       return "AI detected 'Real' News: The AI model classifies the input as likely factual or trustworthy, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output."

# Class Factory FakeNewsFactory
class FakeNewsFactory:
   @staticmethod
   def determine_fake(prediction):
       if prediction == "Fake News":
           return Fake()
       elif prediction == "Not Fake News":
           return Real()
       else:
           return None


# DeepSeek Model
llm = Llama.from_pretrained(
    repo_id="mradermacher/DeepSeekFakeNews-LLM-7B-Chat-GGUF",
    filename="DeepSeekFakeNews-LLM-7B-Chat.IQ4_XS.gguf",
    verbose=False  
)

# DeepSeek Method to detect fake/not fake news
class FakeNewsDetector:
    def __init__(self, llm):
        self.llm = llm

    # Trains AI to answer the way the application needs
    def create_prompt(self, user_input):
        return f"""
        Classify each of the following statements as either "Fake News" or "Not Fake News".

        Example 1:
        "The moon is made of cheese."
        Answer: Fake News

        Example 2:
        "Water boils at 100 degrees Celsius at sea level."
        Answer: Not Fake News

        Example 3:
        "5G towers caused the pandemic."
        Answer: Fake News

        Example 4:
        "The Earth is round."
        Answer: Not Fake News

        Now classify the following:
        "{user_input}"
        Answer:"""


    def classify(self, user_input):
        prompt = self.create_prompt(user_input)
        output = self.llm(prompt, max_tokens=10, temperature=0.3, stop=["\n"])
        reply = output['choices'][0]['text'].strip()
        print("🔍 Raw model response:", repr(reply))  # For debugging
        return self.interpret(reply)

    def interpret(self, reply):
        normalized = reply.lower().strip()

        if "not fake news" in normalized:
            return "Not Fake News"
        elif normalized in ["not fake", "real", "true"]:
            return "Not Fake News"
        elif "fake news" in normalized:
            return "Fake News"
        elif normalized in ["fake"]:
            return "Fake News"
        else:
            return f"Uncertain: {reply}"


# Method/class calls
# Analysis Method to determine the bias, subjectivity, and AI prediction
def analysis(input):
    blob = TextBlob(input)
    blob.sentiment
    bias = blob.sentiment.subjectivity # Number for Subjectivity (Bias)
    polarity = blob.sentiment.polarity # Number for Polarity (+/-)
    detector = FakeNewsDetector(llm) # object for the AI Model
    prediction = detector.classify(input) # Fake News Output (Fake News / Not Fake News)

    # if statements for bias/polarity/news
    # Bias
    if 0 <= bias < .2:
        determined_bias = BiasFactory.determine_bias("ExLowBias")
    elif bias < .4:
        determined_bias = BiasFactory.determine_bias("LowBias")
    elif bias < .6:
        determined_bias = BiasFactory.determine_bias("ModerateBias")
    elif bias < .8:
        determined_bias = BiasFactory.determine_bias("HighBias")
    elif bias <= 1:
        determined_bias = BiasFactory.determine_bias("ExBias")

    # Polarity
    if -1 <= polarity < -0.333:
        determined_polarity = PolarityFactory.determine_polarity("Negative")
    elif polarity < 0.333:
        determined_polarity = PolarityFactory.determine_polarity("Neutral")
    elif polarity <= 1:
        determined_polarity = PolarityFactory.determine_polarity("Positive")

    # News
    if prediction == "Fake News":
        determined_prediction = FakeNewsFactory.determine_fake("Fake News")
    elif prediction == "Not Fake News":
        determined_prediction = FakeNewsFactory.determine_fake("Not Fake News")


    return [determined_bias.determine_bias(), determined_polarity.determine_polarity(), determined_prediction.determine_fake()]

# Routes to index.html (homepage)
@app.route('/')
def index():
    return render_template("index.html")

# Routes to results.html upoon user input
# Uses analysis() to create output for results.html
@app.route('/results', methods=['POST'])
def results():

    if request.method == 'POST':
        user_input = request.form['user_input']
        bias = analysis(user_input)[0]
        polarity = analysis(user_input)[1]
        prediction = analysis(user_input)[2]

    context = {
    'bias': bias,
    'polarity': polarity,
    'prediction': prediction
    }

    return render_template("results.html", **context)
