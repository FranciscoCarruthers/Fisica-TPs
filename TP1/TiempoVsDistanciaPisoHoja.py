import matplotlib.pyplot as plt
import numpy as np
from TiempoVsDistanciaPapelPapel import get_data_from_file, change_data_to_distance, change_ms_to_s, plot_distance_vs_time

# plot the data from hoja 2PB_O
plt.figure()
for i in range(2, 4):
    ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/piso hoja/2PB_O-{i}.csv')
    distance = change_data_to_distance(sensor_data) - 15
    s = change_ms_to_s(ms) - 0.4
    plot_distance_vs_time(s[3:15], distance[3:15], 0.44, i)
plt.tight_layout()
plt.savefig('TP1/TiempoVsDistanciaPisoHoja2PB_O.png')
plt.show()


# plot the data from hoja M_OP
plt.figure()
for i in range(2, 4):
    ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/piso hoja/M_OP-{i}.csv')
    distance = change_data_to_distance(sensor_data) - 15
    s = change_ms_to_s(ms) - 0.5
    plot_distance_vs_time(s[4:16], distance[4:16], 0.44, i)
plt.tight_layout()
plt.savefig('TP1/TiempoVsDistanciaPisoHojaM_OP.png')
plt.show()


# plot the data from hoja V_2P
plt.figure()
for i in range(1, 3):
    ms, sensor_data = get_data_from_file(f'TP1/Mediciones Fisica/piso hoja/V_2P-{i}.csv')
    distance = change_data_to_distance(sensor_data) - 15
    s = change_ms_to_s(ms) - 0.4
    plot_distance_vs_time(s[3:16], distance[3:16], 0.44, i+1)
plt.tight_layout()
plt.savefig('TP1/TiempoVsDistanciaPisoHojaV_2P.png')
plt.show()