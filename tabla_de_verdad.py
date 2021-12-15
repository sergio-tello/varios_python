'''
Sergio Tello - 2021

TABLA DE VERDAD PARA UNA FÓRMULA DE LA LÓGICA PROPOSICIONAL

* Variables que se pueden usar: [a-z] (excepto v).
* Operadores que se pueden usar: negación (¬), disyunción (v).

Este programa valida que la fórmula ingresada por el usuario sea
sintácticamente correcta y, si lo es, imprime la tabla de verdad.
'''


# Funciones empleadas

def particiones_binarias(lista):
    particiones = []
    for i in range(len(lista)-1):
        elemento = ['v'.join(lista[:i+1]), 'v'.join(lista[i+1:])]
        particiones.append(elemento)
    return particiones

def reemplazar_valores_en_formula(cad, diccionario):
    for letra, valor in diccionario.items():
        cad = cad.replace(letra, valor)
    return cad
    
def validar_cadena(cad):
# Caso base: Letra proposicional
    if len(cad) == 1 and 97 <= ord(cad) <= 122 and ord(cad) != 118:
        #print('Estoy analizando una letra proposicional')
        return True
# Caso (E): Expresión entre paréntesis 
    elif cad.startswith('(') and cad.endswith(')'):
        #print('Estoy analizando una expresión entre paréntesis')
        return validar_cadena(cad[1:-1]) or any([validar_cadena(particion[0]) and 
               validar_cadena(particion[1]) for particion in particiones_binarias(cad.split('v'))])
# Caso ¬: Expresión que comienza con un símbolo de negación
    elif cad.startswith('¬'):
        #print('Estoy analizando una negación')
        return validar_cadena(cad[1:])
# Caso v: Expresión con un v
    elif cad.count('v') >= 1:
        #print('Estoy analizando una expresión con v')
        return any([validar_cadena(particion[0]) and 
               validar_cadena(particion[1]) for particion in particiones_binarias(cad.split('v'))])
    else: 
        #print('Error de sintaxis')
        return False


def evaluar_cadena(cadena):
    while len(cadena) > 1:
        cadena = cadena.replace('(0)', '0')
        cadena = cadena.replace('(1)', '1')
        cadena = cadena.replace('¬0', '1')
        cadena = cadena.replace('¬1', '0')
        cadena = cadena.replace('0v0', '0')
        cadena = cadena.replace('0v1', '1')
        cadena = cadena.replace('1v0', '1')
        cadena = cadena.replace('1v1', '1')
    return cadena

def obtener_letras_proposicionales(cadena):
    letras_proposicionales = set()
    for caracter in cadena:
        if 97 <= ord(caracter) <= 122 and ord(caracter) != 118:
            letras_proposicionales.add(caracter)
    return list(letras_proposicionales)

def tabla_de_verdad(cadena):
    tabla = []
    letras_proposicionales = obtener_letras_proposicionales(cadena)
    letras_proposicionales.sort()
    num_letras = len(letras_proposicionales)
    encabezado = []
    encabezado = [letra for letra in letras_proposicionales]
    encabezado.append(cadena)
    tabla.append(encabezado)
    for i in range(2**num_letras):
        binario = bin(i).replace('0b','').zfill(num_letras)
        valores = list(binario)
        zip_letras_valores = zip(letras_proposicionales, valores)
        diccionario_letras_valores = dict(zip_letras_valores)
        cadena_a_evaluar = reemplazar_valores_en_formula(cadena, diccionario_letras_valores)
        valor_de_verdad = evaluar_cadena(cadena_a_evaluar)
        fila = []
        fila = [valor for valor in valores]
        fila.append(valor_de_verdad)
        tabla.append(fila)
    return tabla

def imprimir_tabla(tabla):
    print('-'* (len(str(tabla[0])) - len(tabla[0]) + 1))
    for fila in tabla:
        print('|', end='')
        for i in range(len(fila)):
            print(fila[i].center(len(tabla[0][i])+2), end='')
            print('|', end='')
        print(end='\n')
        print('-'* (len(str(tabla[0])) - len(tabla[0]) + 1))
       


if __name__ == '__main__':
    print(
'''
=========================================================================
TABLA DE VERDAD PARA UNA FÓRMULA DE LA LÓGICA PROPOSICIONAL

* Variables que se pueden usar: [a-z] (excepto v).
* Operadores que se pueden usar: negación (¬), disyunción (v).

El programa valida que la fórmula ingresada por el usuario sea
sintácticamente correcta y, si lo es, imprime la tabla de verdad.
=========================================================================''')
    cadena = input('Ingrese la fórmula: ')
    cadena = cadena.replace(' ', '')
    cadena = cadena.lower()
    valor = validar_cadena(cadena)
    if valor:
        tabla = tabla_de_verdad(cadena)
        imprimir_tabla(tabla)
    else:
        print('Error de sintaxis')
