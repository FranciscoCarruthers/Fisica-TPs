import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

distancia = np.array([10,15,20,25,30])
sensor = np.array([(574 + 598) / 2, (837 + 841) / 2, (1097 + 1101) / 2, (1338 + 1395) / 2, (1676 + 1679) / 2])

def ajuste_lineal(x, y, sigma_x, sigma_y):
    """
    Calcula la regresión lineal de los datos, y propaga sus incertezas.
    """
    X = np.mean(x) # valor medio de x_i: <x>
    Y = np.mean(y) # valor medio de y_i: <y>
    X2 = np.mean(x**2) # valor medio de x_i^2: <x^2>
    XY = np.mean(x*y) # valor medio de x_i*y_i: <xy>
    N = x.size # número de mediciones

    # lo defino en una variable separada porque aparece seguido en las cuentas:
    dX2 = X2 - X**2  # <x^2> - <x>^2

    # calculo los coeficientes de la regresión
    a = (XY-X*Y)/dX2
    b = (Y*X2 - XY*X)/dX2

    # derivadas de los coeficientes
    da_dx = ( (y - Y)*dX2 - 2*(x - X)*(XY - X*Y) ) / ( N * dX2**2 )
    da_dy = (x - X) / ( N * dX2 )

    db_dx = ( (2*x*Y - y*X - XY)*dX2 - 2*(x - X)*(Y*X2 - XY*X) ) / ( N * dX2**2 )
    db_dy = (X2 - x*X) / ( N * dX2 )

    # calculo la matriz de covarianza
    var_a = np.sum(da_dx**2 * sigma_x**2 + da_dy**2 * sigma_y**2) # cov(a, a)
    var_b = np.sum(db_dx**2 * sigma_x**2 + db_dy**2 * sigma_y**2) # cov(b, b)
    cov_ab = np.sum(da_dx * db_dx * sigma_x**2 + da_dy * db_dy * sigma_y**2)  # cov(a, b)
    cov_matrix = np.asarray([[var_a, cov_ab], [cov_ab, var_b]])

    return a, b, cov_matrix


def lineal_ajustada(x, a, b, sigma_x, cov):
    """
    Evalúa la regresión lineal con parámetros de ajustes `a` y `b`,
    y propaga las incertezas a partir de `sigma_x` y la matriz de covarianza `cov`.
    """
    y = a*x + b
    sigma_y = ( a**2 * sigma_x**2 + x**2 * cov[0, 0] + cov[1, 1] + 2*x*cov[0, 1] )**0.5
    return y, sigma_y

sigma_sensor = 18    # Error en el eje X (datos del sensor)
sigma_distancia = 0.2  # Error en el eje Y (distancia)

v, d0, cov = ajuste_lineal(sensor, distancia, sigma_sensor, sigma_distancia)

# la desviación estándar es la raiz de la varianza:
sigma_v = cov[0, 0]**0.5  # incerteza en v
sigma_d0 = cov[1, 1]**0.5 # incerteza en d_0

print(f'v={v} ± {sigma_v}')
print(f'd0={d0} ± {sigma_d0}')
print(f'cov(v, d0) = {cov[0, 1]}')

# grafico los datos junto al ajuste
x = np.linspace(500,1800, 100)
y = v * x + d0 # la recta de ajuste evaluada

x = np.linspace(0, 2000, 100) # evalúo a tiempos más largos que los que medí
y, sigma_y = lineal_ajustada(x, v, d0, sigma_sensor, cov) # recta de ajuste con incertezas

fig, ax = plt.subplots(1, 1, figsize=(6, 4))
ax.set_axisbelow(True)
ax.grid(True, c='gainsboro', linewidth=0.7)
ax.set_xlabel(r'$arduino$', size=15)
ax.set_ylabel(r'$d\,(cm)$', size=15)

ax.fill_between(x, y + sigma_y, y - sigma_y, color='tab:blue', alpha=0.5) # bandas de incerteza
ax.plot(x, y, color='tab:blue', label=r'$d(arduino) = \hat{v} arduino + \hat{d_0}$') # recta ajustada
ax.errorbar(sensor, distancia, xerr=sigma_sensor, yerr=sigma_distancia,
             fmt='o', c='navy', capsize=2, label='Datos', markersize=2) # datos con barras de incerteza
ax.legend()
plt.savefig('Fisica-TPs/TP1/Calibracion.png')
plt.show()

x600 = np.linspace(0, 600, 100) 
y600, sigma_y600 = lineal_ajustada(x600, v, d0, sigma_sensor, cov) 

# dónde me dice el modelo que el cuerpo va a estar
print(f'd(arduino=600) = {y600[-1]} ± {sigma_y600[-1]}')
