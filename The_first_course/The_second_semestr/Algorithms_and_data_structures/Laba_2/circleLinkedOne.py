from Nodes import *
from linkedOne import testOneLink, LinkedListOne
from showlst import *

class CircleLinkedOne(LinkedListOne):


    def __init__(self, head):
        self.head = head
        self.tail = head
        if head:
            self.head.next = head

    def addIndex(self, node, index=float("inf")):
        cur = self.head

        if index == 0:
            self.tail.next = node
            node.next = self.head
            self.head = node

            # Узел до новой головы
            return self.tail
        
        if index == 1 and self.tail != self.head:
            # Если хвост не совпадает с головой
            node.next = cur.next
            cur.next = node
            return cur
        
        elif index == 1:
            # Если хвост совпадает с головой
            self.head.next = node
            node.next = self.head
            self.tail = node

        cur = cur.next
        curIndex = 1
        
        while curIndex != index - 1 and cur.next != self.head:
            cur = cur.next
            curIndex += 1
        
        if cur.next == self.head:
            # Вставка в конец, меняем хвост
            self.tail.next = node
            node.next = self.head
            self.tail = node
        else:
            node.next = cur.next
            cur.next = node
        
        return cur

    
    def addNode(self, nodeStart: Node|TwoNode, node: Node|TwoNode):
        # Если вставляем после хвоста
        if nodeStart.next == self.head:
            self.tail = node
        node.next = nodeStart.next
        nodeStart.next = node


    def removeIndex(self, index = float('inf')):
        cur = self.head

        if not index:
            cur = cur.next
            if self.head == self.tail:
                # Если хвост совпадает с головой
 
                self.head = self.tail = None
                print("Список пуст")
                return None
            
            self.tail.next = self.head.next
            self.head = self.head.next
            return cur
        

        if index == 1:
            if self.tail == self.head:
                self.tail = self.head = None
                print("Список пуст")
                return None
            
            cur.next = cur.next.next
            return cur
        
        curIndex = 1
        cur = cur.next

        while curIndex < index - 1 and cur.next.next != self.head:
            curIndex += 1
            cur = cur.next
        
        if cur.next.next == self.head:
            cur.next = self.head
            self.tail = cur

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

            if self.tail == self.head:
                self.tail = self.head = None
                print("Список пуст")
                return None
            
            self.head = self.tail = self.head.next
            return self.tail
    
        # Удаляем второй узел (после головы)
        if cur.next == node:
            if self.tail == node:
                # Если в списке всего 2 элемента
                self.tail = cur

            cur.next = cur.next.next
            return cur
    
        # Удаляем узел в середине или в конце
        cur = cur.next
    
        # Ищем узел, до удаляемго
        while cur.next != node and cur.next != self.head:
            cur = cur.next
    
        # Нашли узел, который нужно удалить
        if cur.next == node:
            if self.tail == node:
                self.tail = cur

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
    testOneLink(CircleLinkedOne(Node(1)), "Односвязный циклический список")



if __name__ == "__main__":
    main()