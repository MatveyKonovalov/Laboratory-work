from linkedOne import LinkedListOne
from Nodes import Node
from task2 import expandList, makeList

def is_pal(root: LinkedListOne):

    size = 0
    cur = root.head

    # Определение размера
    while cur is not None:
        cur = cur.next
        size += 1

    med = size // 2

    cur = root.head
    while med:
        med -= 1
        cur = cur.next
    if size % 2 == 1:
        cur = cur.next

    # Переворачиваем вторую половину за O(n)
    med = size // 2
    newHead = expandList(cur, med)
    cur = root.head

    while med > 0:
        if newHead.val != cur.val:
            return False
        med -= 1
        newHead = newHead.next
        cur = cur.next
    return True



def main():
    root = LinkedListOne(Node(1))
    root.addIndex(Node(2))
    root.addIndex(Node(3))
    root.addIndex(Node(2))
    root.addIndex(Node(1))

    root.show()
    print(f"Для симметричного: {is_pal(root)}\n\n")
    
    root = makeList(6)
    root.show()
    print(f"Для не симметричного: {is_pal(root)}")

if __name__ == "__main__":
    main()
