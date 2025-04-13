# grabs analysis method from script.py to unit test
from script import analysis
# UNIT TEST SUITE
import sys

def test(did_pass):
     """ Print the result of a test. """
     linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
     if did_pass:
         msg = "Test at line {0} ok.".format(linenum)
     else:
         msg = ("Test at line {0} FAILED.".format(linenum))
     print(msg)


def test_suite():
     # bias
     test(analysis("The moon landing was fake.")[0] == "Extreme Bias Detected: The text appears to be highly opinionated, indicating that there may be little to no factual basis. This indicates that the text may be strongly subjective, reflecting personal beliefs or persuasive rhetoric.")
     test(analysis("Only people who are completely misinformed would think differently.")[0] == "High Bias Detected: The text appears to be mostly subjective, but may still contain some factual elements. This indicates that the text may contain opinion-driven arguments or interpretations.")
     test(analysis("Pizza can have pineapple.")[0] == "Extremely Low Bias Detected: The text appears to be highly objective, indicating that it is almost entirely based on factual statements with minimal or no subjectivity.")
     test(analysis("Movies are fun, but books always have a better story.")[0] == "Low Bias Detected: The text appears to be mostly objective, with minor subjective elements. This indicates that the text focuses on facts but may include slight opinions or interpretations.")
     test(analysis("I like spring.")[0] == "Extremely Low Bias Detected: The text appears to be highly objective, indicating that it is almost entirely based on factual statements with minimal or no subjectivity.")
     test(analysis("1 + 1 = 2")[0] == "Extremely Low Bias Detected: The text appears to be highly objective, indicating that it is almost entirely based on factual statements with minimal or no subjectivity.")
     test(analysis("123456789")[0] == "Extremely Low Bias Detected: The text appears to be highly objective, indicating that it is almost entirely based on factual statements with minimal or no subjectivity.")
     test(analysis("Fall is the best season")[0] == "Low Bias Detected: The text appears to be mostly objective, with minor subjective elements. This indicates that the text focuses on facts but may include slight opinions or interpretations.")

     # polarity
     test(analysis("I love unicorns so much")[1] == "Positive Polarity Detected: The text appears to express an overall positive sentiment, indicating that the overall connotation of words and phrases shows optimism, approval, or favorable opinions.")
     test(analysis("The moon landing was fake")[1] == "Negative Polarity Detected: The text appears to express an overall negative sentiment, indicating that the overall connotation of words and phrases shows criticism, disapproval, or unfavorable opinions.")
     test(analysis("Watching reality TV is a complete waste of time.")[1] == "Neutral Polarity Detected: The text does not appear to strongly express positive or negative sentiment. This indicates that text may be factual, balanced, or emotionally neutral.")
     test(analysis("Donald duck is the worst disney character ever")[1] == "Negative Polarity Detected: The text appears to express an overall negative sentiment, indicating that the overall connotation of words and phrases shows criticism, disapproval, or unfavorable opinions.")
     test(analysis("I'm going to fist fight ai in the back of a Denny's")[1] == "Neutral Polarity Detected: The text does not appear to strongly express positive or negative sentiment. This indicates that text may be factual, balanced, or emotionally neutral.")
     test(analysis("This is completely depressing.")[1] == "Negative Polarity Detected: The text appears to express an overall negative sentiment, indicating that the overall connotation of words and phrases shows criticism, disapproval, or unfavorable opinions.")
     test(analysis("I'm so proud of what I’ve accomplished.")[1] == "Positive Polarity Detected: The text appears to express an overall positive sentiment, indicating that the overall connotation of words and phrases shows optimism, approval, or favorable opinions.")
     test(analysis("I have lunch on the moon.")[1] == "Neutral Polarity Detected: The text does not appear to strongly express positive or negative sentiment. This indicates that text may be factual, balanced, or emotionally neutral.")

     # fake news
     test(analysis("Nathan Barker teaches at Southern Utah University.")[2] == "AI detected 'Real' News: The AI model classifies the input as likely factual or trustworthy, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
     test(analysis("The moon landing was fake.")[2] == "AI detected 'Fake' News: The AI model classifies the input as likely false or misleading, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
     test(analysis("Cats are the best animal.")[2] == "AI detected 'Real' News: The AI model classifies the input as likely factual or trustworthy, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
     test(analysis("Aliens control the stock market.")[2] == "AI detected 'Fake' News: The AI model classifies the input as likely false or misleading, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
     test(analysis("The human body has 206 bones.")[2] == "AI detected 'Real' News: The AI model classifies the input as likely factual or trustworthy, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
     test(analysis("COVID-19 is caused by eating spicy food.")[2] == "AI detected 'Fake' News: The AI model classifies the input as likely false or misleading, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
     test(analysis("The moon affects tides on Earth.")[2] == "AI detected 'Real' News: The AI model classifies the input as likely factual or trustworthy, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
     test(analysis("Dinosaurs built the pyramids.")[2] == "AI detected 'Fake' News: The AI model classifies the input as likely false or misleading, but the reasoning behind this decision is unknown to us. As the model's criteria are not transparent, the accuracy and reliability of this label cannot be verified. This label should not be taken as definitive proof of accuracy, so please verify the credibility of this output.")
    
#test() 
test_suite()