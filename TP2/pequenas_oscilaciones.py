import numpy as np
import matplotlib.pyplot as plt
from pendulo import get_data, plot_all_trayectories

def plot_all_trayectories(thetas, angles=[10, 15, 25, 45, 60]):
    # colors = ['r', 'b', 'g', 'y', 'm']
    w = (1/(2*np.pi * np.sqrt(42/9.30)))
    # a = 10
    # b = 
    # pequeñas_oscilaciones = a np.cos(wt) + b np.sin(wt)
    pequeñas_oscilaciones = 10 * np.cos(w)
    pequenas_x = np.linspace(0, 250, 250)
    pequenas_y = []
    for i in range (len(pequenas_x)):
        pequenas_y.append(-60*np.cos(w*pequenas_x[i]))
    

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

    plot_all_trayectories([theta60[:250]], [60])
        # [theta10[56:306]]), 
                            # theta15[86:336], theta25[73:326], theta45[99:349], theta60[:250]])


if __name__ == '__main__':
    main()