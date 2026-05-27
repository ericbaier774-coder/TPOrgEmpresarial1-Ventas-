import os
import time
import pandas as pd
import matplotlib.pyplot as plt

#Levanta el csv y lo convierte en un dataframe
def levantar_csv():
    try:
        df = pd.read_csv("datos/ventas.csv")
        if df.empty:
            raise ValueError("El archivo CSV está vacío.")
        return df
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'ventas.csv' en ../datos/")
        exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"Error inesperado al leer el CSV: {e}")
        exit(1)

#Guarda en variables los datos del dataframe.
def guardar_datos(df):
    productos = df['id'].tolist()
    ventas = df['sales_amount'].tolist()
    meses = df['sales_date'].tolist()
    return productos, ventas, meses

# Suma de todas la ventas
def ventas_totales(ventas):
    return sum(ventas)

# Producto más vendido
def max_producto(ventas, productos):
    index_max = ventas.index(max(ventas))
    return productos[index_max], ventas[index_max]

# Ventas mensuales
def ventas_mensuales(ventas, meses):
    ventas_por_mes = {}
    for i in range(len(meses)):
        mes = str(meses[i])[:7]  # Extrae solo "YYYY-MM" de "YYYY-MM-DD"
        if mes in ventas_por_mes:
            ventas_por_mes[mes] += ventas[i]
        else:
            ventas_por_mes[mes] = ventas[i]
    return ventas_por_mes

# Imprime ventas por mes
def imprimir_ventas_mensuales(ventas_por_mes):
    for mes, venta in ventas_por_mes.items():
        print(f"{mes}: {venta}")

#Grafico de ventas por producto
def grafico_ventas_productos(ventas, productos):
    plt.bar(productos, ventas)
    plt.xlabel('Productos')
    plt.ylabel('Ventas')
    plt.title('Ventas por Producto')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("resultados/grafico_ventas.png")
    plt.show()


# Crear carpeta de resultados si no existe
os.makedirs("resultados", exist_ok=True)

#Limpio consola y ejecuto funciones
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos...")
df = levantar_csv()
productos, ventas, meses = guardar_datos(df)
time.sleep(1)

# Imprime resultados de ventas totales
print("Calculando ventas totales...")
total_ventas = ventas_totales(ventas)
time.sleep(1)
print(f"Ventas totales: {total_ventas}")

# Imprime resultados del producto más vendido
print("Calculando producto más vendido...")
producto_max, venta_max = max_producto(ventas, productos)
print(f"Producto más vendido: {producto_max} con ventas de {venta_max}")

# Imprime resultados de ventas mensuales
print("Calculando ventas mensuales...")
ventas_por_mes = ventas_mensuales(ventas, meses)
time.sleep(1)
print("Ventas por mes:")
imprimir_ventas_mensuales(ventas_por_mes)

# Imprime gráfico de ventas por producto
print("Generando gráfico de ventas por producto...")
time.sleep(1)
grafico_ventas_productos(ventas, productos)
