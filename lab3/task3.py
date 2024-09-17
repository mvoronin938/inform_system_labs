import os
import json
class Config:
    l = float(os.environ['L'])
    v_next = int(os.environ['V_NEXT'])
    r0 = int(os.environ['R0'])
    vol = json.loads(os.environ['VOL'])
    b = json.loads(os.environ['B'])

config = Config

R0 = config.r0
l = config.l
V = config.vol
B = config.b
v_next = config.v_next

def c1(l, r):
    return (1 / (l + r))

def c2(l, r):
    return (1 / (l * r))

def c3(l, r):
    return (1 / l) + (1 / r)

def Ri(R0, l, V, B, ind, cFn):
    return R0 * ((1 + (10 ** (-3)) * (sum(V[:ind]) - sum([b / cFn(l, R0) for b in B[:ind]]))))

def B_next(cFn):
    r1 = Ri(R0, l, V, B, 1, cFn)
    r2 = Ri(r1, l, V, B, 2, cFn)
    r3 = Ri(r2, l, V, B, 3, cFn)
    return cFn(l, r3) * v_next

print(f'b4 with c1: {B_next(c1)}\nb4 with c2: {B_next(c2)}\nb4 with c3: {B_next(c3)}')