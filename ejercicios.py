# ============================
# Parte 1: Visualización con Matplotlib
# ============================

# 1. Gráfico de línea simple
# Escribe un programa que grafique la siguiente lista de valores:
# valores = [3, 7, 1, 5, 12]
# Agrega título, etiquetas de ejes y una cuadrícula.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

valores = [3, 7, 1, 5, 12]
plt.figure()
plt.plot(valores, marker='o')
plt.title('Gráfico de Línea Simple')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.show()

# 2. Gráfico de barras
# Grafica la cantidad de estudiantes en 5 cursos:
# cursos = ['A', 'B', 'C', 'D', 'E']
# cantidad = [30, 25, 40, 20, 35]

cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]
plt.figure()
plt.bar(cursos, cantidad, color='skyblue')
plt.title('Estudiantes por Curso')
plt.xlabel('Curso')
plt.ylabel('Cantidad de Estudiantes')
plt.grid(axis='y')
plt.show()

# 3. Gráfico de dispersión (scatter plot)
# Genera dos listas de números aleatorios de 50 elementos y haz un gráfico de dispersión.

x = np.random.rand(50)
y = np.random.rand(50)
plt.figure()
plt.scatter(x, y, color='green')
plt.title('Gráfico de Dispersión')
plt.xlabel('X aleatorio')
plt.ylabel('Y aleatorio')
plt.grid(True)
plt.show()

# 4. Subplots
# Crea un figure con 2 subgráficos:
# • Uno con una línea senoidal.
# • Otro con una función cuadrática.

x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = x**2

fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(x, y1)
axs[0].set_title('Función Senoidal')
axs[1].plot(x, y2, color='red')
axs[1].set_title('Función Cuadrática')
plt.tight_layout()
plt.show()

# ============================
# Parte 2: Cálculos y gráficos con NumPy
# ============================

# 5. Generar datos y graficar una función
# Usa np.linspace() para generar valores x entre -10 y 10, y grafica y = x² - 3x + 2.

x = np.linspace(-10, 10, 200)
y = x**2 - 3*x + 2
plt.figure()
plt.plot(x, y)
plt.title('y = x² - 3x + 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# 6. Comparación de funciones
# En el mismo gráfico, traza las funciones sin(x) y cos(x) para x entre 0 y 2π.

x = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.title('Funciones Seno y Coseno')
plt.xlabel('x')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

# 7. Operaciones entre arrays
# Genera dos vectores de 100 valores aleatorios entre 0 y 100 y calcula:
# • La suma total.
# • El valor máximo.
# • La desviación estándar.

a = np.random.randint(0, 100, 100)
b = np.random.randint(0, 100, 100)

suma_total = np.sum(a + b)
valor_maximo = np.max(np.concatenate([a, b]))
desviacion_std = np.std(np.concatenate([a, b]))

print(f"Suma total: {suma_total}")
print(f"Valor máximo: {valor_maximo}")
print(f"Desviación estándar: {desviacion_std:.2f}")

# 8. Histograma con NumPy
# Genera 1000 números aleatorios con distribución normal y muestra un histograma con plt.hist().

datos = np.random.randn(1000)
plt.figure()
plt.hist(datos, bins=30, color='purple', edgecolor='black')
plt.title('Histograma de Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# ============================
# Parte 3: Lectura de archivos con Pandas
# ============================

# Supone que el archivo datos_ventas.csv está en el mismo directorio que este script.
# Columnas esperadas: Producto, Ventas, Precio, Fecha

# 9. Cargar archivo
# Carga el archivo y muestra las primeras 5 filas con head().

df = pd.read_csv('datos_ventas.csv')
print(df.head())

# 10. Estadísticas básicas
# Muestra:
# • Total de ventas (Ventas.sum())
# • Promedio de precio
# • Producto más vendido

total_ventas = df['Ventas'].sum()
promedio_precio = df['Precio'].mean()
producto_mas_vendido = df.groupby('Producto')['Ventas'].sum().idxmax()

print(f"Total de ventas: {total_ventas}")
print(f"Promedio de precio: {promedio_precio:.2f}")
print(f"Producto más vendido: {producto_mas_vendido}")

# 11. Filtrar datos
# Muestra solo los productos vendidos en el mes de enero (Fecha empieza por 2025-01).

df_enero = df[df['Fecha'].str.startswith('2025-01')]
print(df_enero)

# 12. Gráfica de barras con Pandas
# Grafica la cantidad total vendida por producto. (Agrupa por Producto y suma las ventas)

ventas_por_producto = df.groupby('Producto')['Ventas'].sum()
ventas_por_producto.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Ventas Totales por Producto')
plt.xlabel('Producto')
plt.ylabel('Total Vendido')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
