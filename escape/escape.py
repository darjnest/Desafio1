#Velocidad de escape 

import math

def escape_velocity(g, r):
    """
    Calcular la velocidad de escape.
    
    Parámetros:
    g (float): Constante gravitacional en m/s^2
    r (float): Radio del planeta en metros
    
    Retorna:
    float: Velocidad de escape en m/s
    """
    return math.sqrt(2 * g * r)

def main():
    # Solicitar la constante gravitacional g
    g = float(input("Ingrese la constante gravitacional g (en m/s^2): "))
    
    # Solicitar el radio del planeta r en kilómetros y convertirlo a metros
    r_km = float(input("Ingrese el radio en Kilómetros: "))
    r_m = r_km * 1000  # Convertir kilómetros a metros
    
    # Calcular la velocidad de escape
    ve = escape_velocity(g, r_m)
    
    # Mostrar el resultado
    print(f"La velocidad de escape es {ve:.1f} [m/s]")

# Este bloque asegura que main() solo se ejecutará si este archivo es ejecutado como un script
if __name__ == "__main__":
    main()



