import unittest
import warnings

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    # Disable Unverified HTTPS request and ResourceWarning: unclosed warnings
    def setUp(self):
        warnings.filterwarnings('ignore', message='Unverified HTTPS request')
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test1(self): 
        self.assertEqual(english_to_french(''), 'Text to be translated not provided') # Test for null input for english_to_french.

    def test2(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Test for the translation of the world 'Hello' and 'Bonjour'.        


class TestFrenchToEnglish(unittest.TestCase): 
    # Disable Unverified HTTPS request and ResourceWarning: unclosed warnings
    def setUp(self):
        warnings.filterwarnings('ignore', message='Unverified HTTPS request')
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)    

    def test1(self): 
        self.assertEqual(french_to_english(''), 'Text to be translated not provided') # Test for null input for frenchToEnglish

    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test for the translation of the world 'Bonjour' and 'Hello'.
        
unittest.main()