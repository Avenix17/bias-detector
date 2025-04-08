import pytest
# grabs analysis method from script.py to unit test
from script import analysis, ClassBiased, ExBias, Positive, Neutral, Negative, Polarity, HighBias, LowBias, ModerateBias, ExLowBias

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

     # polarity
     test(analysis("I love unicorns so much")[1] == Positive.determine_polarity())
     test(analysis("The moon landing was fake")[1] == Neutral.determine_polarity())
     test(analysis("Watching reality TV is a complete waste of time.")[1] == Negative.determine_polarity())
     test(analysis("123456789") == None)

     # fake news
    
#test() 
test_suite()