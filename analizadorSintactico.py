import numpy as np
import analizadorLexico as pr
import pila as pila
from anytree import Node, RenderTree
import analizadorSemantico as anS

class elementoPila:
    def __init__(self):
        self.tipoE = ""
        self.valorE = ""
        self.idE = 0
        self.tipo = ""

#Tomar valores de arreglo empezando por el último
def tomar_valores_desde_el_final(arreglo, cantidad):
    valores = arreglo[-cantidad:]
    return valores

# Comparar pila y valores de una regla
def comparar_arreglos(arreglo1, arreglo2):
    if arreglo1 == arreglo2:
        return True
    else:
        return False

# Guardar palabras de parte derecha de una regla en un arreglo
def guardar_palabras_en_arreglo(cadena):
    palabras = cadena.split()
    return palabras

# Obtener parte derecha de una regla
def obtener_caracteres_despues_de(cadena):
    partes = cadena.split("::=")
    if len(partes) > 1:
        caracteres_despues_de = partes[1].strip()
        return caracteres_despues_de
    else:
        return ""

#Quitar texto desde fin
def quitar_texto_desde_fin(cadena, texto_a_quitar):
    indice = cadena.rfind(texto_a_quitar)
    if indice != -1:
        nueva_cadena = cadena[:indice] + cadena[indice + len(texto_a_quitar):]
        return nueva_cadena
    else:
        return cadena

#Modificar cadena de entrada para mostrar
def quitar_texto(cadena, texto_a_quitar):
    nueva_cadena = cadena.replace(texto_a_quitar, '', 1)
    return nueva_cadena

