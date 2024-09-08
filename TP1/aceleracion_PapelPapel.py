import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 'Fisica-TPs/TP1/Mediciones Fisica/papel boligoma papel/M_O.csv'

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


ms2 , sensor_data2 = get_data_from_file('TP1/Mediciones Fisica/papel boligoma papel/M_O-2.csv')
ms3 , sensor_data3 = get_data_from_file('TP1/Mediciones Fisica/papel boligoma papel/M_O-3.csv')

tiempo2 = change_ms_to_s(ms2[5:26]) - 0.5
posicion2 = change_data_to_distance(sensor_data2[5:26]) - 15
errores_y2 = np.full(len(posicion2), 0.44)

tiempo3 = change_ms_to_s(ms3[5:26]) - 0.5
posicion3 = change_data_to_distance(sensor_data3[5:26]) - 15
errores_y3 = np.full(len(posicion3), 0.44)

# Definir la función cuadrática con v_0 = 0
def modelo_cuadratico(t, a, v_0, x_0):
    return a * t**2 + v_0 * t +  x_0

# ajustar las curvas
popt2, pcov2 = curve_fit(modelo_cuadratico, tiempo2[1:-1], posicion2[1:-1], sigma=errores_y2[1:-1], absolute_sigma=True)
popt3, pcov3 = curve_fit(modelo_cuadratico, tiempo3[1:-1], posicion3[1:-1], sigma=errores_y3[1:-1], absolute_sigma=True)


# obtener los coeficientes ajustados y sus errores

a_opt2, v_0_opt2, x_0_opt2 = popt2
errores2 = np.sqrt(np.diag(pcov2))

a_opt3, v_0_opt3, x_0_opt3 = popt3
errores3 = np.sqrt(np.diag(pcov3))


print(f"Aceleración a: {a_opt2:.2f} ± {errores2[0]:.2f} m /s^2")
print(f"Velocidad inicial v_0: {v_0_opt2:.2f} ± {errores2[1]:.2f} m /s")
print(f"Posición inicial x_0: {x_0_opt2:.2f} ± {errores2[2]:.2f}m")

# Graficar los datos y el ajuste

t_ajuste2 = np.linspace(tiempo2.min(), tiempo2.max(), 100)
plt.errorbar(tiempo2, posicion2, yerr=errores_y2, fmt='o', color = 'red')

t_ajuste3 = np.linspace(tiempo3.min(), tiempo3.max(), 100)
plt.errorbar(tiempo3, posicion3, yerr=errores_y3, fmt='o', color = 'blue')

plt.plot(t_ajuste2, modelo_cuadratico(t_ajuste2, *popt2), 'r', label=f'Ajuste cuadrático 1')
plt.plot(t_ajuste3, modelo_cuadratico(t_ajuste3, *popt3), 'b', label=f'Ajuste cuadrático 2')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [cm]')
plt.legend()
plt.savefig('TP1/ajuste2_PapelPapelM_O.png')
plt.show()

# 'Fisica-TPs/TP1/Mediciones Fisica/papel boligoma papel/M_OP.csv'

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

# Definir la función cuadrática 
def modelo_cuadratico(t, a, v_0, x_0):
    return a * t**2 + v_0 * t +  x_0


# ajustar las curvas
popt2, pcov2 = curve_fit(modelo_cuadratico, tiempo2[1:-2], posicion2[1:-2], sigma=errores_y2[1:-2], absolute_sigma=True)
popt3, pcov3 = curve_fit(modelo_cuadratico, tiempo3[1:-1], posicion3[1:-1], sigma=errores_y3[1:-1], absolute_sigma=True)

# obtener los coeficientes ajustados y sus errores

a_opt2, v_0_opt2, x_0_opt2 = popt2
errores2 = np.sqrt(np.diag(pcov2))

a_opt3, v_0_opt3, x_0_opt3 = popt3
errores3 = np.sqrt(np.diag(pcov3))


