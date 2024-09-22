# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
# Solicitar el monto total y calcular el descuento con valor predeterminado (10%)
monto_total_1 = float(input("Ingresa el monto total de la primera compra: $"))
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1

# Solicitar el monto total y el porcentaje de descuento para la segunda compra
monto_total_2 = float(input("Ingresa el monto total de la segunda compra: $"))
porcentaje_descuento_2 = float(input("Ingresa el porcentaje de descuento para la segunda compra: "))
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - desc52uento_2

# Mostrar los resultados
print(f"\nMonto total 1: ${monto_total_1}")
print(f"Descuento 1 (10%): ${descuento_1}")
print(f"Monto final a pagar 1: ${monto_final_1}\n")

print(f"Monto total 2: ${monto_total_2}")
print(f"Descuento 2 ({porcentaje_descuento_2}%): ${descuento_2}")
print(f"Monto final a pagar 2: ${monto_final_2}")
