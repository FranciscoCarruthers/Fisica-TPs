import numpy as np
import matplotlib.pyplot as plt

def get_dinamic_friction(mC, mG, a):
    return (a * (mC + mG) + mC * 9800 ) / (mG * 9800)

######## PapelPapel ########

# M_O, M_OP, V_O

ace1 = [3.91, 24.80, 87.20]
print(np.mean(ace1))
sigma_ace1 = [0.33, 4.80, 7.20]
print(np.mean(sigma_ace1))
m_chiquita1 = [72, 72 + 23, 72]
M_grande1 = [109 + 134, 109 + 134, 109]

fricciones1 = [get_dinamic_friction(m_chiquita1[i], M_grande1[i], ace1[i]) for i in range(3)]

mG_mC1 = [M_grande1[i] / m_chiquita1[i] for i in range(3)]

print("PapelPapel")
print(fricciones1)
print(mG_mC1)

# plt.scatter(mG_mC1, fricciones1)
# plt.ylim(0, 1)
# plt.xlabel('M / m (g)')
# plt.ylabel('Coef. fricción dinámica')
# plt.savefig('TP1/ud_PapelPapel.png')
# plt.show()

######## PisoPapel ########

# 2PB_O, M_OP, V_2P

ace2 = [29.03, 18.84, 17.65]
print(np.mean(ace2))
sigma_ace2 = [3.39, 2.51, 2.51]
print(np.mean(sigma_ace2))
m_chiquita2 = [72, 72 + 23, 23*2]
M_grande2 = [2*23 + 6 + 109, 109 + 134, 109]

fricciones2 = [get_dinamic_friction(m_chiquita2[i], M_grande2[i], ace2[i]) for i in range(3)]

mG_mC2 = [M_grande2[i] / m_chiquita2[i] for i in range(3)]

print("PisoPapel")
print(fricciones2)
print(mG_mC2)

# plt.scatter(mG_mC2, fricciones2)
# plt.ylim(0, 1)
# plt.xlabel('M / m (g)')
# plt.ylabel('Coef. fricción dinámica')
# plt.savefig('TP1/ud_PisoPapel.png')
# plt.show()


######## PisoMadera ########

# 2PB_O, MPB_O, V_2P

ace3 = [47.70, 10.81, 41.02]
print(np.mean(ace3))
sigma_ace3 = [3.39, 1.20, 2.51]
print(np.mean(sigma_ace3))
m_chiquita3 = [72, 72, 23*2]
M_grande3 = [2*23 + 6 + 109, 109 + 134 + 23 + 6, 109 + 23*2]

fricciones3 = [get_dinamic_friction(m_chiquita3[i], M_grande3[i], ace3[i]) for i in range(3)]

mG_mC3 = [M_grande3[i] / m_chiquita3[i] for i in range(3)]

print("PisoMadera")
print(fricciones3)
print(mG_mC3)

# plt.scatter(mG_mC3, fricciones3)
# plt.ylim(0, 1)
# plt.xlabel('M / m (g)')
# plt.ylabel('Coef. fricción dinámica')
# plt.savefig('TP1/ud_PisoMadera.png')
# plt.show()


######## Combined ########

mean_fricciones = [np.mean(fricciones1), np.mean(fricciones2), np.mean(fricciones3)]
sigma_fricciones = [np.std(fricciones1), np.std(fricciones2), np.std(fricciones3)]

print("Combined")
print(mean_fricciones)
print(sigma_fricciones)

plt.errorbar(["Madera y trineo", "Papel y trineo", "Papel y papel"], mean_fricciones, yerr=sigma_fricciones, color='navy', capsize=12, elinewidth=10, fmt='o')
plt.ylim(0, 1)
plt.ylabel('Coef. fricción dinámica')
plt.savefig('TP1/ud_Combined.png')
plt.show()