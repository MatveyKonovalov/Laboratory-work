class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class TwoNode(Node):
    def __init__(self, val, prev = None, next = None):
        super().__init__(val, next)
        self.prev = prev



class LinkedListOne():
    
    def __init__(self, node: Node|TwoNode = None):
        self.head = node



    def show(self, delimiter = " -> "):
        cur = self.head
        while cur is not None:
            print(cur.val, end = delimiter)
            cur = cur.next
        print("None")


    def append(self, value):
        node = Node(value)
        self.addInEnd(node)


        
    def addIndex(self, node: Node|TwoNode, index=float("inf")):
        '''Добавление в начало .add(Node, 0), добавление в конец .add(Node)'''

        # Добавление в начало
        if not index or not self.head:
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

