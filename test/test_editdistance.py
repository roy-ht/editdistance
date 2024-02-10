import unittest
import random


class TestEditDistance(unittest.TestCase):
    def test_editdistance(self):
        import editdistance
        self.assertEqual(1, editdistance.eval('abc', 'aec'))

    def test_dp_editdistance(self):
        from editdistance.bycython import eval_dp
        self.assertEqual(3, eval_dp('bbb', 'a'))
        self.assertEqual(3, eval_dp('a', 'bbb'))

    def test_dp_vs_default(self):
        for _ in range(10):
            import editdistance
            from editdistance.bycython import eval_dp
            seq1 = random.choices([0, 1, 2], k=random.randint(10, 50))
            seq2 = random.choices([0, 1, 2], k=random.randint(10, 50))

            self.assertEqual(editdistance.eval(seq1, seq2), eval_dp(seq1, seq2))
    

if __name__ == '__main__':
    unittest.main()