def busqueda_binaria(lista, objetivo):
    # Definir los límites del rango de búsqueda
    inicio = 0
    fin = len(lista) - 1

    # Realizar la búsqueda mientras el rango sea válido
    while inicio <= fin:
        # Encontrar el punto medio del rango
        medio = (inicio + fin) // 2
        # Comparar el valor en el punto medio con el objetivo
        if lista[medio] == objetivo:
            return medio  # Retorna el índice si se encuentra el objetivo
        elif lista[medio] < objetivo:
            inicio = medio + 1  # Si el objetivo es mayor, descartar la mitad inferior
        else:
            fin = medio - 1  # Si el objetivo es menor, descartar la mitad superior

    return -1  # Retorna -1 si el objetivo no se encuentra en la lista

# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = 7
resultado = busqueda_binaria(lista_ordenada, objetivo)

if resultado != -1:
    print(f"El número {objetivo} se encuentra en el índice {resultado}.")
else:
    print(f"El número {objetivo} no está en la lista.")
