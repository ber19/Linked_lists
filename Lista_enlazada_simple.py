# Esta clase representa un nodo
class Node:
    # Cuando se instancie la clase
    def __init__(self, value):
        # Se define el valor del nodo
        self.value = value
        # Se define el siguiente nodo, que por defecto es ninguno
        self.next = None

    # Cuando se use str() en el nodo
    def __str__(self):
        # Se retorna su valor como string
        return str(self.value)

# Esta clase representa una lista enlazada simple
class LinkedList:
    # Cuando se instancie la clase
    def __init__(self):
        # Se define la cabeza(primer nodo) de la lista
        # que por defecto es ninguno
        self.head = None
        # Se define el tamaño de la lista
        # que por defecto es 0
        self.size = 0

    # Este metodo es para añadir(al final) un nodo(elemento) a la lista
    def append(self, value):
        # Se crea un nodo
        node = Node(value)
        # Si la lista esta vacia
        if self.size == 0:
            # El nodo se convierte en la cabeza
            self.head = node
        # Si la lista no esta vacia
        else:
            # Se crea un apuntador ubicado 
            # en el nodo cabeza
            current = self.head
            # Mientras el apuntador tenga 
            # nodos delante de él
            while current.next != None:
                # El apuntador cambia al siguiente nodo
                current = current.next
            # Cuando el apuntador ya no tenga
            # nodos delante de él:
            # El siguiente nodo del nodo cola(ultimo nodo)
            # es el nodo que se creo al principio
            # que por defecto su siguiente nodo es None
            current.next = node
        
        # Se aumenta en uno el tamaño de la lista
        self.size += 1

        # Esto es opcional, para que el metodo regrese algo
        return node

    # Este metodo es para eliminar un nodo(elemento) de la lista
    # segun su valor
    def remove(self, value):
        # Si el tamaño de la lista es 0 (no hay elementos)
        if self.size == 0:
            # Retornamos False 
            return False
        
        # Si la lista contiene elementos
        else:
            # Se crea un apuntador ubicado en el nodo cabeza
            current = self.head

            # Mientras el valor del siguiente nodo
            # del apuntador no sea igual a value(parametro)
            while current.next.value != value:
                # El apuntador se ubica en el siguiente nodo
                current = current.next
                # Si el apuntador es el ultimo nodo de la lista
                if current.next == None:
                    # Se retorna False
                    raise ValueError('Value not in list')

            # Cuando el valor del siguiente nodo del
            # apuntador es igual a value(parametro):
            # Se crea guarda el siguiente nodo(el que se borrará)
            deletedNode = current.next
            # El apuntador ahora apunta al nodo
            # que apuntaba el nodo borrado (el que le seguia)
            current.next = deletedNode.next

        # Se disminuye en uno el tamaño de la lista
        self.size -= 1

        # Esto es opcional, para que el metodo regrese algo
        return deletedNode

    # Cuando se use len() en la lista
    def __len__(self):
        # Se retorma el tamaño de la lista
        return self.size

    # Cuando se use str() en la lista
    def __str__(self):
        # Se crea un string
        string = '['
        # Se crea un apuntador
        current = self.head
        # Se itera en un rango de 0 a
        # el valor del tamaño de la lista
        for i in range(self.size):
            # Se concatena el valor del nodo
            # donde esta el apuntador al string
            string += str(current)
            # Si la iteracion actual no es la ultima
            if i != self.size - 1:
                # Se concatena al string ', '
                string += ', '
            # El apuntador cambia a su siguiente nodo
            current = current.next
        # Al final de la iteración se concatena ']'
        # al string
        string += ']'

        # Se retorna el string
        return string


# Se instancia la clase de la lista (se crea una lista vacia)
lista = LinkedList()
# Se añaden velores a la lista
lista.append(1)
lista.append(2)
lista.append(3)

# Se eliminan valores de la lista
lista.remove(2)
# Esta eliminacion debe causar un error (el valor no esta en la lista)
lista.remove(7)