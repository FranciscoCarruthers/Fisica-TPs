import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 'Fisica-TPs/TP1/Mediciones Fisica/papel boligoma papel/M_OP-1.csv'

def get_data_from_file(path):
    with open(path):
        ms, sensor_data = np.loadtxt(path, delimiter=',', unpack=True)
        return ms, sensor_data
    
sigma_sensor = 18    # Error en el eje X (datos del sensor)
sigma_distancia = 0.2  # Error en el eje Y (distancia)

def change_data_to_distance(sensor_data):
    return 0.0184 * sensor_data + -0.508

def change_ms_to_s(ms):
    ms = ms / 1000
    return ms


ms2 , sensor_data2 = get_data_from_file('TP1/Mediciones Fisica/papel boligoma papel/M_OP-2.csv')
ms3 , sensor_data3 = get_data_from_file('TP1/Mediciones Fisica/papel boligoma papel/M_OP-3.csv')

tiempo2 = change_ms_to_s(ms2[8:18]) - 0.5
posicion2 = change_data_to_distance(sensor_data2[8:18]) - 15
errores_y2 = np.full(len(posicion2), 0.44)

tiempo3 = change_ms_to_s(ms3[8:18]) - 0.5
posicion3 = change_data_to_distance(sensor_data3[8:18]) - 15
errores_y3 = np.full(len(posicion3), 0.44)

# Definir la función cuadrática con v_0 = 0
def modelo_cuadratico(t, a, v_0, x_0):
    return a * t**2 + v_0 * t +  x_0

# Ajustar la curva
# popt, pcov = curve_fit(modelo_cuadratico, tiempo, posicion, sigma=errores_y, absolute_sigma=True)

# ajustar las curvas
popt2, pcov2 = curve_fit(modelo_cuadratico, tiempo2[1:-2], posicion2[1:-2], sigma=errores_y2[1:-2], absolute_sigma=True)
popt3, pcov3 = curve_fit(modelo_cuadratico, tiempo3[1:-1], posicion3[1:-1], sigma=errores_y3[1:-1], absolute_sigma=True)

# Obtener los coeficientes ajustados y sus errores
# a_opt, v_0_opt, x_0_opt = popt
# errores = np.sqrt(np.diag(pcov))

# obtener los coeficientes ajustados y sus errores

a_opt2, v_0_opt2, x_0_opt2 = popt2
errores2 = np.sqrt(np.diag(pcov2))

a_opt3, v_0_opt3, x_0_opt3 = popt3
errores3 = np.sqrt(np.diag(pcov3))


# print(f"Aceleración a: {a_opt:.1f} ± {errores[0]:.1f} m /s^2")
# print(f"Velocidad inicial v_0: {v_0_opt:.0f} ± {errores[1]:.0f} m /s")
# print(f"Posición inicial x_0: {x_0_opt:.0f} ± {errores[2]:.0f}m")

# Graficar los datos y el ajuste
# t_ajuste = np.linspace(tiempo.min(), tiempo.max(), 100)
# plt.errorbar(tiempo, posicion, yerr=errores_y, fmt='o', label='Datos')

# Graficar los datos y el ajuste

t_ajuste2 = np.linspace(tiempo2.min(), tiempo2.max(), 100)
plt.errorbar(tiempo2, posicion2, yerr=errores_y2, fmt='o', color = 'red')

t_ajuste3 = np.linspace(tiempo3.min(), tiempo3.max(), 100)
plt.errorbar(tiempo3, posicion3, yerr=errores_y3, fmt='o', color = 'blue')

# plt.plot(t_ajuste, modelo_cuadratico(t_ajuste, *popt), 'r', label=f'Ajuste cuadrático')
plt.plot(t_ajuste2, modelo_cuadratico(t_ajuste2, *popt2), 'r', label=f'Ajuste cuadrático 1')
plt.plot(t_ajuste3, modelo_cuadratico(t_ajuste3, *popt3), 'b', label=f'Ajuste cuadrático 2')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m]')
plt.legend()
plt.show()

"""# Otra forma

Pueden también pensar en derivar numéricamente los datos. Ojo que para calcular derivadas con diferencias finitas necesitamos puntos a ambos lados de los datos.

Es decir, para la velocidad no miren los extremos y para aceleración también descarten los dos puntos de los extremos de cada lado.
"""

# Calcular la derivada numérica de los datos de posición respecto al tiempo
# velocidad = np.gradient(posicion, tiempo)[1:-1]
# tiempo = tiempo[1:-1]

# Calcular la derivada numérica de los datos de posición respecto al tiempo
velocidad2 = np.gradient(posicion2, tiempo2)[1:-1]
tiempo2 = tiempo2[1:-1]
velocidad3 = np.gradient(posicion3, tiempo3)[1:-1]
tiempo3 = tiempo3[1:-1]

# Graficar la derivada numérica
# plt.plot(tiempo, velocidad, 'b-', marker='o', label='Derivada numérica')
plt.plot(tiempo2, velocidad2, 'b-', marker='o', label='Derivada numérica 1', color='red')
plt.plot(tiempo3, velocidad3, 'b-', marker='o', label='Derivada numérica 2', color='blue')
plt.xlabel('Tiempo [s]')
plt.ylabel('Velocidad [m/s]')
plt.legend()
plt.show()

# Calcular la derivada numérica de los datos de posición respecto al tiempo
# aceleracion = np.gradient(velocidad, tiempo)
aceleracion2 = np.gradient(velocidad2, tiempo2)
aceleracion3 = np.gradient(velocidad3, tiempo3)

# Graficar la derivada numérica
plt.plot(tiempo2, aceleracion2, 'b-', marker='o', label='Derivada numérica 1', color='red')
plt.plot(tiempo3, aceleracion3, 'b-', marker='o', label='Derivada numérica 2', color='blue')
plt.xlabel('Tiempo [s]')
plt.ylabel(r'$ 2 \times$ Aceleración [$cm/s^2$]')
plt.legend()
plt.show()

# calcualar la aceleración promedio
acel_prom2 = np.mean(aceleracion2[:-3]) /2
acel_prom3 = np.mean(aceleracion3[:-3]) /2

m_chiquita = 72+23
M_grande = 109 + 134

# Graficar las aceleraciones promedio

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs=m_chiquita, ys=M_grande, zs=(acel_prom2+acel_prom3)/2)
ax.set_xlabel('Masa chica [g]')
ax.set_ylabel('Masa grande [g]')
ax.set_zlabel('Aceleración promedio')
plt.show()