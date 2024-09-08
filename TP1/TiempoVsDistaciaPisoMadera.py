import matplotlib.pyplot as plt
import numpy as np
from TiempoVsDistanciaPapelPapel import get_data_from_file, change_data_to_distance, change_ms_to_s, plot_distance_vs_time

# plot the data from madera 2PB_O
plt.figure()
for i in range(2, 4):
    ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/piso madera/2PB_O-{i}.csv')
    distance = change_data_to_distance(sensor_data) - 15
    s = change_ms_to_s(ms) - 0.7
    plot_distance_vs_time(s[6:14], distance[6:14], 0.44, i)
plt.tight_layout()
plt.savefig('TP1/TiempoVsDistanciaPisoMadera2PB_O.png')
plt.show()


# plot the data from madera MPB_O
plt.figure()
for i in range(2, 4):
    ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/piso madera/MPB_O-{i}.csv')
    distance = change_data_to_distance(sensor_data) - 15
    s = change_ms_to_s(ms) - 1.5
    plot_distance_vs_time(s[14:27], distance[14:27], 0.44, i)
plt.tight_layout()
plt.savefig('TP1/TiempoVsDistanciaPisoMaderaMPB_O.png')
plt.show()


# plot the data from madera V_2P
plt.figure()
for i in range(2, 4):
    ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/piso madera/V_2P-{i}.csv')
    distance = change_data_to_distance(sensor_data) - 15
    s = change_ms_to_s(ms) - 0.4
    plot_distance_vs_time(s[3:13], distance[3:13], 0.44, i)
plt.tight_layout()
plt.savefig('TP1/TiempoVsDistanciaPisoMaderaV_2P.png')
plt.show()