"""
This module provides unit tests for the english_to_french() and french_to_english() functions
in the translator module.
"""

import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """
    Test English to French translation
    """
    def test1(self):
        """
        Test that English text is correctly translated to French
        """
        # Test 'Hello' returns 'Bonjour'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test 'Hello' does not return 'Hello'
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # Test 'None' returns empty string
        self.assertNotEqual(english_to_french("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)

class TestF2E(unittest.TestCase):
    """ 
    Test French to English translation
    """
    def test1(self):
        """
        Test that French text is correctly translated to English
        """
        # Test 'Bonjour' returns 'Hello'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Test 'Bonjour' does not return 'Bonjour'
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        # Test 'None' returns empty string
        self.assertNotEqual(french_to_english("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(french_to_english(0), 0)

unittest.main()
