import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from pendulo import get_data

def interpolate_and_calculate_error(t_exp, theta_exp, t_theo, theta_theo):
    # Interpolación para alinear el tiempo experimental con el teórico
    interp_func = interp1d(t_theo, theta_theo, kind='linear', bounds_error=False, fill_value='extrapolate')
    theta_theo_interp = interp_func(t_exp)
    
    # Cálculo del error cuadrático medio normalizado
    error = np.mean((theta_exp - theta_theo_interp) ** 2)
    error_normalized = error / max(abs(theta_theo_interp)) * 1  # Normalizado como porcentaje
    return error_normalized

def theoretical_oscillation(angulo, t, L=41.9, g=9.8):
    # Cálculo de la oscilación teórica
    w = (1 / (2 * np.pi * np.sqrt(L / g)))
    return -angulo * np.cos(w * t)

def main():
    # Cargar datos experimentales
    t10, _, theta10 = get_data('TP2/tp2_fisica - angulo_10.csv')
    t15, _, theta15 = get_data('TP2/tp2_fisica - angulo_15.csv')
    t25, _, theta25 = get_data('TP2/tp2_fisica - caso_base.csv')
    t45, _, theta45 = get_data('TP2/tp2_fisica - angulo_45.csv')
    t60, _, theta60 = get_data('TP2/tp2_fisica - angulo_60.csv')
    
    # Configurar incertezas
    d_angle = 2  # ± 2 grados
    d_L = 0.1  # ± 0.1 metros

    # Generar trayectorias teóricas considerando incertezas en ángulo y longitud
    t_theory = np.linspace(0, max(t10), len(t10))  # Tiempo teórico uniforme
    L_nominal = 41.9
    theta_theory_10 = theoretical_oscillation(10, t_theory, L=L_nominal)
    theta_theory_15 = theoretical_oscillation(15, t_theory, L=L_nominal)
    theta_theory_25 = theoretical_oscillation(25, t_theory, L=L_nominal)
    theta_theory_45 = theoretical_oscillation(45, t_theory, L=L_nominal)
    theta_theory_60 = theoretical_oscillation(60, t_theory, L=L_nominal)

    # Calcular errores normalizados
    error_10 = interpolate_and_calculate_error(t10, theta10, t_theory, theta_theory_10)
    error_15 = interpolate_and_calculate_error(t15, theta15, t_theory, theta_theory_15)
    error_25 = interpolate_and_calculate_error(t25, theta25, t_theory, theta_theory_25)
    error_45 = interpolate_and_calculate_error(t45, theta45, t_theory, theta_theory_45)
    error_60 = interpolate_and_calculate_error(t60, theta60, t_theory, theta_theory_60)

    # Calcular incertezas en el error por ángulo y longitud
    angles = np.array([10, 15, 25, 45, 60])
    errors = np.array([error_10, error_15, error_25, error_45, error_60])
    uncertainty_angle = (errors / angles) * d_angle
    uncertainty_length = (errors / L_nominal) * d_L
    total_uncertainty = np.sqrt(uncertainty_angle**2 + uncertainty_length**2)

    # Gráfico de dispersión con barras de error
    plt.figure(figsize=(8, 5))
    plt.errorbar(angles, errors, yerr=total_uncertainty, fmt='o', color='blue', label='Errores normalizados con incertezas')
    plt.axhline(40, color='red', linestyle='--', label='Error máximo tolerado (40%)')  # Línea de error máximo tolerado

    # Configuración del gráfico
    plt.xlabel('Ángulo inicial (°)', fontsize=12)
    plt.ylabel('Error normalizado (%)', fontsize=12)
    plt.title('Error normalizado vs Ángulo inicial con incertezas', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig('TP2/errores_normalizados_incertezas.png')  # Guardar la imagen
    plt.show()

if __name__ == '__main__':
    main()
