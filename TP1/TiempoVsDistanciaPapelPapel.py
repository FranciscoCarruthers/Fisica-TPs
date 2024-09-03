import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# 'Fisica-TPs/TP1/Mediciones Fisica/papel boligoma papel/M_O-1.csv'

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

def plot_distance_vs_time(s, distance, sigma_y, i):
    colores = ['r', 'b']
    plt.errorbar(s, distance, yerr=sigma_y, fmt='o', color=colores[i-2], label='Datos experimentales')
    plt.plot(s, distance, color=colores[i-2])
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Distancia (cm)')


# plot the data from papel boligoma papel M_O
plt.figure()
plt.suptitle('Distancia vs Tiempo')
for i in range(2, 4):
    # plt.subplot(2, 1, i-1)
    path = f'Fisica-TPs/TP1/Mediciones Fisica/papel boligoma papel/M_O-{i}.csv'
    ms, sensor_data = get_data_from_file(path)
    distance = change_data_to_distance(sensor_data) - 15
    s = change_ms_to_s(ms) - 0.5
    plot_distance_vs_time(s[6:], distance[6:], 0.44, i)
plt.tight_layout()
plt.show()