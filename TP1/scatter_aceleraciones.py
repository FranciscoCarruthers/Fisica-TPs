import numpy as np
import matplotlib.pyplot as plt

# PapelPapelM_O

acel_prom_PPM_O = 4.884117647058833
m_chiquita_PPM_O = 72
M_grande_PPM_O = 109 + 134

# PapelPapelM_OP

acel_prom_PPM_OP = 28.680999999999997
m_chiquita_PPM_OP = 72 + 23
M_grande_PPM_OP = 109 + 134

# PapelPapelV_O

acel_prom_PPV_O = 47.868750000000006
m_chiquita_PPV_O = 72
M_grande_PPV_O = 109

# graficar el scatter

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs=m_chiquita_PPM_O, ys=M_grande_PPM_O, zs=acel_prom_PPM_O, label='PapelPapelM_O')
ax.scatter(xs=m_chiquita_PPM_OP, ys=M_grande_PPM_OP, zs=acel_prom_PPM_OP, label='PapelPapelM_OP')
ax.scatter(xs=m_chiquita_PPV_O, ys=M_grande_PPV_O, zs=acel_prom_PPV_O, label='PapelPapelV_O')
ax.set_xlabel('Masa chica [g]')
ax.set_ylabel('Masa grande [g]')
ax.set_zlabel('Aceleración promedio [cm/s^2]')

plt.legend()

plt.show()