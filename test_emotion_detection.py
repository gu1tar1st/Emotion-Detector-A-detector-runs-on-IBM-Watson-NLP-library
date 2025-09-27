import unittest
from EmotionDetection.emotion_detection import emotion_detector as eDetect


class test_emotion_detection(unittest.TestCase):
    def test_emotion1(self):
        statement1 = "I am glad this happened"
        self.assertEqual(eDetect(statement1), 'joy')

    def test_emotion2(self):
        statement2 = "I am really mad about this"
        self.assertEqual(eDetect(statement2), 'anger')

    def test_emotion3(self):
        statement3 = "I feel disgusted just hearing about this"
        self.assertEqual(eDetect(statement3), 'disgust')
    
    def test_emotion4(self):
        statement4 = "I am so sad about this"
        self.assertEqual(eDetect(statement4), 'sadness')

    def test_emotion5(self):
        statement5 = "I am really afraid that this will happen"
        self.assertEqual(eDetect(statement5), 'fear')


if __name__ == "__main__":
    unittest.main()