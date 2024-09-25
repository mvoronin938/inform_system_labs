import math
import os

class Config:
    num_targets = int(os.environ['LAB3_NUM_TARGETS'])
    num_measurements_per_target = int(os.environ['LAB3_NUM_MEASUREMENTS_PER_TARGET'])
    num_tracked_params = int(os.environ['LAB3_NUM_TRACKED_PARAMS'])
    num_computed_params_per_target = int(os.environ['LAB3_NUM_COMPUTED_PARAMS_PER_TARGET'])
    L = float(os.environ['LAB3_L'])

config = Config

# минимальное число различных операндов
n = config.num_targets + config.num_measurements_per_target + config.num_tracked_params + config.num_computed_params_per_target

# потенциальный объем программы V*
V = (n + 2) * math.log2(n + 2)

# Расчет потенциального числа ошибок B
B = (V ** 2) / (3000 * config.L)

print(f"Потенциальный объем программы (V*): {V:.2f}")
print(f"Потенциальное число ошибок (B): {B:.0f}")