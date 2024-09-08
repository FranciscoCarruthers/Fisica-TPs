import numpy as np
import matplotlib.pyplot as plt

def get_dinamic_friction(mC, mG, a):
    return (a * (mC + mG) + mC * 9.8 ) / (mG * 9.8)

######## PapelPapel ########

# M_O, M_OP, V_O

ace = [3.91/100, 24.80/100, 76.97/100]
sigma_ace = [0.33/100, 4.80/100, 4.80/100]
m_chiquita = [72, 72 + 23, 72]
M_grande = [109 + 134, 109 + 134, 109]

fricciones = [get_dinamic_friction(m_chiquita[i], M_grande[i], ace[i]) for i in range(3)]

mG_mC = [M_grande[i] / m_chiquita[i] for i in range(3)]
plt.scatter(mG_mC, fricciones)
plt.ylim(0, 1)
plt.xlabel('M / m')
plt.ylabel('Fricción dinámica')
plt.savefig('TP1/ud_PapelPapel.png')
plt.show()

######## PisoPapel ########

# 2PB_O, M_OP, V_2P

ace = [29.03/100, 18.84/100, 17.65/100]
sigma_ace = [3.39/100, 2.51/100, 2.51/100]
m_chiquita = [72, 72 + 23, 23*2]
M_grande = [2*23 + 6 + 109, 109 + 134, 109]

fricciones = [get_dinamic_friction(m_chiquita[i], M_grande[i], ace[i]) for i in range(3)]

mG_mC = [M_grande[i] / m_chiquita[i] for i in range(3)]

plt.scatter(mG_mC, fricciones)
plt.ylim(0, 1)
plt.xlabel('M / m')
plt.ylabel('Fricción dinámica')
plt.savefig('TP1/ud_PisoPapel.png')
plt.show()


######## PisoMadera ########

# 2PB_O, MPB_O, V_2P

ace = [47.70/100, 10.81/100, 41.02/100]
sigma_ace = [3.39/100, 1.20/100, 2.51/100]
m_chiquita = [72, 72, 23*2]
M_grande = [2*23 + 6 + 109, 109 + 134 + 23 + 6, 109 + 23*2]

fricciones = [get_dinamic_friction(m_chiquita[i], M_grande[i], ace[i]) for i in range(3)]

mG_mC = [M_grande[i] / m_chiquita[i] for i in range(3)]

plt.scatter(mG_mC, fricciones)
plt.ylim(0, 1)
plt.xlabel('M / m')
plt.ylabel('Fricción dinámica')
plt.savefig('TP1/ud_PisoMadera.png')
plt.show()