import random
import string

# Grupos de caracteres permitidos
MAYUS = string.ascii_uppercase
MINUS = string.ascii_lowercase
NUMS = string.digits
ESPECIALES = "!@#$%&*?"

# Todos los caracteres juntos para completar la contraseña
TODOS = MAYUS + MINUS + NUMS + ESPECIALES

def generar_password(longitud):
    # Validación: mínimo 12 (3 de cada tipo)
    if longitud < 12:
        raise ValueError("La longitud mínima es 12 (3 mayúsculas, 3 minúsculas, 3 números, 3 especiales).")

    password = []  # Lista mutable donde iremos agregando caracteres

    # --- Agregamos 3 caracteres de cada tipo ---
    for _ in range(3):
        password.append(random.choice(MAYUS))      # 3 mayúsculas

    for _ in range(3):
        password.append(random.choice(MINUS))      # 3 minúsculas

    for _ in range(3):
        password.append(random.choice(NUMS))       # 3 números

    for _ in range(3):
        password.append(random.choice(ESPECIALES)) # 3 especiales

    # --- Si la longitud es mayor a 12, completamos con cualquier tipo ---
    for _ in range(longitud - 12):
        password.append(random.choice(TODOS))

    # Mezclamos para que no queden en orden predecible
    random.shuffle(password)

    # Convertimos la lista en un string final
    return "".join(password)

# --- Programa principal ---
while True:
    try:
        # Pedimos la longitud al usuario
        entrada = int(input("Ingresá la longitud de la contraseña (mínimo 12, no puede ser 0): "))

        # Validaciones básicas
        if entrada == 0:
            print("La longitud no puede ser 0.")
            continue

        if entrada < 12:
            print("Debe ser al menos 12 para cumplir las reglas.")
            continue

        # Generamos y mostramos la contraseña
        pwd = generar_password(entrada)
        print("Contraseña generada:", pwd)
        break

    except ValueError:
        print("Ingresá un número entero válido.")
