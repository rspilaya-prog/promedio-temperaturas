def calcular_promedios(temperaturas, ciudades):
    """
    Calcula la temperatura promedio de cada ciudad.

    Parámetros:
    temperaturas: Lista de listas con temperaturas por ciudad y semana
    ciudades: Lista con los nombres de las ciudades

    Retorna:
    Diccionario con el nombre de la ciudad y su promedio
    """
    promedios = {}  # Creamos un diccionario vacío para guardar los resultados
    
    # Recorremos cada ciudad usando un índice
    for i in range(len(ciudades)):
        suma = sum(temperaturas[i])           # Sumamos todas las temperaturas de esa ciudad
        promedio = suma / len(temperaturas[i])  # Calculamos el promedio
        promedios[ciudades[i]] = promedio    # Guardamos el resultado en el diccionario
    
    return promedios  # Devolvemos los promedios
