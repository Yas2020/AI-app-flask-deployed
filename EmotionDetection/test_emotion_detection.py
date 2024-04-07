import unittest

from emotion_detection import emotion_detector 

class TestStringMethods(unittest.TestCase):

    def test_emotion(self):
        test_cases = {
            'I am glad this happened': 'joy',
            'I am really mad about this': 'anger',
            'I feel disgusted just hearing about this': 'disgust',
            'I am so sad about this': 'sadness',
            'I am really afraid that this will happen': 'fear'
        }
        for text in test_cases:
            ans = emotion_detector(text)['dominant_emotion']
            self.assertEqual(ans, test_cases[text])


if __name__ == '__main__':
    unittest.main()