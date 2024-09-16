def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades durante varias semanas.

    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de listas de temperaturas (una lista por semana) como valores.

    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}  # Diccionario para almacenar el promedio de temperaturas por ciudad

    # Iteramos sobre cada ciudad en el diccionario
    for ciudad, semanas in ciudades_temperaturas.items():
        # Aplanamos la lista de temperaturas de todas las semanas en una sola lista
        temperaturas = [temp for semana in semanas for temp in semana]

        # Calculamos el promedio de temperaturas
        promedio = sum(temperaturas) / len(temperaturas)

        # Guardamos el promedio en el diccionario de resultados
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario de ciudades en Riobamba y temperaturas durante 4 semanas
ciudades_temperaturas = {
    "Riobamba Centro": [[18, 20, 21, 19], [19, 21, 22, 20], [20, 22, 23, 21], [18, 20, 21, 19]],
    "Quito": [[17, 19, 20, 18], [18, 20, 21, 19], [19, 21, 22, 20], [17, 19, 20, 18]],
    "Cayambe": [[16, 18, 19, 17], [17, 19, 20, 18], [18, 20, 21, 19], [16, 18, 19, 17]]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados en la consola
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
