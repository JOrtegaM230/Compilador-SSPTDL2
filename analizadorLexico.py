import re

# Definir las expresiones regulares para los tokens
tokens = [
    ('real', 2, r'\d+\.\d+'),              # Números reales
    ('entero', 1, r'\d+'),                 # Números enteros (con parte decimal opcional)
    (';', 12, r';'),                       # Punto y coma
    (',', 13, r','),                       # Coma
    ('if', 19, r'if'),                     # Palabra reservada if
    ('while', 20, r'while'),               # Palabra reservada while
    ('return', 21, r'return'),             # Palabra reservada return
    ('else', 22, r'else'),                 # Palabra reservada else
    ('tipo', 4, r'(int|float|void)'),      # Tipos (int, float, void)
    ('identificador', 0, r'\w+'),          # Identificadores (letras y números)
    ('cadena', 3, r'[a-zA-Z]+'),           # Cadenas (letras)
    ('opSuma', 5, r'[+\-]'),               # Operadores de suma y resta
    ('opMul', 6, r'[*/]'),                 # Operadores de multiplicación y división
    ('opRelac', 7, r'[<>]=?'),             # Operadores de relación
    ('opOr', 8, r'\|\|'),                  # Operador lógico OR
    ('opAnd', 9, r'\&\&'),                 # Operador lógico AND
    ('opIgualdad', 11, r'==|!='),          # Operadores de igualdad
    ('opNot', 10, r'!'),                   # Operador de negación
    ('(', 14, r'\('),                      # Paréntesis izquierdo
    (')', 15, r'\)'),                      # Paréntesis derecho
    ('{', 16, r'\{'),                      # Llave izquierda
    ('}', 17, r'\}'),                      # Llave derecha
    ('=', 18, r'='),                       # Asignación
    ('$', 23, r'\$'),                      # Símbolo $ 
    ('ESPACIO', "NA", r'\s+'),             # Espacios en blanco (saltos de línea, espacios, tabulaciones, etc.)
]
# Función para analizar el código fuente
def analizar_codigo_fuente(codigo):
    # Lista para almacenar los tokens encontrados
    resultado = []
    # Iterar sobre el código fuente
    while codigo:
        # Bandera para indicar si se encontró un token válido
        emparejado = False
        # Iterar sobre las expresiones regulares de los tokens
        for token_nombre, token_tipo, patron in tokens:
            # Intentar hacer coincidir el patrón con el código fuente
            coincidencia = re.match(patron, codigo)
            # Si se encontró un token válido
            if coincidencia:
                # Obtener el valor del token
                valor = coincidencia.group(0)
                # Agregar el token y su valor al resultado
                resultado.append((token_nombre, token_tipo, valor))
                # Actualizar el código fuente eliminando el token encontrado
                codigo = codigo[len(valor):]
                # Marcar la bandera como True
                emparejado = True              
                # Salir del bucle interno
                break       
        # Si no se encontró un token válido, lanzar un error
        if not emparejado:
            raise ValueError('Token no válido: ' + codigo)    
    return resultado

