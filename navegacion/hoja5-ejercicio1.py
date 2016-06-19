import numpy as np
import matplotlib.pyplot as plt

m = 0.8
V = 1

fc = 10
fm = 1

t = np.linspace(0, 3, 500)

v_c = V * np.cos(2 * np.pi * fc * t)
v_m = V * m * np.cos(2 * np.pi * fm * t)

signal = V * (1 + m * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t)

evol1 = V * (1 + m * np.cos(2 * np.pi * fm * t))
evol2 = - evol1

fig1, ax1 = plt.subplots()

ax1.set_title(r'Ejercicio 1 (apartado $b$)- Hoja 5')
ax1.set_xlabel(r'time $(t)$')
ax1.set_ylabel(r'voltage $(V)$')

ax1.plot(t, v_c, 'g', label='portadora')
ax1.plot(t, v_m, 'b', label='moduladora')
ax1.plot(t, signal, 'r', label='señal modulada')
ax1.plot(t, evol1, 'k--', label='evolventes')
ax1.plot(t, evol2, 'k--')

ax1.legend(loc='upper right')

#############################

m = 0.5

t = np.linspace(0, 0.5, 500)

# mantengo V, fc, fm, v_c, v_m, signal y las evolventes

v_bl = V * m * np.cos(2 * np.pi * fm * t) * np.cos(2 * np.pi * fc * t)

v_bls = V  * m / 2 * np.cos(2 * np.pi * (fc + fm) * t)
v_bli = V  * m / 2 * np.cos(2 * np.pi * (fc - fm) * t)

fig2, ax2 = plt.subplots()

ax2.set_title(r'Ejercicio 1 (apartado $d$)- Hoja 5')
ax2.set_xlabel(r'time $(t)$')
ax2.set_ylabel(r'voltage $(V)$')

ax2.plot(t, signal, 'r', label='señal modulada')
ax2.plot(t, v_bls, 'g', linewidth=1.5, label='banda lateral superior')
ax2.plot(t, v_bli, 'b', linewidth=1.5, label='banda lateral inferior')
ax2.plot(t, v_bl, 'k--', linewidth=2, label='bandas laterales')

ax2.legend(loc='upper right')

fig1.savefig('fig1.svg')
fig2.savefig('fig2.svg')

plt.show()
