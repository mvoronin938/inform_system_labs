import json


class ModelDM:
    def __init__(self) -> None:
        self.EPSILON = 0.01

    @property
    def table(self):
        with open('./lab2/table.json') as file:
            return json.load(file)

    @property
    def N(self):
        return len(self.table)

    @property
    def sum_xi(self):
        return sum([data['xi'] for data in self.table])

    @property
    def sum_ix(self):
        return sum([data['x'] * data['xi'] for data in self.table])

    def b_plus_1(self, B):
        return (B + 1) * self.sum_xi - self.sum_ix
  

    def nonlinear_equation(self):
        B_left = self.N
        B_right = 45
        idx = 0
        
        while idx < 2000 and ((B_right - B_left) > self.EPSILON):
            idx += 1
            B_mid = (B_left + B_right) / 2
            
            f_left = self.left_nonlinear_equation(B_left) - self.right_nonlinear_equation(B_left)
            f_mid = self.left_nonlinear_equation(B_mid) - self.right_nonlinear_equation(B_mid)

            if (f_left * f_mid) < 0:
                B_right = B_mid
            else:
                B_left = B_mid

        return int((B_left + B_right) / 2)


    def left_nonlinear_equation(self, B):
        result = 0
        for i in range(1, self.N + 1):
            try:
                equation = 1 / (B - i + 1)
            except ZeroDivisionError:
                continue
            else:
                result += equation

        return result

    def right_nonlinear_equation(self, B):
        numerator = self.N * self.sum_xi
        denominator = self.b_plus_1(B)
        equation = numerator / denominator

        return equation

    def alter_ratio_K(self, B):
        sum_bix = sum([(B - (data['x'] + 1) + 1) * data['xi'] for data in self.table])

        equation_2 = self.N / self.b_plus_1(B)
        equation_1 = self.N / sum_bix

        return equation_1, equation_2

    def ratio_K(self, B):
        return self.N / self.b_plus_1(B)


    def avg_time_x(self, B):
        K = self.ratio_K(B)
        return 1 / (K * (B - self.N))

    def test_time(self, B):
        K = self.ratio_K(B)
        left = 1 / K
        sum_ = sum([(1 / i) for i in range(1, (B - self.N) + 1)])

        return left * sum_



model_dm = ModelDM()
B = model_dm.nonlinear_equation()
K = model_dm.ratio_K(B)
X_n_1 = model_dm.avg_time_x(B)
tk = model_dm.test_time(B)

print('----')
print(f'B:\t{B}\nK:\t{K}\nXn+1:\t{X_n_1}\ntk:\t{tk}')
print('----')
