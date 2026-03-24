from Nodes import Node

class LinkedListOne():
    
    def __init__(self, value):
        self.head = Node(value)



    def add(self, key, value):
        value = (key, value)
        node = Node(value)

        if self.head is None:
            self.head = node
            return 
        
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = node


    def remove(self, key):
        cur = self.head
        if self.head is None:
            return "Backet is empty"
        while cur.next is not None and cur.next.val[0] != key:
            cur = cur.next


        if self.head.val[0] == key:
            self.head = self.head.next

        elif cur.next is not None and cur.next.val[0] == key:
            cur.next = cur.next.next
        if self.head is None:
            return "Head is empty"

    def search(self, key):
        cur = self.head
        while cur is not None and cur.val[0] != key:
            cur = cur.next
        if cur:
            return cur
        else:
            return None
        
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.val
            cur = cur.next
    

        
        
    

    













