from operator import index

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def get_data(file_path):
    with open(file_path, 'r') as file:
        t, r, theta = [], [], []
        data = file.readlines()

        # Ignorar las primeras 2 líneas
        for line in data[2:]:
            line = line.strip()
            if line:  # Si la línea no está vacía
                line = line.split(',')
                t.append(float(line[0]))
                r.append(float(line[1]))
                theta.append(float(line[2]))

        return t, r, theta
    
def get_avg_periodo_time(times, theta):
    p = []
    for i in range(len(theta)):
        if abs(theta[i]) < 1:
            p.append(times[i])
    
    t = []
    for i in range(len(p)-2):
        t.append(p[i+2] - p[i])
    
    return np.mean(t)

def linear_func(x, a, b):
        return a * x + b

def cuadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

def get_gravedad_local(T, times, thetas):
    l = [0.15, 0.26, 0.42]
    T = []
    for i in range(len(thetas)):
        T.append(get_avg_periodo_time(times[i], thetas[i])**2)

    params, p_cov = curve_fit(linear_func, l, T, sigma=0.05*np.ones_like(T), absolute_sigma=True)
    plt.scatter(l, T)
    plt.plot(l, linear_func(np.array(l), *params))
    plt.xlabel('Largo (m)')
    plt.ylabel('$T^2$ ($s^2$)')
    plt.legend()
    plt.savefig('TP2/gravedad.png')
    plt.show()

    gravedad = 4 * np.pi**2 / params[0]
    error_gravedad = gravedad * np.sqrt(p_cov[0, 0]) / params[0]

    print('Gravedad local:', gravedad)
    print('Error de la gravedad:', error_gravedad)

# def plot_trayectory(theta, angle):
#     plt.plot(theta, label=f"Ángulo inicial = {angle}°")
#     plt.xlabel('Tiempo (ms)')
#     plt.ylabel('Ángulo (°)')
#     plt.title('Ángulo vs Tiempo')
#     plt.legend()
#     plt.show()

def plot_all_trayectories(times, thetas):
    angles=[10, 15, 25, 45, 55]
    # colors = ['r', 'b', 'g', 'y', 'm']
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    for theta in thetas:
        theta_plot = theta[:175]
        plt.plot(theta_plot, label=f"Ángulo inicial = {angles[thetas.index(theta)]}°")
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Ángulo (°)')
    # plt.title('Ángulo vs Tiempo')

    plt.subplot(1, 2, 2)
    w = []
    for i in range(len(thetas)):
        w.append(1/get_avg_periodo_time(times[i], thetas[i]))

    # calcular bien el error en y para cada w --> chat gpt
    params, p_cov = curve_fit(linear_func, angles, w, sigma=0.05*np.ones_like(w), absolute_sigma=True)
    x = np.linspace(0, 60, 100)
    plt.scatter(angles, w)
    # plt.fill_between(x, cuadratic_func(x, params[0] + np.sqrt(p_cov[0, 0]), params[1] + np.sqrt(p_cov[1, 1]), params[2] + np.sqrt(p_cov[2, 2])), cuadratic_func(x, params[0] - np.sqrt(p_cov[0, 0]), params[1] - np.sqrt(p_cov[1, 1]), params[2] - np.sqrt(p_cov[2, 2])), color='tab:blue', alpha=0.5)
    plt.plot(x, linear_func(np.array(x), *params))
    plt.errorbar(angles, w, yerr=0.01*np.ones_like(w), fmt='o', color='black')
    plt.xlabel('Ángulo inicial (°)')
    plt.ylabel('Frecuencia (Hz)')
    # plt.title('Frecuencia vs Ángulo inicial')
    plt.ylim(0.6,0.9)
    plt.legend()
    plt.savefig('TP2/angulos.png')
    plt.show()

