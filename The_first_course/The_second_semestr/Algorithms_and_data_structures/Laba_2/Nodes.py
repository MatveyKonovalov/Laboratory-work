class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    


class TwoNode(Node):
    def __init__(self, val, prev = None, next = None):
        super().__init__(val, next)
        self.prev = prev
