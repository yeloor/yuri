informacion_personal = {
    "nombre": "Yuri Loor",
    "edad": 22,
    "ciudad": "Riobamba",
    "profesion": "Ingeniero en Tecnologías de la Información"
}
# Acceder al valor actual de la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Tegnologias de la informacion"

# Ver el diccionario actualizado
print(informacion_personal)
# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregar la clave "telefono" con un valor ficticio
    informacion_personal["telefono"] = "0987654321"

# Ver el diccionario actualizado
print(informacion_personal)
# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Ver el diccionario actualizado
print(informacion_personal)
# Imprimir el diccionario final
print(informacion_personal)