def plot_trayectory_based_lenght(times, thetas):
    colors = ['r', 'b', 'black']
    lengths = [0.15, 0.26, 0.42]
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    for theta in thetas:
        theta_plot = theta[:175]
        plt.plot(theta_plot, label=f"L = {lengths[thetas.index(theta)]} m", color=colors[thetas.index(theta)])
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Ángulo (°)')
    # plt.title('Ángulo vs Largo')

    plt.subplot(1, 2, 2)
    w = []
    for i in range(len(thetas)):
        w.append(1/get_avg_periodo_time(times[i], thetas[i]))
    print(w)
    # calcular bien el error en y para cada w --> chat gpt

    params, p_cov = curve_fit(cuadratic_func, lengths, w, sigma=0.05*np.ones_like(w), absolute_sigma=True)
    x = np.linspace(0, 0.5, 100)
    plt.scatter(lengths, w)
    # plt.fill_between(x, cuadratic_func(x, params[0] + np.sqrt(p_cov[0, 0]), params[1] + np.sqrt(p_cov[1, 1]), params[2] + np.sqrt(p_cov[2, 2])), cuadratic_func(x, params[0] - np.sqrt(p_cov[0, 0]), params[1] - np.sqrt(p_cov[1, 1]), params[2] - np.sqrt(p_cov[2, 2])), color='tab:blue', alpha=0.5)
    plt.plot(x, cuadratic_func(np.array(x), *params))  
    plt.errorbar(lengths, w, yerr=0.01*np.ones_like(w), fmt='o', color='black')
    plt.xlabel('Largo (m)')
    plt.ylabel('Frecuencia (Hz)')
    plt.ylim(0.7,1.5)
    # plt.title('Frecuencia vs Largo')

    plt.legend()
    plt.savefig('TP2/largo.png')
    plt.show()

def plot_trayectory_based_weight(times, thetas):
    colors = ['r', 'b', 'black']
    weights = [5, 23, 72]
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    for theta in thetas:
        theta_plot = theta [:200]
        plt.plot(theta_plot, label=f"m = {weights[thetas.index(theta)]} g", color=colors[thetas.index(theta)])
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Ángulo (°)')
    # plt.title('Ángulo vs Peso')

    plt.subplot(1, 2, 2)
    w = []
    for i in range(len(thetas)):
        w.append(1/get_avg_periodo_time(times[i], thetas[i]))
    
    # calcular bien el error en y para cada w --> chat gpt
    params, p_cov = curve_fit(linear_func, weights[1:], w[1:], sigma=0.05*np.ones_like(w[1:]), absolute_sigma=True)
    x = np.linspace(0, 100, 100)
    plt.scatter(weights, w)
    # plt.fill_between(x, cuadratic_func(x, params[0] + np.sqrt(p_cov[0, 0]), params[1] + np.sqrt(p_cov[1, 1]), params[2] + np.sqrt(p_cov[2, 2])), cuadratic_func(x, params[0] - np.sqrt(p_cov[0, 0]), params[1] - np.sqrt(p_cov[1, 1]), params[2] - np.sqrt(p_cov[2, 2])), color='tab:blue', alpha=0.5)
    plt.plot(x, linear_func(np.array(x), *params))   
    plt.errorbar(weights, w, yerr=0.01*np.ones_like(w), fmt='o', color='black')
    plt.xlabel('Largo (m)')
    plt.ylabel('Frecuencia (Hz)')
    plt.ylim(0,1)
    # plt.title('Frecuencia vs masa')

    plt.legend()
    plt.savefig('TP2/peso.png')
    plt.show()



def main():
    t10, r10, theta10 = get_data('TP2/tp2_fisica - angulo_10.csv')
    t10 = [a-1 for a in t10]
    t15, r15, theta15 = get_data('TP2/tp2_fisica - angulo_15.csv')
    t15 = [a-1 for a in t15]
    t25, r25, theta25 = get_data('TP2/tp2_fisica - caso_base.csv')
    t25 = [a-1 for a in t25]
    t45, r45, theta45 = get_data('TP2/tp2_fisica - angulo_45.csv')
    t45 = [a-1 for a in t45]
    t55, r55, theta55 = get_data('TP2/tp2_fisica - angulo_60.csv')

    # plot_all_trayectories([t10,t15,t25,t45,t55],[theta10[21:], theta15[48:], theta25[29:], theta45[56:], theta55[17:]])

    tl15, rl15, thetal15 = get_data('TP2/tp2_fisica - largo_15.csv')
    tl15 = [a-1 for a in tl15]
    tl26, rl26, thetal26 = get_data('TP2/tp2_fisica - largo_26.csv')
    tl26 = [a-1 for a in tl26]

    plot_trayectory_based_lenght([tl15, tl26, t25], [thetal15[3:], thetal26[1:], theta25[7:]])

    tw5, rw5, thetaw5 = get_data('TP2/tp2_fisica - peso_madera.csv')
    tw72, rw72, thetaw72 = get_data('TP2/tp2_fisica - peso_oro.csv')

    # plot_trayectory_based_weight([tw5, t25, tw72],[thetaw5[2:], theta25[7:], thetaw72[9:]])

    # get_gravedad_local(1, [tl15, tl26, t25], [thetal15, thetal26, theta25])

if __name__ == '__main__':
    main()
