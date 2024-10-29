import numpy as np
import matplotlib.pyplot as plt
from pendulo import get_data, plot_all_trayectories
from scipy.optimize import curve_fit

def plot_all_trayectories(thetas, angles=[10, 15, 25, 45, 60]):
    # colors = ['r', 'b', 'g', 'y', 'm']
    w = (1/(2*np.pi * np.sqrt(41.9/9.8)))
    # a = 10
    # b = 
    # pequeñas_oscilaciones = a np.cos(wt) + b np.sin(wt)
    # pequeñas_oscilaciones = 10 * np.cos(w)
    pequenas_x = np.linspace(0, 250, 250)
    pequenas_y = []
    angulo = angles[0]
    for i in range (len(pequenas_x)):
        pequenas_y.append(-(angulo)*np.cos(w*pequenas_x[i]))
    
    # Calculo de error cuadratico medio
    errores = 0
    for i in range(len(thetas)):
        error = 0
        for j in range(len(thetas[i])):
            error += (thetas[i][j] - pequenas_y[j])**2
        errores = error / len(thetas[i])
    print(f'Error cuadratico medio con angulo = {angulo}:', errores)

    #Grafico
    # for i in range(len(thetas)):
    #     plt.plot(thetas[i], label=f"Ángulo inicial = {angles[i]}°")
    # plt.plot(pequenas_y, label='Pequeñas oscilaciones')
    # plt.xlabel('Tiempo (ms)')
    # plt.ylabel('Ángulo (°)')
    # # plt.title('Ángulo vs Tiempo')
    # plt.legend()
    # # plt.show()

    return errores

def cuadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

def main():
    t10, r10, theta10 = get_data('TP2/tp2_fisica - angulo_10.csv')
    t15, r15, theta15 = get_data('TP2/tp2_fisica - angulo_15.csv')
    t25, r25, theta25 = get_data('TP2/tp2_fisica - caso_base.csv')
    t45, r45, theta45 = get_data('TP2/tp2_fisica - angulo_45.csv')
    t60, r60, theta60 = get_data('TP2/tp2_fisica - angulo_60.csv')
    
    # print(theta10.index(min(theta10)))
    # print(theta15.index(min(theta15)))
    # print(theta25.index(min(theta25)))
    # print(theta45.index(min(theta45)))
    # print(theta60.index(min(theta60)))

    # print(theta15[83])
    # print(theta45[89])
    # print(theta60[73])

    errores_cuadrarico_medio = []
    errores_cuadrarico_medio.append(plot_all_trayectories([theta10[1:251]], [9.4]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta15[28:278]], [15.2]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta25[8:258]], [25.3]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta45[32:282]], [43]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta60[0:250]], [53]))
        # [theta10[56:306]]), 
                            # theta15[86:336], theta25[73:326], theta45[99:349], theta60[:250]])

    # bar chart de los errores cuadraticos medios
    errores_cuadrarico_medio_2 = [0,errores_cuadrarico_medio[0], errores_cuadrarico_medio[1], errores_cuadrarico_medio[2], errores_cuadrarico_medio[4], 0]
    params, p_cov = curve_fit(cuadratic_func, [0,10,15,25,55,360], errores_cuadrarico_medio_2, sigma=0.05*np.ones_like(errores_cuadrarico_medio_2), absolute_sigma=True)
    angulos = [10, 15, 25, 45, 55]
    plt.bar(angulos, errores_cuadrarico_medio)
    x = np.linspace(0, 60, 100)
    plt.ylim(0, 80)
    plt.plot(x, cuadratic_func(np.array(x), *params))
    plt.xticks(angulos)
    plt.xlabel('Ángulo inicial (°)')
    plt.ylabel('Error cuadrático medio')
    plt.show()
    


if __name__ == '__main__':
    main()