import math
import os
class Config:
    num_targets = int(os.environ['LAB3_NUM_TARGETS'])
    num_measurements_per_target = int(os.environ['LAB3_NUM_MEASUREMENTS_PER_TARGET'])
    num_tracked_params = int(os.environ['LAB3_NUM_TRACKED_PARAMS'])
    num_computed_params_per_target = int(os.environ['LAB3_NUM_COMPUTED_PARAMS_PER_TARGET'])
    L = float(os.environ['LAB3_L'])
    m = int(os.environ['LAB3_M'])
    v = int(os.environ['LAB3_V'])

config = Config
n = config.num_targets + config.num_measurements_per_target + config.num_tracked_params + config.num_computed_params_per_target
# а) Расчёт структурных параметров:
# 1) число модулей программного средства
k = n / 8
# 2) если k >> 8
if k > 8:
    i = (math.log2(n) / 3) + 1  # Число уровней
    K = n / 8 + n / (8 ** 2)  # Число модулей для многоуровневой структуры
else:
    K = k
# б) Расчет длины программы
N = 220 * K + K * math.log2(K)
# в) Расчет объема программного обеспечения
V = K * 220 * math.log2(48)
# г) Расчет количества команд ассемблера
P = 3 * N / 8
# д) Расчет календарного времени программирования
Tk_days = 3 * N / (8 * config.m * config.v)  # в днях
Tk_hours = Tk_days * 8  # в часы
# е) Расчет потенциального количества ошибок
B = V / 3000
# ж) Расчет начальной надежности ПО (времени наработки на отказ)
tn = Tk_hours / (2 * math.log(B))
print(f"а) Расчёт структурных параметров:")
print(f"число модулей программного средства k = {k:.2f}")
print(f"б) Расчет длины программы N = {N:.2f}")
print(f"в) Расчет объема программного обеспечения V = {V:.2f}")
print(f"г) Расчет количества команд ассемблера P = {P:.2f}")
print(f"д) Расчет календарного времени программирования Tk в днях = {Tk_days:.2f}")
print(f"д) Расчет календарного времени программирования Tk в часах = {Tk_hours:.2f}")
print(f"е) Расчет потенциального количества ошибок B = {B:.0f}")
print(f"ж) Расчет начальной надежности ПО (времени наработки на отказ) tн = {tn:.2f} часов")