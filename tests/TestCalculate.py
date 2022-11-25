import unittest
from originalproject.Calculate import Calculate


class TestCalculate(unittest.TestCase):
    def test_plus(self):
        calc = Calculate(1, 2)
        ans = calc.calc_plus()
        self.assertEqual(3, ans)

    def test_minus(self):
        calc = Calculate(1, 2)
        ans = calc.calc_minus()
        self.assertEqual(-1, ans)

    def test_times(self):
        calc = Calculate(1, 2)
        ans = calc.calc_times()
        self.assertEqual(2, ans)

    def test_division(self):
        calc = Calculate(4, 2)
        ans = calc.calc_division()
        self.assertEqual(2, ans)

    def test_mod(self):
        calc = Calculate(5, 2)
        ans = calc.calc_mod()
        self.assertEqual(1, ans)

    def test_score1(self):
        calc = Calculate(4, 30)
        ans = calc.calc_score()
        self.assertEqual(7700, ans)

    def test_score2(self):
        calc = Calculate(5, 45)
        ans = calc.calc_score()
        self.assertEqual(8000, ans)

    def test_score3(self):
        calc = Calculate(13, 30)
        ans = calc.calc_score()
        self.assertEqual(32000, ans)

    def test_score4(self):
        calc = Calculate(4, 20)
        ans = calc.calc_score()
        self.assertEqual(5200, ans)