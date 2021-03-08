class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        string = '['
        if self.head == None:
            string += ']'
            return string
        current = self.head
        string += str(current.value)
        while current.next != None:
            string += ', '
            current = current.next
            string += str(current.value)
        string += ']'
        return string

    def push(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            moved = self.head
            self.head = new_node
            self.head.next = moved
        self.size += 1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete(self, value):
        if self.head == None:
            return False

        if self.head.value == value and self.head.next == None:
            self.head = None
            self.size -= 1
            return str(self)

        while self.head.value == value and self.head.next != None:
            self.head = self.head.next
            self.size -= 1
        
        current = self.head
        while current.next != None:
            if current.next.value == value:
                deleted = current.next
                current.next = deleted.next
                self.size -= 1
            else:
                current = current.next
        
        return str(self)