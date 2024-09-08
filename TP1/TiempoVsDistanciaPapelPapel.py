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
    plt.errorbar(s, distance, yerr=sigma_y, fmt='o', color=colores[i-2])
    plt.plot(s, distance, color=colores[i-2], label=f'Medicion {i-1}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Distancia (cm)')
    plt.legend()


if __name__ == '__main__':
        
    # plot the data from papel boligoma papel M_O
    plt.figure()
    for i in range(2, 4):
        ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/papel boligoma papel/M_O-{i}.csv')
        distance = change_data_to_distance(sensor_data) - 15
        s = change_ms_to_s(ms) - 0.5
        plot_distance_vs_time(s[6:28], distance[6:28], 0.44, i)
    plt.tight_layout()
    plt.savefig('TP1/TiempoVsDistanciaPapelPapelM_O.png')
    plt.show()


    # plot the data from papel boligmoa papel M_OP
    plt.figure()
    for i in range(2, 4):
        ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/papel boligoma papel/M_OP-{i}.csv')
        distance = change_data_to_distance(sensor_data) - 15
        s = change_ms_to_s(ms) - 0.5
        plot_distance_vs_time(s[6:19], distance[6:19], 0.44, i)
    plt.tight_layout()
    # plt.savefig('TP1/TiempoVsDistanciaPapelPapelM_OP.png')
    plt.show()


    # plot the data from papel boligmoa papel V_O
    plt.figure()
    for i in range(2, 4):
        ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/papel boligoma papel/V_O-{i}.csv')
        distance = change_data_to_distance(sensor_data) - 15
        s = change_ms_to_s(ms) - 0.7
        plot_distance_vs_time(s[6:14], distance[6:14], 0.44, i)
    plt.tight_layout()
    # plt.savefig('TP1/TiempoVsDistanciaPapelPapelV_O.png')
    plt.show()