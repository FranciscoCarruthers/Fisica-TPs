import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

distancia = [10,15,20,25,30]
sensor = np.array([(574 + 598) / 2, (837 + 841) / 2, (1097 + 1101) / 2, (1338 + 1395) / 2, (1676 + 1679) / 2])

# Definimos los erroresx
def func(x, a, b):
    return a * x + b

popt, pcov = sp.optimize.curve_fit(func, sensor, distancia)

# Calcular la recta de tendencia
tendencia = func(sensor, *popt)

error_sensor = 1    # Error en el eje X (datos del sensor)
error_distancia = 0.1  # Error en el eje Y (distancia)

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.errorbar(sensor, distancia, xerr=error_sensor, yerr=error_distancia, fmt='o', color='blue', ecolor='blue', elinewidth=2, capsize=10, label='Datos de Sensor vs Distancia')

# Graficar la recta de tendencia
plt.plot(sensor, tendencia, color='cyan', label='Tendencia con error $\pm$0.5')

# Graficar las bandas de desviación
plt.fill_between(sensor, tendencia - 0.5, tendencia + 0.5, color='cyan', alpha=0.2)

plt.title('Relación de Conversión entre Datos del Sensor y Distancias con Error en ambos ejes')
plt.xlabel('Datos del Sensor')
plt.ylabel('Distancia')
plt.legend()
plt.grid(True)
plt.savefig('Calibracion.png')
plt.show()

# Calcular la pendiente y ordenada al origen
pendiente = popt[0]
ordenada_origen = popt[1]

print("Pendiente:", pendiente)
print("Ordenada al origen:", ordenada_origen)

# Calcular para 600
distancia_600 = func(600, *popt)
print("Distancia para 600:", distancia_600)
