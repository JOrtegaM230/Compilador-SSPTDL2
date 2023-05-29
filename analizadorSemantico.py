from anytree import Node

# Clase para el analizador semántico
class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}  # Tabla de símbolos para almacenar información semántica

    def analyze(self, ast):
        self.visit(ast)  # Iniciar el análisis semántico en el nodo raíz del árbol sintáctico

    def visit(self, node):
        if node.name == 'Definiciones':
            for child in node.children:
                self.visit(child)

        elif node.name == 'Definicion':
            self.visit(node.children[0])

        elif node.name == 'DefVar':
            tipo = node.children[0].name
            identificador = node.children[1].name
            self.add_variable(identificador, tipo)

            self.visit(node.children[2])  # Visitamos la lista de variables

        elif node.name == 'ListaVar':
            for child in node.children:
                self.visit(child)

        else:
            for child in node.children:
                self.visit(child)

    def add_variable(self, identificador, tipo):
        if identificador in self.symbol_table:
            print("La variable " + identificador + " ya está declarada")
        else:
            self.symbol_table[identificador] = tipo


# # Análisis semántico
# analyzer = SemanticAnalyzer()
# analyzer.analyze(nodoP)
# print("")
# print("Tabla de símbolos")
# for identificador, tipo in analyzer.symbol_table.items():
#     print(f'{identificador}: {tipo}')

