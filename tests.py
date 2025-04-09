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
     test(analysis("The moon landing was fake")[1] == "Neutral Polarity Detected: The text does not appear to strongly express positive or negative sentiment. This indicates that text may be factual, balanced, or emotionally neutral.")
     test(analysis("Watching reality TV is a complete waste of time.")[1] == "Negative Polarity Detected: The text appears to express an overall negative sentiment, indicating that the overall connotation of words and phrases shows criticism, disapproval, or unfavorable opinions.")
     test(analysis("Donald duck is the worst disney character ever")[1] == "Negative Polarity Detected: The text appears to express an overall negative sentiment, indicating that the overall connotation of words and phrases shows criticism, disapproval, or unfavorable opinions.")
     test(analysis("I'm going to fist fight ai in the back of a Denny's")[1] == "Neutral Polarity Detected: The text does not appear to strongly express positive or negative sentiment. This indicates that text may be factual, balanced, or emotionally neutral.")

     # fake news
    
#test() 
test_suite()