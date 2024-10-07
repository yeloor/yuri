# Escritura de Archivo de Texto
# El archivo se abre en modo escritura ("w"). Si no existe, se creará automáticamente.
# Se escribe cada línea usando el método write().
with open("my_notes.txt", "w") as file:
    # Escribir tres líneas de texto
    file.write("Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("Escribir y leer archivos de texto es bastante sencillo.\n")
    file.write("¡Estoy emocionado por continuar mejorando mis habilidades de programación!\n")

# Lectura de Archivo de Texto
# Abrir el archivo en modo lectura ("r") y leerlo línea por línea utilizando readline().
with open("my_notes.txt", "r") as file:
    # Leer y mostrar la primera línea
    line = file.readline()
    print(line, end="")  # Mostrar línea sin añadir salto de línea extra

    # Leer y mostrar la segunda línea
    line = file.readline()
    print(line, end="")

    # Leer y mostrar la tercera línea
    line = file.readline()
    print(line, end="")
