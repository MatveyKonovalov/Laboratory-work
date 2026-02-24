from linkedOne import LinkedListOne
from Nodes import Node

def expandList(head: Node, k: int):

    if not head:
        return None
    # Если разворот делать не нужно, возвращаем голову
    if k <= 1:
        return head
    
    
    cur = head # Указатель на текущий узел
    res = None # Ссылка на новую голову
    lastG = None # Указатель на текущий хвост

    while cur:

        newHead = None # Голова новой группы
        lastL = None # Ссылка на следующую группу для новой группы

        # Проверка, есть ли к узлов для поворота
        curCheck = cur
        cntCheck = 0
        while curCheck is not None and cntCheck < k:
            cntCheck += 1
            curCheck = curCheck.next
        
        
        if not curCheck and cntCheck != k:
            if not res:
                res = head
            else:
                lastG.next = cur
            return res
        
        # Если есть, то делаем поворот
        for _ in range(k):
            if not newHead:
                newHead = cur
                lastL = cur # Сохраняем хвост новой группы
                cur = cur.next
                
            else:
                nextNode = cur.next # Сохраняем ссылку на следующий элемент
                cur.next = newHead 
                newHead = cur
                cur = nextNode

        if not res:
            res = newHead
            lastG = lastL
        else:
            lastG.next = newHead # Присоединяем новую группу
            lastG = lastL # Меняем значение хвоста

        if not lastG:
            break
        else:
            lastG.next = None


    return res




def makeList(n: int):
    # Создание списка для тестов
    inputData = LinkedListOne(Node(1))
    for i in range(2, n + 1):
        inputData.addIndex(Node(i))
    return inputData


def showResult(k: int):
    inputData = makeList(6)
    new_head = expandList(inputData.head, k)
    
    print(f"Для k = {k}: ", end="")
    cur = new_head
    while cur is not None:
        print(cur.val, end=' -> ')
        cur = cur.next
    print(None)

def main():
    # Если кол-во узлов кратное
    showResult(3)

    # Если некратное
    showResult(4)

if __name__ == "__main__":
    main()