import unittest
from main import calculate


class TestMain(unittest.TestCase):

    def test_simple_example(self):
        """
        Test that the returned solution is correct for simple problem.
        """
        usb_size = 1
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling_kid.avi', 605, 12)
        ]

        expected = (
            22,
            {'yodeling_kid.avi', 'sad_pepe_compilation.gif'}
            )
        result = calculate(usb_size, memes)

        self.assertEqual(expected, result)

    def test_one_better_than_more(self):
        """
        Test that the returned solution is correct for simple problem.
        """
        usb_size = 1
        memes = [
            ('hello_there.jpg', 140, 5),
            ('grumpy_cat.jpg', 50, 6),
            ('rollsafe.jpg', 105, 2),
            ('sad_pepe_compilation.gif', 310, 4),
            ('yodeling_kid.avi', 405, 3),
            ('I_am_the_Senate.gif', 1004, 21)
        ]

        expected = (
            21,
            {'I_am_the_Senate.gif'}
            )
        result = calculate(usb_size, memes)

        self.assertEqual(expected, result)

    def test_more_better_than_one(self):
        """
        Test that the returned solution is correct for simple problem.
        """
        usb_size = 1
        memes = [
            ('hello_there.jpg', 140, 5),
            ('grumpy_cat.jpg', 50, 6),
            ('rollsafe.jpg', 105, 2),
            ('sad_pepe_compilation.gif', 310, 4),
            ('yodeling_kid.avi', 405, 3),
            ('I_am_the_Senate.gif', 1004, 19)
        ]

        expected = (
            20,
            {
                'hello_there.jpg',
                'grumpy_cat.jpg',
                'rollsafe.jpg',
                'sad_pepe_compilation.gif',
                'yodeling_kid.avi'
            }
            )
        result = calculate(usb_size, memes)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
