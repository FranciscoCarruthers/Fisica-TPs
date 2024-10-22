from operator import index

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

def plot_trayectory(theta, angle):
    plt.plot(theta, label=f"Ángulo inicial = {angle}°")
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Ángulo (°)')
    plt.title('Ángulo vs Tiempo')
    plt.legend()
    plt.show()

def plot_all_trayectories(thetas, angles=[10, 15, 25, 45, 60]):
    # colors = ['r', 'b', 'g', 'y', 'm']
    for i in range(len(thetas)):
        plt.plot(thetas[i], label=f"Ángulo inicial = {angles[i]}°")
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Ángulo (°)')
    # plt.title('Ángulo vs Tiempo')
    plt.legend()
    plt.savefig('angulos.png')
    plt.show()

def plot_trayectory_based_lenght(thetas):
    colors = ['r', 'b', 'black']
    lengths = [15, 26, 42]
    for theta in thetas:
        theta_plot = theta[:250]
        plt.plot(theta_plot, label=f"L = {lengths[thetas.index(theta)]} cm", color=colors[thetas.index(theta)])
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Ángulo (°)')
    # plt.title('Ángulo vs Largo')
    plt.legend()
    plt.savefig('largo.png')
    plt.show()

def plot_trayectory_based_weight(thetas):
    colors = ['r', 'b', 'black']
    weights = [5, 23, 72]
    for theta in thetas:
        theta_plot = theta [:200]
        plt.plot(theta_plot, label=f"m = {weights[thetas.index(theta)]} g", color=colors[thetas.index(theta)])
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Ángulo (°)')
    # plt.title('Ángulo vs Peso')
    plt.legend()
    plt.savefig('peso.png')
    plt.show()



def main():
    t10, r10, theta10 = get_data('TP2/tp2_fisica - angulo_10.csv')
    t15, r15, theta15 = get_data('TP2/tp2_fisica - angulo_15.csv')
    t25, r25, theta25 = get_data('TP2/tp2_fisica - caso_base.csv')
    t45, r45, theta45 = get_data('TP2/tp2_fisica - angulo_45.csv')
    t60, r60, theta60 = get_data('TP2/tp2_fisica - angulo_60.csv')

    # plot_trayectory(theta10[56:], 10)
    # plot_trayectory(theta15[86:], 15)
    # plot_trayectory(theta25[73:], 25)
    # plot_trayectory(theta45[99:], 45)
    # plot_trayectory(theta60, 60)

    # print(theta60.index(max(theta60)))
    # print(theta10.index(max(theta10)))
    # print(theta15.index(max(theta15)))
    # print(theta25.index(max(theta25)))
    # print(theta45.index(max(theta45)))

    plot_all_trayectories([theta10[56:306], theta15[86:336], theta25[73:326], theta45[99:349], theta60[:250]])

    tl15, rl15, thetal15 = get_data('TP2/tp2_fisica - largo_15.csv')
    tl26, rl26, thetal26 = get_data('TP2/tp2_fisica - largo_26.csv')

    # print(thetal15.index(max(thetal15)))
    # print(thetal26.index(max(thetal26)))

    plot_trayectory_based_lenght([thetal15[46:], thetal26[51:], theta25[70:]])

    tw5, rw5, thetaw5 = get_data('TP2/tp2_fisica - peso_madera.csv')
    tw72, rw72, thetaw72 = get_data('TP2/tp2_fisica - peso_oro.csv')

    # print(thetaw5.index(max(thetaw5)))
    # print(thetaw72.index(max(thetaw72)))

    plot_trayectory_based_weight([thetaw5[30:], theta25[70:], thetaw72[179:]])

if __name__ == '__main__':
    main()
