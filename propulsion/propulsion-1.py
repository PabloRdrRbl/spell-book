import numpy as np
import matplotlib.pyplot as plt

# 1 - Despegue + postcombustión

s_to = 437 # m
t_r = 3 # s
k_to = 1.2
g = 9.8 # m/s2
c_lmax = 2
alpha = 0.8775
beta = 1
rho = 1.225 # kg/m3

WS = np.linspace(0, 10000, 500)

TW1 = ((((k_to ** 2) + (beta ** 2)) / (rho * g * alpha * c_lmax)) *
     (1 / (s_to - t_r * k_to * np.sqrt(2 / (rho * c_lmax) * WS))) * WS)

#################################################

# 2 - Crucero supersónico + postcombustión

beta = 0.78
alpha = 0.4792
k_1 = 0.27
q = 47477.09 # Pa
c_do = 0.028

WS = np.linspace(0, 10000, 500)

TW2 = (beta / alpha) * (k_1 * (beta / q) * WS + c_do / ((beta / q) * WS))

#################################################

# 3 - Giro 1 + postcombustión

beta = 0.78
alpha = 0.784
k_1 = 0.288
q = 54016.86 # Pa
n = 5
c_do = 0.028

WS = np.linspace(0, 10000, 500)

TW3 = ((beta / alpha) *
      (k_1 * (beta / q) * (n ** 2) * WS + c_do / ((beta / q) * WS)))

#################################################

# 4 - Giro 2 + postcombustión

beta = 0.78
alpha = 0.52
k_1 = 0.218
q = 17091.27 # Pa
n = 5
c_do = 0.028

WS = np.linspace(0, 10000, 500)

TW4 = ((beta / alpha) *
      (k_1 * (beta / q) * (n ** 2) * WS + c_do / ((beta / q) * WS)))

#################################################

# 5 - Aceleleración + postcombustión

beta = 0.78
alpha = 0.6
k_1 = 0.27
q = 30384.128 # Pa
c_do = 0.028
g = 9.8 # m/s2
v_f = 484.958 # m/s
v_i = 242.49 # m/s
dt = 50 # s

WS = np.linspace(0, 10000, 500)

TW5 = ((beta / alpha) * (k_1 * (beta / q) * WS + c_do / ((beta / q) * WS) +
      ((1 / g) * ((v_f - v_i) / dt))))

#################################################

# 6 - Aterrizaje - Sin reversa

beta = 0.56
rho = 1.225 # kg/m3
g = 9.8 # m/s2
e_l = 0.8
mi_l = 0.18
c_lmax = 1.2
k_l = 1.15
t_fr = 3 # s
s_l = 457

A =  ((beta / (rho * g * e_l)) *
     np.log(1 + (e_l / ((mi_l * c_lmax) / (k_l ** 2)))))

B = (t_fr * k_l * np.sqrt((2 * beta) / (rho * c_lmax)))

C = - s_l

# son dos rectas verticales

WS_6a = (((- B + np.sqrt((B ** 2) - 4 * A * C)) / (2 * A)) ** 2)
WS_6b = (((- B - np.sqrt((B ** 2) - 4 * A * C)) / (2 * A)) ** 2)

print(A, B, C, "\n"*6)
print(WS_6a, WS_6b, "\n"*6)

#################################################

# 7 - Máximo Mach + postcombustión

alpha = 0.633
beta = 0.78
k_1 = 0.324
q = 42709.62
c_do = 0.028

TW7 = ((beta / alpha) * (k_1 * (beta / q) * WS + (c_do / ((beta / q) * WS))))

#################################################

# plotting

fig, ax = plt.subplots(figsize=(6, 6), dpi=100)

ax.set_ylim(0, 3)
ax.set_xlim(0, 10000)

ax.set_title(r'Problema propulsión')
ax.set_xlabel(r'$\frac{W_{TO}}{S}$')
ax.set_ylabel(r'$\frac{T_{SL}}{W_{TO}}$')

ax.plot(WS, TW1, 'r-', linewidth=3, label='Mission 1')
ax.plot(WS, TW2, 'b-', linewidth=3, label='Mission 2')
ax.plot(WS, TW3, 'g-', linewidth=3, label='Mission 3')
ax.plot(WS, TW4, 'k-', linewidth=3, label='Mission 4')
ax.plot(WS, TW5, 'r--', linewidth=3, label='Mission 5')

yy = np.linspace(0, 10, 100)

ax.axvline(WS_6a, color ='b', linestyle='--', linewidth=3, label='Mission 6a')
ax.axvline(WS_6b, color ='g', linestyle='--', linewidth=3, label='Mission 6b')

ax.plot(WS, TW7, 'k--', linewidth=3, label='Mission 7')

ax.legend(loc='lower right')

plt.savefig('propulsion-1.svg')
plt.show()
