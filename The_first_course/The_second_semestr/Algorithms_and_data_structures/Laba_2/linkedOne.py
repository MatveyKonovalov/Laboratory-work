from Nodes import *
from showlst import *

class LinkedListOne():
    
    def __init__(self, node: Node|TwoNode):
        self.head = node



    def show(self, delimiter = " -> "):
        cur = self.head
        while cur is not None:
            print(cur.val, end = delimiter)
            cur = cur.next
        print("None")



    def addIndex(self, node: Node|TwoNode, index=float("inf")):
        '''Добавление в начало .add(Node, 0), добавление в конец .add(Node)'''

        # Добавление в начало
        if not index:
            node.next = self.head
            self.head = node
            return self.head
        
        cur = self.head
        while index > 1 and not (cur.next is None):
            index -= 1
            cur = cur.next

        if cur.next is None:
            cur.next = node
        else:
            node.next = cur.next
            cur.next = node

        return cur



    def removeIndex(self, index=float("inf")):

        cur = self.head
        if not index or cur.next is None:
            self.head = self.head.next
            print("Список пуст")
            return None
        
        curIndex = 0

        while curIndex != index - 1:
            curIndex += 1
            if cur.next.next is None:
                break
            cur = cur.next
        cur.next = cur.next.next

        return cur

    def removeNode(self, node: Node|TwoNode):
        if not node:
            print("Такого узла нет")
            return None
        
        cur = self.head
        if cur == node:
            self.head = cur.next
            if not self.head:
                print("Список пуст")

            return self.head
        
        while cur.next != node and cur.next is not None:
            cur = cur.next

        if cur.next == node:
            cur.next = cur.next.next
        else:
            print("Такого узла нет")
        
        return cur
    
    def addNode(self, nodeStart: Node|TwoNode, node: Node|TwoNode):
        cur = self.head
        if nodeStart.next:
            node.next = nodeStart.next
            nodeStart.next = node
        else:
            nodeStart.next = node

    def search(self, val):
        cur = self.head
        while cur is not None and cur.val != val:
            cur = cur.next
        if cur:
            return cur
        else:
            return None
    
    def addInBegin(self, node):
        self.addIndex(node, 0)

    def addInEnd(self, node):
        self.addIndex(node)
        
    def removeBegin(self):
        self.removeIndex(0)
    
    def removeEnd(self):
        self.removeIndex()

    
def testOneLink(lst = LinkedListOne(Node(1)), name = "Односвязный список", typeLst = 1):
    def convert(val):
        if typeLst == 1:
            return Node(val)
        else:
            return TwoNode(val)
        

    print(f"{name}:")

    # Заполнение
    for i in range(2, 9):
        lst.addInEnd(convert(i))
    showsp("Заполненный список: ", lst)


    lst.addInBegin(convert(0)) # Добавление в начало
    showsp("Добавление в начало (val = 0): ", lst)

    lst.addIndex(convert(15), 3) # Добавление по индексу
    showsp("Добавление по индексу (ind=3, val=15): ", lst)

    lst.removeBegin() # Удаление первого элемента
    showsp("Удаление первого элемента: ", lst)

    lst.removeEnd() # Удаление последнего
    showsp("Удаление последнего: ", lst)

    lst.removeIndex(2) # Удаление по индексу
    showsp("Удаление по индексу (ind=2): ", lst)

    
    showsp("Удаление узла (val = 15): ", lst)
    lst.removeNode(lst.search(15))

    lst.removeNode(lst.search(3))
    showsp("Удаление узла (val = 3): ", lst)

    lst.removeNode(lst.search(7))
    showsp("Удаление узла (val = 7): ", lst)

    lst.addNode(lst.search(6), convert(900))
    showsp("Добавление узла (после 6): ", lst)

    lst.addNode(lst.search(4), convert(901))
    showsp("Добавление узла (после 4): ", lst)

    lst.addNode(lst.search(6), convert(902))
    showsp("Добавление узла (после 6): ", lst)

    lst.addNode(lst.search(900), convert(903))
    showsp("Добавление узла (после 900): ", lst)
    
    print(f"3 есть в списке: {lst.search(3) is not None}")
    print(f"999 есть в списке: {lst.search(999) is not None}")


if __name__ == "__main__":  
    testOneLink()












