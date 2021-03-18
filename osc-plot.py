import matplotlib.pyplot as plt

import numpy as np

theta = np.pi/3
delta = 5.04*10**(-11)
x = 7.3*10**(23)
#p = {}
# ((np.sin(2*theta))**2)


def p(e):
    p = 1-0.846*(np.sin((((1266.93273*delta))/e)*x))**2
    return p


e = np.linspace(0, 10)  # num=10...números de pontos

"""
for e in range(0, 6):
    p[e] = (1-0.86*(np.sin((((1267*delta))/4*e)*x))**2)
"""
# plt.plot(p.values())
#plt.xlim(0, 6)
plt.ylim(0.15, 1.01)
plt.plot(e, p(e))
plt.show()