import numpy as np


class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_plus(self):
        ans = self.a + self.b
        return ans

    def calc_minus(self):
        ans = self.a - self.b
        return ans

    def calc_times(self):
        ans = self.a * self.b
        return ans

    def calc_division(self):
        ans = self.a / self.b
        return ans

    def calc_mod(self):
        ans = self.a % self.b
        return ans

    def calc_score(self):
        han = self.a
        fu = self.b
        # チートイツ
        if fu != 25:
            fu = np.ceil(self.b/10) * 10
        # 点数分岐
        if han >= 13:
            return 32000
        elif han >= 11:
            return 24000
        elif han >= 8:
            return 16000
        elif han >= 6:
            return 12000
        elif han == 5:
            return 8000
        elif han == 4:
            if fu == 40:
                return 8000
            elif fu == 30:
                return 7700
            elif fu == 20:
                return 5200
