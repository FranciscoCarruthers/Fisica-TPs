import numpy as np
import matplotlib.pyplot as plt
from pendulo import get_data, plot_all_trayectories

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
    errores = []
    for i in range(len(thetas)):
        error = 0
        for j in range(len(thetas[i])):
            error += (thetas[i][j] - pequenas_y[j])**2
        errores.append(error)
    print(f'Error cuadratico medio con angulo = {angulo}:', errores[0])

    #Grafico
    for i in range(len(thetas)):
        plt.plot(thetas[i], label=f"Ángulo inicial = {angles[i]}°")
    plt.plot(pequenas_y, label='Pequeñas oscilaciones')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Ángulo (°)')
    # plt.title('Ángulo vs Tiempo')
    plt.legend()
    plt.show()

    
    

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

    plot_all_trayectories([theta10[50:300]], [9.4])
    plot_all_trayectories([theta15[83:333]], [15.2])
    plot_all_trayectories([theta25[70:320]], [25])
    plot_all_trayectories([theta45[89:338]], [43])
    plot_all_trayectories([theta60[73:310]], [52.4])
        # [theta10[56:306]]), 
                            # theta15[86:336], theta25[73:326], theta45[99:349], theta60[:250]])
    


if __name__ == '__main__':
    main()