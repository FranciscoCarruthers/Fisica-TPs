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

    # Grafico
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

def plot_real_vs_theory(thetas, angles=[10, 15, 25, 45, 60]):
    # colors = ['r', 'b', 'g', 'y', 'm']
    w = (1/(2*np.pi * np.sqrt(41.9/9.8)))
    pequenas_x = np.linspace(0, 250, 250)
    pequenas_y = []
    angulo = angles[0]
    for i in range (len(pequenas_x)):
        pequenas_y.append(-(angulo)*np.cos(w*pequenas_x[i]))
    
    # Grafico
    for i in range(len(thetas)):
        plt.plot(thetas[i], label=f"Ángulo inicial = 10°")
    plt.plot(pequenas_y, label='Predicción teórica')
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

    # Cálculo de errores cuadráticos medios (ejemplo basado en tu código)
    errores_cuadrarico_medio = []
    errores_cuadrarico_medio.append(plot_all_trayectories([theta10[1:251]], [9.4]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta15[28:278]], [15.2]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta25[8:258]], [25.3]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta45[32:282]], [43]))
    errores_cuadrarico_medio.append(plot_all_trayectories([theta60[0:250]], [53]))

    # Preparación de datos de ajuste
    errores_cuadrarico_medio_2 = [0, errores_cuadrarico_medio[0], errores_cuadrarico_medio[1], 
                                errores_cuadrarico_medio[2], errores_cuadrarico_medio[4], 0]
    params, p_cov = curve_fit(cuadratic_func, [0, 10, 15, 25, 55, 360], errores_cuadrarico_medio_2, 
                            sigma=0.05 * np.ones_like(errores_cuadrarico_medio_2), absolute_sigma=True)

    # Configuración de los ángulos
    angulos = [10, 15, 25, 45, 55]

    # Gráfica de barras para los errores cuadráticos medios
    plt.bar(angulos, errores_cuadrarico_medio, label="Datos experimentales")
    plt.hlines(40, 0, 60, 'black', linestyle='-', label="Error máximo tolerado")  # Línea horizontal para el error máximo tolerado

    # Configuración de la línea de ajuste cuadrático en rojo
    x = np.linspace(0, 60, 100)
    plt.plot(x, cuadratic_func(x, *params), 'r-', label="Ajuste cuadrático")  # Línea en rojo con etiqueta

    # Calcular la intersección entre el ajuste cuadrático y el error máximo tolerado (y = 40)
    error_maximo = 40
    # Resolución de la ecuación cuadrática: a * x^2 + b * x + (c - error_maximo) = 0
    a, b, c = params
    coeficientes = [a, b, c - error_maximo]
    intersecciones = np.roots(coeficientes)

    # Filtrar las soluciones reales que están en el rango del gráfico
    intersecciones = [sol.real for sol in intersecciones if sol.imag == 0 and 0 <= sol.real <= 60]

    # Agregar las líneas punteadas en las intersecciones
    for interseccion in intersecciones:
        plt.vlines(interseccion, 0, error_maximo, colors='gray', linestyles='--')  # Línea vertical punteada
        plt.plot(interseccion, error_maximo, 'ko')  # Punto de intersección

    # Configuraciones del gráfico
    plt.ylim(0, 80)
    plt.xlim(0, 60)
    plt.xticks(angulos)
    plt.xlabel('Ángulo inicial (°)')
    plt.ylabel('Error cuadrático medio')
    plt.legend()
    plt.grid(True)  # Activar grid
    plt.savefig('TP2/peq_oscilaciones.png')  # Guardar la imagen
    plt.show()

    # Gráfico de comparación entre los datos experimentales y la teoría

    plot_real_vs_theory([theta10[1:251]], [9.4])




if __name__ == '__main__':
    main()