print(f"Aceleración a: {a_opt2:.2f} ± {errores2[0]:.2f} m /s^2")
print(f"Velocidad inicial v_0: {v_0_opt2:.2f} ± {errores2[1]:.2f} m /s")
print(f"Posición inicial x_0: {x_0_opt2:.2f} ± {errores2[2]:.2f}m")

# Graficar los datos y el ajuste

t_ajuste2 = np.linspace(tiempo2.min(), tiempo2.max(), 100)
plt.errorbar(tiempo2, posicion2, yerr=errores_y2, fmt='o', color = 'red')

t_ajuste3 = np.linspace(tiempo3.min(), tiempo3.max(), 100)
plt.errorbar(tiempo3, posicion3, yerr=errores_y3, fmt='o', color = 'blue')

plt.plot(t_ajuste2, modelo_cuadratico(t_ajuste2, *popt2), 'r', label=f'Ajuste cuadrático 1')
plt.plot(t_ajuste3, modelo_cuadratico(t_ajuste3, *popt3), 'b', label=f'Ajuste cuadrático 2')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [cm]')
plt.legend()
plt.savefig('TP1/ajuste2_PapelPapelM_OP.png')
plt.show()

# 'Fisica-TPs/TP1/Mediciones Fisica/papel boligoma papel/V_O.csv'

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


ms2 , sensor_data2 = get_data_from_file('TP1/Mediciones Fisica/papel boligoma papel/V_O-2.csv')
ms3 , sensor_data3 = get_data_from_file('TP1/Mediciones Fisica/papel boligoma papel/V_O-3.csv')

tiempo2 = change_ms_to_s(ms2[6:15]) - 0.7
posicion2 = change_data_to_distance(sensor_data2[6:15]) - 15
errores_y2 = np.full(len(posicion2), 0.44)

tiempo3 = change_ms_to_s(ms3[6:15]) - 0.7
posicion3 = change_data_to_distance(sensor_data3[6:15]) - 15
errores_y3 = np.full(len(posicion3), 0.44)

# Definir la función cuadrática
def modelo_cuadratico(t, a, v_0, x_0):
    return a * t**2 + v_0 * t +  x_0

# ajustar las curvas
popt2, pcov2 = curve_fit(modelo_cuadratico, tiempo2[:-1], posicion2[:-1], sigma=errores_y2[:-1], absolute_sigma=True)
popt3, pcov3 = curve_fit(modelo_cuadratico, tiempo3[:-1], posicion3[:-1], sigma=errores_y3[:-1], absolute_sigma=True)

# obtener los coeficientes ajustados y sus errores

a_opt2, v_0_opt2, x_0_opt2 = popt2
errores2 = np.sqrt(np.diag(pcov2))

a_opt3, v_0_opt3, x_0_opt3 = popt3
errores3 = np.sqrt(np.diag(pcov3))

print(f"Aceleración a: {a_opt2:.2f} ± {errores2[0]:.2f} m /s^2")
print(f"Velocidad inicial v_0: {v_0_opt2:.2f} ± {errores2[1]:.2f} m /s")
print(f"Posición inicial x_0: {x_0_opt2:.2f} ± {errores2[2]:.2f}m")

# Graficar los datos y el ajuste

t_ajuste2 = np.linspace(tiempo2.min(), tiempo2.max(), 100)
plt.errorbar(tiempo2, posicion2, yerr=errores_y2, fmt='o', color = 'red')

t_ajuste3 = np.linspace(tiempo3.min(), tiempo3.max(), 100)
plt.errorbar(tiempo3, posicion3, yerr=errores_y3, fmt='o', color = 'blue')


plt.plot(t_ajuste2, modelo_cuadratico(t_ajuste2, *popt2), 'r', label=f'Ajuste cuadrático 1')
plt.plot(t_ajuste3, modelo_cuadratico(t_ajuste3, *popt3), 'b', label=f'Ajuste cuadrático 2')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [cm]')
plt.legend()
plt.savefig('TP1/aceleracion_PapelPapelV_O.png')
plt.show()