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
            if cur.next.next is not None:
                cur.next.next.prev = cur

    
    def addNode(self, nodeStart: TwoNode, nodeNext: TwoNode):
        super().addNode(nodeStart, nodeNext)
        nodeNext.prev = nodeStart

    def removeNode(self, node: TwoNode):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = node.next
    
    def showLinks(self):
        cur = self.head
        index = 0
        ans = "Номер: {}\nЗначение: {}\nprev: {}\nnext: {}\n"

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




def test(lst = LinkedListTwo(TwoNode(1))):

    for i in range(2, 10):
        lst.addIndex(TwoNode(i))
    lst.show()
    lst.showLinks()
    lst.addIndex(TwoNode(90), 1)
    showsp("Добавление по индексу(val = 90, ind=1): ", lst)

    lst.addIndex(TwoNode(0), 0)
    showsp("Добавление по индексу(val = 0, ind=0): ", lst)

    lst.removeIndex(0)
    showsp("Удаление первого: ", lst)

    lst.removeIndex()
    showsp("Удаление последнего: ", lst)

    lst.removeIndex(1)
    showsp("Удаление по индексу (1): ", lst)

    lst.removeNode(lst.search(1))
    showsp("Удаление по узлу(первому): ", lst)


    lst.removeNode(lst.search(6))
    showsp("Удаление по узлу(val=6): ", lst)


    lst.addNode(lst.search(2), Node(900))
    showsp("Добавление узла (2): ", lst)

    lst.addNode(lst.search(5), Node(900))
    showsp("Добавление узла (5): ", lst)

    lst.addNode(lst.search(8), Node(900))
    showsp("Добавление узла (8): ", lst)

    # lst.showLinks(lst.head)
    print(f"2 есть в списке: {lst.search(2) is not None}")
    print(f"680 есть в списке: {lst.search(680) is not None}")


if __name__ == "__main__":
    test()