class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        node = Node(value)
        if self.size == 0:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        
        self.size += 1

        return node

    def remove(self, value):
        if self.size == 0:
            return False
        
        else:
            current = self.head

            while current.next.value != value:
                current = current.next
                if current.next == None:
                    raise ValueError('Value not in list')

            deletedNode = current.next
            current.next = deletedNode.next

        self.size -= 1

        return deletedNode

    def __len__(self):
        return self.size

    def __str__(self):
        string = '['
        current = self.head
        for i in range(self.size):
            string += str(current)
            if i != self.size - 1:
                string += ', '
            current = current.next
        string += ']'

        return string