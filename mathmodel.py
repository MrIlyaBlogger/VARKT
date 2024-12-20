import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from math import sin

# для графика
#time = 160
time = 279
sep_time = 77
V = []
H = []

# параметры ракеты и планеты
m0 = 18338
M = 65804
P = 1117580  # 1167580  #
C = 0.9
# ro = 1.293
# S = constants.pi * ((6.6 / 2) ** 2)
g = 1.00034 * constants.g
k = (M - m0) / time
alpha = 0.82 * constants.pi / 360
M2 = 19800
P2 = 259970  # 309970  #

# термодинамика
p0 = 101325
air_M = 0.029
R = 8.314
air_T = 293


def mas(t):
    if t <= sep_time:
        return M - k * t
    return M2 - k * (t - sep_time)
    # return M - k * t


def a_after_sep(t):
    if t == 0:
        return 0
    else:
        return (((-mas(t) * g * 2) / (C * ro(t)) + (2 * P2) / (C * ro(t)) + mas(t) ** 2 / (
                t * C * ro(t)) ** 2) ** 0.5 - mas(t) / (t * C * ro(t))) / t


def v(t):
    if t == 0:
        return 0
    elif t <= sep_time:
        return (((-mas(t) * g * 2) / (C * ro(t)) + (2 * P) / (C * ro(t)) + mas(t) ** 2 / (
                t * C * ro(t)) ** 2) ** 0.5 - mas(t) / (t * C * ro(t)))
    else:
        return V[-1] + a_after_sep(t)


def h(t):
    if t == 0:
        return 0
    elif t <= sep_time:
        return V[-1] * sin(alpha * t) + H[-1]
    else:
        return H[-1]


def ro(t):
    if t == 0:
        return p0 * air_M / (R * air_T)
    p = p0 * 2.7182 ** (-air_M * g * H[-1] / (R * air_T))
    return p * air_M / (R * air_T)


X = np.arange(0, time, 1)
for i in X:
    V.append(v(i))
    H.append(h(i))

plt.figure(figsize=(7, 6))
plt.plot(X, V, '-r', label="v(t) модель")
#plt.plot(X, H, '-r', label="model")
plt.legend()
plt.title("График значений симуляции")
plt.xlabel("Время (с)")
plt.ylabel("Наземная скорость (м/c)")
plt.grid(True)
plt.show()
