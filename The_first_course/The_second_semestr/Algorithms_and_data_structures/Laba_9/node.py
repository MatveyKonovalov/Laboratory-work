class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return f"Node({self.value})"
    
    def __ptr__(self):
        return f"Node({self.value})"