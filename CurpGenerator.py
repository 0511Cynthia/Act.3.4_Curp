import random
import re
from GetStates import get_state

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_consonante_interna(palabra):
    consonantes = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', palabra[1:])
    return consonantes[0] if consonantes else 'X'

def generar_curp(nombre, apellido_paterno, apellido_materno, anio, mes, dia, sexo, estado):
    if not all([nombre, apellido_paterno, apellido_materno, anio, mes, dia, sexo, estado]):
        raise ValueError("Todos los campos son obligatorios.")

    state = get_state(estado)
    curp = apellido_paterno[0] + re.search(r'[aeiouAEIOU]', apellido_paterno[1:])[0] + apellido_materno[0] + nombre[0]
    curp += f"{anio % 100:02d}{mes}{dia}"
    curp += sexo[0]
    curp += state

    curp += obtener_consonante_interna(apellido_paterno)
    curp += obtener_consonante_interna(apellido_materno)
    curp += obtener_consonante_interna(nombre)

    penultimo = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    ultimo = random.choice("0123456789")
    curp += penultimo + ultimo

    return curp