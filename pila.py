class Pila:

    def __init__(self):
        # Crea una pila vacía. 
        self.items=[]
    
    def apilar(self, x):
        # Agregar el elemento x a la pila.
        self.items.append(x)

    def desapilar(self):
        # Devolvee el elemento tope y lo elimina de la pila.
        # Si la pila está vacía levanta una excepción.
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
        
    def mostrarUltimo(self):
        # Devolver tipo de último elemento
        if len(self.items) > 0:
            return int(self.items[len(self.items)-1].idE)
        else:
            return 0
    
    def imprimir(self):
        for i in self.items:
            print(i.valorE)

    def mostrarPila(self):
        if len(self.items) > 0:
            textoPila = ""
            for i in self.items:
                textoPila = textoPila + str(i.valorE)
            return textoPila
        else:
            return ""

    def nombreNodo(self):
        if len(self.items) > 0:
            nombre = ""
            nombre = nombre + self.items[len(self.items)-2].valorE

    def mostrarNoest(self):
        if len(self.items) > 0:
            valores = []
            for i in self.items:
                if i.tipoE != "ESTADO":
                    valores.append(i.valorE)
                else:
                    pass
            return valores
        else:
            return None

    def mostrarNoestados(self):
        if len(self.items) > 0:
            valores = []
            for i in self.items:
                if i.tipoE != "ESTADO":
                    if i.tipoE == "NO TERMINAL":
                        valores.append(i.valorE)
                    else:
                        valores.append(i.tipo)
                else:
                    pass
            return valores
        else:
            return None
        
    def vaciar(self, cant):
        for i in range(cant*2):
            self.items.pop()
