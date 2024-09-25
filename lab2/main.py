import os
import json


class Config:
    EPSILON = float(os.environ['LAB2_EPSILON'])
    B_RIGHT = float(os.environ['LAB2_B_RIGHT'])


class ModelDM:
    def __init__(self, config: Config) -> None:
        self.epsilon = config.EPSILON
        self.b_right = config.B_RIGHT

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
        b_left = self.N
        b_right = self.b_right

        for index in range(1000):
            if (b_right - b_left) > self.epsilon:
                break
            else:
                b_mid = (b_left + b_right) / 2
                
                f_left = self.left_nonlinear_equation(b_left) - self.right_nonlinear_equation(b_left)
                f_mid = self.left_nonlinear_equation(b_mid) - self.right_nonlinear_equation(b_mid)

                if (f_left * f_mid) < 0:
                    b_right = b_mid
                else:
                    b_left = b_mid

        return int((b_left + b_right) / 2)

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


config = Config()

model_dm = ModelDM(config)

B = model_dm.nonlinear_equation()
K = model_dm.ratio_K(B)

X_n_1 = model_dm.avg_time_x(B)
tk = model_dm.test_time(B)

print('----')
print(f'B:\t{B}\nK:\t{K}\nXn+1:\t{X_n_1}\ntk:\t{tk}')
print('----')


p = '[1, 2, 3]'

a = list(p)

print()