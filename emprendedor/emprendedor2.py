
# emprendedor2.py

# Advertencias al usuario
print("Advertencia: Asegúrese de que los valores ingresados sean positivos y que el gasto total no exceda los ingresos.")

# Solicitar parámetros de entrada
precio_suscripcion_normal = float(input("Ingrese el precio de suscripción normal: "))
if precio_suscripcion_normal <= 0:
    print("El precio de suscripción debe ser mayor que 0.")
    exit()

numero_usuarios_normal = int(input("Ingrese el número de usuarios normales: "))
if numero_usuarios_normal < 0:
    print("El número de usuarios normales no puede ser negativo.")
    exit()

numero_usuarios_premium = int(input("Ingrese el número de usuarios premium: "))
if numero_usuarios_premium < 0:
    print("El número de usuarios premium no puede ser negativo.")
    exit()

gasto_total = float(input("Ingrese el gasto total: "))
if gasto_total < 0:
    print("El gasto total no puede ser negativo.")
    exit()

# Calcular el precio de suscripción premium
precio_suscripcion_premium = precio_suscripcion_normal * 1.5

# Calcular las utilidades
ingresos_normal = precio_suscripcion_normal * numero_usuarios_normal
ingresos_premium = precio_suscripcion_premium * numero_usuarios_premium
utilidades = ingresos_normal + ingresos_premium - gasto_total

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades:.2f}")
