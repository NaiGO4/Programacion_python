def add_water():
    print("1. Añadiendo agua en la tetera.")

def herve_water():
    print("2. Poniendo el a calentar la tetera.")
    print("El agua comienza a hervir \n")
    return "Agua caliente"

def preparar_cafe():
    print("3. Preparar Cafe")


def add_granulo_cafe(taza):
    print("Añadiendo granos de cafe a la taza.")
    taza.append("cafe")

def vertir_cafe_y_agua(taza, agua):
    if agua == "agua caliente":
        print("5. Veritiendo agua caliente en la taza.")
        taza.append(agua)
    else:
        print("Esperando a que el agua este caliente")

def add_opciones(taza, leche=False, nata=False, azucar=0):
    if leche:
        print("6. Añadiendo leche a la taza.")
        taza.append("leche")
    if nata:
        print("6. Añadiendo nata a la taza.")
    if azucar > 0:
        print(f"6. Añadiendo {azucar} cucharadas de azucar.")
        taza.append(f"{azucar} cucharadas de azucar.")

def revolver(taza):
    print("7. Revolviendo la taza")
    taza.append("mezclando")

def preparar_taza_café(leche=False, nata=False, azucar=0):
    print("Iniciando preparación de una taza de café...\n")
    taza = []
    add_water()
    agua = herve_water()
    preparar_cafe()
    add_granulo_cafe(taza)
    vertir_cafe_y_agua(taza, agua)
    add_opciones(taza, leche, nata, azucar)
    print("\nTu taza de cafe esta lista")
    return taza

# Llamamos a la función principal con opciones de leche, nata y azúcar
preparar_taza_café(leche=True, nata=False, azúcar=2)