import graphviz

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if not self.cola:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza
        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def mostrar_lista(self):
        nodo_actual = self.cabeza
        lista_str = "None <- "
        while nodo_actual:
            lista_str += f"{nodo_actual.nombre} {nodo_actual.apellido} ({nodo_actual.carnet}) <-> "
            nodo_actual = nodo_actual.siguiente
        lista_str += "-> None"
        print(lista_str)

    def graficar_lista(self, filename):
        dot = graphviz.Digraph(comment='Lista Doblemente Enlazada')
        nodo_actual = self.cabeza
        while nodo_actual:
            dot.node(str(nodo_actual.carnet), f"{nodo_actual.nombre} {nodo_actual.apellido} ({nodo_actual.carnet})")
            if nodo_actual.anterior:
                dot.edge(str(nodo_actual.anterior.carnet), str(nodo_actual.carnet))
            if nodo_actual.siguiente:
                dot.edge(str(nodo_actual.carnet), str(nodo_actual.siguiente.carnet))
            nodo_actual = nodo_actual.siguiente
        dot.render(filename, format='png', cleanup=True)

def menu():
    lista = ListaDoblementeEnlazada()

    while True:
        print("\nMenú:")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por valor")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            carnet = input("Ingrese carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)
        elif opcion == "2":
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            carnet = input("Ingrese carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)
        elif opcion == "3":
            carnet = input("Ingrese el carnet a eliminar: ")
            if lista.eliminar_por_valor(carnet):
                print("Nodo eliminado correctamente.")
            else:
                print("El carnet no existe en la lista.")
        elif opcion == "4":
            lista.mostrar_lista()
            lista.graficar_lista("lista_doblemente_enlazada.png")
            print("Representación visual de la lista generada.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()

