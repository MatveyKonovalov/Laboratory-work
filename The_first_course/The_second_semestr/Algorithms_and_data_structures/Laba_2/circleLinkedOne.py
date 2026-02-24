from Nodes import *
from linkedOne import testOneLink
from showlst import *

class CircleLinkedOne():


    def __init__(self, head):
        self.head = head
        self.head.next = head

    def addIndex(self, node, index=float("inf")):
        cur = self.head
        if index == 0:
            cur = cur.next
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node
            self.head = node
            return cur
        
        if index == 1:
            node.next = cur.next
            cur.next = node
            return cur

        cur = cur.next
        curIndex = 1
        
        while curIndex != index - 1 and cur.next != self.head:
            cur = cur.next
            curIndex += 1
        
        if cur.next == self.head:
            node.next = self.head
            cur.next = node
        else:
            node.next = cur.next
            cur.next = node
        
        return cur

    
    def addNode(self, nodeStart: Node|TwoNode, node: Node|TwoNode):
        node.next = nodeStart.next
        nodeStart.next = node


    def removeIndex(self, index = float('inf')):
        cur = self.head

        if not index:
            cur = cur.next
            if cur == self.head:
                cur = None
                print("List is empty")
                return None
            
            while cur.next != self.head:
                cur = cur.next
            
            cur.next = cur.next.next
            self.head = self.head.next
            return cur
        

        if index == 1:
            cur.next = cur.next.next
            return cur
        
        curIndex = 1
        cur = cur.next

        while curIndex < index - 1 and cur.next.next != self.head:
            curIndex += 1
            cur = cur.next
        
        if cur.next.next == self.head:
            cur.next = self.head

        else:
            cur.next = cur.next.next

        return cur
        

    

    def search(self, val):
        cur = self.head

        if cur.val == val:
            return cur
        
        cur = cur.next

        while cur != self.head:
            if cur.val == val:
                return cur
            cur = cur.next
            
        return None


    def removeNode(self, node: Node|TwoNode):
        cur = self.head

        # Удаление головного узла
        if node == self.head:

            if cur.next == self.head:
                self.head = None
                print("List is empty")
                return None
            
            while cur.next != self.head:
                cur = cur.next

            self.head = self.head.next
            cur.next = self.head
            return cur
    
        # Удаляем второй узел (после головы)
        if cur.next == node:
            cur.next = cur.next.next
            return cur
    
        # Удаляем узел в середине или в конце
        cur = cur.next
    
        # Ищем узел, до удаляемго
        while cur.next != node and cur.next != self.head:
            cur = cur.next
    
        # Нашли узел, который нужно удалить
        if cur.next == node:
            cur.next = cur.next.next
        else:
            print("Узел не найден")
            return -1

        return cur


    
    def show(self, delimiter=" -> "):
        """Отображает все элементы списка"""
        if self.head is None:
            print("Список пуст")
            return
        
        current = self.head
        print("Начало списка: ", end="")
        
        while True:
            print(current.val, end=delimiter)
            current = current.next
            if current == self.head:
                break
        
        print("(возврат к началу)")



def main():
    testOneLink(CircleLinkedOne(Node(1)))



if __name__ == "__main__":
    main()