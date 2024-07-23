# emprendedor3.py

print("Advertencia: Asegúrese de que los valores ingresados sean positivos y que el gasto total no exceda los ingresos.")


def obtener_datos():
    try:
        precio_suscripcion = float(input("Ingrese el precio de suscripción (P): "))
        if precio_suscripcion <= 0:
            raise ValueError("El precio de suscripción debe ser mayor que 0.")
        
        numero_usuarios = int(input("Ingrese el número de usuarios normales (U): "))
        if numero_usuarios <= 0:
            raise ValueError("El número de usuarios debe ser mayor que 0.")
        
        gasto_total = float(input("Ingrese el gasto total (GT): "))
        if gasto_total < 0:
            raise ValueError("El gasto total no puede ser negativo.")
        
        utilidades_anterior = float(input("Ingrese las utilidades del año anterior (Uanterior): "))
        if utilidades_anterior == 0:
            raise ValueError("Las utilidades del año anterior no pueden ser cero.")

        return precio_suscripcion, numero_usuarios, gasto_total, utilidades_anterior
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

def calcular_utilidades(precio_suscripcion, numero_usuarios, gasto_total):
    return (precio_suscripcion * numero_usuarios) - gasto_total

def calcular_razon(utilidades_actuales, utilidades_anterior):
    return utilidades_actuales / utilidades_anterior

def main():
    datos = obtener_datos()
    if datos:
        precio_suscripcion, numero_usuarios, gasto_total, utilidades_anterior = datos
        utilidades_actuales = calcular_utilidades(precio_suscripcion, numero_usuarios, gasto_total)
        razon = calcular_razon(utilidades_actuales, utilidades_anterior)
        print(f"Las utilidades actuales son: {utilidades_actuales:.2f}")
        print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f}")

if __name__ == "__main__":
    main()



