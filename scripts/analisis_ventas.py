import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde la carpeta /datos
df = pd.read_csv("datos/ventas.csv", parse_dates=["fecha"])

# Calcular ventas totales
print("=== VENTAS TOTALES ===")
print(f"Total general: ${df['total'].sum():,.0f}")

# Producto más vendido por cantidad
print("\n=== PRODUCTO MÁS VENDIDO ===")
mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print(f"Producto más vendido: {mas_vendido}")

# Ventas agrupadas por mes
print("\n=== VENTAS POR MES ===")
df["mes"] = df["fecha"].dt.to_period("M")
ventas_mes = df.groupby("mes")["total"].sum()
print(ventas_mes)

# Gráfico de evolución de ventas por mes
ventas_mes.plot(kind="bar", title="Evolución de Ventas por Mes", color="steelblue")
plt.ylabel("Total ($)")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
plt.show()
print("Gráfico guardado en /resultados")
