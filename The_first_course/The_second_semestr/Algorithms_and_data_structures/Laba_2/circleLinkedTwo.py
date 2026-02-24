from Nodes import TwoNode
from circleLinkedOne import CircleLinkedOne
from linkedTwo import test

class CircleLinkedTwo(CircleLinkedOne):
    def __init__(self, head: TwoNode):
        super().__init__(head)
        self.head.prev = head

    def addNode(self, nodeStart, node):
        super().addNode(nodeStart, node)

        # Добавление обратных связей
        node.next.prev = node
        node.prev = nodeStart

    def removeNode(self, node):
        cur = super().removeNode(node)

        # Если список был полностью удалён
        if not cur:
            return None
        
        # Если узел не был найден
        if cur == -1:
            return
        
        # Добавление оьратной связи
        cur.next.prev = cur

    def show(self):
        super().show(delimiter=" <-> ")



    def showLinks(self):

        cur = self.head
        index = 0
        ans = "Номер: {}\nЗначение: {}\nprev: {}\nnext: {}\n"

        # Связи головы
        print(ans.format(index, cur.val, cur.prev.val, cur.next.val))

        # Связи остальных
        cur = cur.next
        while cur != self.head:
            index += 1
            print(ans.format(index, cur.val, cur.prev.val, cur.next.val))
            cur = cur.next



    def addIndex(self, node, index=float("inf")):
        # cur - узел, до добавляемого узла
        cur = super().addIndex(node, index)

        # Добавление обратных связей
        node.prev = cur
        node.next.prev = node

    def removeIndex(self, index=float("inf")):
        # cur - узел, до удаляемого узла
        cur = super().removeIndex(index)

        # Добавление обратных связей
        if cur is None:
            return
        
        cur.next.prev = cur


def main():
    test(CircleLinkedTwo(TwoNode(1)))

if __name__ == "__main__":
    main()