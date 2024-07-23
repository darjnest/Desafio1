
print("Advertencia: Asegúrese de que los valores ingresados sean positivos y que el gasto total no exceda los ingresos.")


# Solicitar parámetros de entrada
suscripcion = float(input("Ingrese el precio de suscripción: "))
if suscripcion <= 0:
    print("Error: El precio de suscripción debe ser mayor que 0.")
    exit()

numero_usuarios = int(input("Ingrese el número de usuarios: "))
if numero_usuarios < 0:
    print("Error: El número de usuarios no puede ser negativo.")
    exit()

gasto_total = float(input("Ingrese el gasto total: "))
if gasto_total < 0:
    print("Error: El gasto total no puede ser negativo.")
    exit()

# Calcular las utilidades
utilidades = (suscripcion * numero_usuarios) - gasto_total

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades:.2f}")