def analizar(codigo_fuente):
    bandraiz = 0

    pilaObjetos = pila.Pila()

    # Ruta del archivo .lr
    archivo_lr = "compilador.lr"

    # Número de filas a omitir
    filas_a_omitir = 54

    # Leer el archivo y cargar los datos en una matriz, omitiendo las filas anteriores
    matriz = np.loadtxt(archivo_lr, delimiter='\t', dtype=int, skiprows=filas_a_omitir)

    # Configurar la impresión de numpy para mostrar todos los elementos
    np.set_printoptions(threshold=np.inf)

    # Ruta del archivo .inf
    archivo_inf = "compilador.inf"

    # Número de filas a omitir
    filas_a_omitirinf = 26

    # Leer el archivo y guardar las filas en una lista
    filas = []
    with open(archivo_inf, "r") as archivo:
        for _ in range(filas_a_omitirinf):
            next(archivo)  # Omitir filas anteriores

        for linea in archivo:
            fila = linea.strip().split(" ", 1)[1]  # Excluir primera palabra y espacio en blanco
            filas.append(fila)

    # Convertir la lista de filas en un arreglo numpy
    arreglo_filas = np.array(filas)

    # Ruta del archivo .lr
    archivo_lr = "compilador.lr"

    # Rango de filas a leer
    inicio_fila = 1  # Fila 2
    fin_fila = 52   # Fila 53

    # Leer el archivo y guardar las filas de la 2 a la 53 como texto
    datos_texto = np.genfromtxt(archivo_lr, delimiter='\t', dtype=str, skip_header=inicio_fila, max_rows=(fin_fila - inicio_fila + 1))

    entrada = codigo_fuente

    #Hacer análisis léxico
    tokens_encontrados = pr.analizar_codigo_fuente(codigo_fuente)

    print("Tokens")

    for token_nombre, token_tipo, valor in tokens_encontrados:
        print(f'Token: {token_nombre}, Tipo: {token_tipo}, Valor: {valor}')

    print("")

    contador = 0
    bandera = True
    while bandera == True:
        if entrada != "":
            actual = tokens_encontrados[contador][1]
        else:
            actual = 23
        if actual == "NA":
            entrada = quitar_texto(entrada, tokens_encontrados[contador][2])
            contador += 1
            continue
        tope = pilaObjetos.mostrarUltimo()
        salida = matriz[tope][actual]
        objp = elementoPila()
        if salida > 0:
            textopila = pilaObjetos.mostrarPila()
            objp.idE = actual
            objp.tipoE = "TERMINAL"
            objp.valorE = tokens_encontrados[contador][2]
            objp.tipo = tokens_encontrados[contador][0]
            pilaObjetos.apilar(objp)
            objpe = elementoPila()
            objpe.idE = salida
            objpe.tipoE = "ESTADO"
            objpe.valorE = str(salida)
            pilaObjetos.apilar(objpe)
            #textopila = pilaObjetos.mostrarPila()
            if contador == 0:
                print("{:<50s}{:>20s}{:>10s}".format("PILA", "ENTRADA", "SALIDA"))
                #print(f'Pila                        Entrada                     Salida                      ')
            print("{:<50s}{:>20s}{:>10s}".format("$0"+textopila, entrada+"$", "d"+str(salida)))
            #print(f'$0{textopila}                       {entrada}                       d{salida}')
            entrada = quitar_texto(entrada, tokens_encontrados[contador][2])
            contador += 1
        elif salida < 0:
            salida = abs(salida) - 1
            if salida == 0:
                textopila = pilaObjetos.mostrarPila()
                print("{:<50s}{:>20s}{:>10s}".format("$0"+textopila, entrada+"$", "d"+str(salida)))
                break
            regla = arreglo_filas[salida-1]
            reglamostrar = regla
            lonRegla = int(datos_texto[salida - 1][1])
            if lonRegla == 0:
                textopila = pilaObjetos.mostrarPila()
                objp.idE = int(datos_texto[salida - 1][0])
                objp.tipoE = "NO TERMINAL"
                objp.valorE = datos_texto[salida - 1][2]
                objpE = elementoPila()
                objpE.idE = matriz[pilaObjetos.mostrarUltimo()][objp.idE]
                objpE.tipoE = "ESTADO"
                objpE.valorE = str(matriz[pilaObjetos.mostrarUltimo()][objp.idE])
                pilaObjetos.apilar(objp)
                pilaObjetos.apilar(objpE)
                #textopila = pilaObjetos.mostrarPila()
                if contador == 0:
                    print("{:<50s}{:>20s}{:>10s}".format("PILA", "ENTRADA", "SALIDA"))
                print("{:<50s}{:>20s}{:>10s}{:<60s}".format("$0"+textopila, entrada+"$", "r"+str(salida), "  ->  "+reglamostrar))
            else:
                regla = obtener_caracteres_despues_de(regla)
                for i in range(lonRegla):
                    regla = quitar_texto_desde_fin(regla, ">")
                    regla = quitar_texto_desde_fin(regla, "<")
                regla = guardar_palabras_en_arreglo(regla)
                comparar = pilaObjetos.mostrarNoestados()
                comparar = tomar_valores_desde_el_final(comparar, len(regla))
                comparar2 = pilaObjetos.mostrarNoest()
                comparar2 = tomar_valores_desde_el_final(comparar2, len(regla))
                if comparar_arreglos(regla, comparar) == True:
                    if bandraiz == 0:
                        nodoP = Node(datos_texto[salida - 1][2])
                        bandraiz += 1
                        name = nodoP.name
                    else:
                        name = nodoP.name
                        nodoR = Node(datos_texto[salida - 1][2])
                        nodoP.parent = nodoR
                        nodoP = nodoR
                    for i in range(lonRegla):
                        if i == 0:
                            if name == comparar[i]:
                                continue
                        nodo = Node(comparar2[i], parent = nodoP)
                    textopila = pilaObjetos.mostrarPila()
                    pilaObjetos.vaciar(len(comparar))
                    objp.idE = int(datos_texto[salida - 1][0])
                    objp.tipoE = "NO TERMINAL"
                    objp.valorE = datos_texto[salida - 1][2]
                    objpE = elementoPila()
                    objpE.idE = matriz[pilaObjetos.mostrarUltimo()][objp.idE]
                    objpE.tipoE = "ESTADO"
                    objpE.valorE = str(matriz[pilaObjetos.mostrarUltimo()][objp.idE])
                    pilaObjetos.apilar(objp)
                    pilaObjetos.apilar(objpE)
                    #textopila = pilaObjetos.mostrarPila()
                    if contador == 0:
                        print("{:<50s}{:>20s}{:>10s}".format("PILA", "ENTRADA", "SALIDA"))
                    print("{:<50s}{:>20s}{:>10s}{:<60s}".format("$0"+textopila, entrada+"$", "r"+str(salida), "  ->  "+reglamostrar))
                else:
                    print("NO SÉ QUÉ PASÓ")
                    print(regla)
                    print(comparar)
                    break
        else:
            print("La sintáxis no es válida")
            print(pilaObjetos.mostrarPila())
            break

    print("")
    print("Árbol sintáctico")
    #Mostrar el árbol
    for pre, fill, node in RenderTree(nodoP):
        print("%s%s" % (pre, node.name))

    analizador = anS.SemanticAnalyzer()

    # Análisis semántico
    analizador.analyze(nodoP)
    print("")
    print("Tabla de símbolos")
    for identificador, tipo in analizador.symbol_table.items():
        print(f'{identificador}: {tipo}')