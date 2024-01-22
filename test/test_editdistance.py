import unittest

class TestEditDistance(unittest.TestCase):
    def test_editdistance(self):
        import editdistance
        self.assertEqual(1, editdistance.eval('abc', 'aec'))

    def test_editdistance_criterion(self):
        import editdistance
        self.assertEqual(False, editdistance.eval_criterion('abcb', 'aeca', 1))
        self.assertEqual(True, editdistance.eval_criterion('abc', 'aec', 1))

if __name__ == '__main__':
    unittest.main()