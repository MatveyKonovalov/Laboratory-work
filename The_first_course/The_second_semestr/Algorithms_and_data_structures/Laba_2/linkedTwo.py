from Nodes import *
from linkedOne import *
from showlst import *

class LinkedListTwo(LinkedListOne):

    def show(self, delimiter=" <-> "):
        print("None", end=delimiter)
        super().show(delimiter)

    def addIndex(self, node: TwoNode, index=float("inf")):
        cur = super().addIndex(node, index)
        
        if cur is not None:
            cur.next.prev = cur
            if cur.next.next is not None:
                cur.next.next.prev = cur.next

    def removeIndex(self, index=float('inf')):
        cur = super().removeIndex(index)
        if cur is None:
            if self.head is not None:
                self.head.prev = None
            return
        
        if cur.next is not None:
            cur.next.prev = cur

    
    def addNode(self, nodeStart: TwoNode, nodeNext: TwoNode):
        super().addNode(nodeStart, nodeNext)
        nodeNext.prev = nodeStart

    def removeNode(self, node: TwoNode):
        if node is None:
            print("Такого узла нет")
            return None
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = node.next
            self.head.prev = None
    
    def showLinks(self):
        cur = self.head
        index = 0
        ans = "Индекс: {}\nЗначение: {}\nprev: {}\nnext: {}\n"

        # Связи головы
        print(ans.format(index, cur.val, None, cur.next.val))

        # Связи остальных
        cur = cur.next
        while cur != None:
            index += 1
            if cur.next is None:
                print(ans.format(index, cur.val, cur.prev.val, None))
            else:
                print(ans.format(index, cur.val, cur.prev.val, cur.next.val))
            cur = cur.next




def test(lst = LinkedListTwo(TwoNode(1)), name = "Двусвязный список"):
    testOneLink(lst, name, 2)
    
    print("\n\n\nДемонстрация связей: ")
    lst.showLinks()


if __name__ == "__main__":
    test()