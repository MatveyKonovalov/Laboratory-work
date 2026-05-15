from node import Node


class LList:
    def __init__(self, head_key = None, head_value = None):
        if head_key:
            self.head = Node(head_key, head_value)
        else:
            self.head = None

    def add(self, key, value):
        node = Node(key, value)
        node.next = self.head
        self.head = node

    def search(self, key):
        cur = self.head

        while cur and cur.key != key:
            cur = cur.next
        
        if cur:
            return cur.value
        return None
    
    def delete(self, key):
        cur = self.head

        if not cur:
            return None
        
        if cur.key == key:
            tmp = self.head
            self.head = self.head.next
            return tmp
        
        if cur.next:
            while cur.next and cur.next.key != key:
                cur = cur.next

            if not cur.next:
                return None
            tmp = cur.next
            cur.next = cur.next.next
            return tmp
        else:
            return None
        
    def __iter__(self):
        cur = self.head
        while cur:
            yield (cur.key, cur.value)
            cur = cur.next
    