import numpy as np
import matplotlib.pyplot as plt

# PapelPapelM_O

acel_prom_PPM_O = 3.91 /100 #± 0.33 m /s^2
m_chiquita_PPM_O = 72
M_grande_PPM_O = 109 + 134

# PapelPapelM_OP

acel_prom_PPM_OP = 24.80 /100 #± 4.80 m /s^2
m_chiquita_PPM_OP = 72 + 23
M_grande_PPM_OP = 109 + 134

# PapelPapelV_O

acel_prom_PPV_O = 76.97 /100 #± 4.80 m /s^2
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
plt.savefig('TP1/scatter_aceleraciones.png')
plt.show()