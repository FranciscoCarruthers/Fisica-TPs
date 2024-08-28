import matplotlib.pyplot as plt
import numpy as np

distancia = [10,15,20,25,30]
sensor = [(574+598)/2 , (837+841)/2, (1097+1101)/2, (1338+1395)/2,(1676+1679)/2] 

# Definimos los errores
error_sensor = 1    # Error en el eje X (datos del sensor)
error_distancia = 0.1  # Error en el eje Y (distancia)

# Calcular la recta de tendencia
coef = np.polyfit(sensor, distancia, 1)
tendencia = np.polyval(coef, sensor)

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
plt.show()