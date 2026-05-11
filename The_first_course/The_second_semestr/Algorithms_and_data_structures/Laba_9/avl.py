from node import Node

class AVLTree:
    def __init__(self, root: Node = None):
        self.root = root

    # Вспомогательные функции для AVL
    def get_height(self, node: Node) -> int:
        if not node:
            return 0
        return node.height 

    def update_height(self, node: Node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node: Node) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Правый поворот
    def rotate_right(self, y: Node) -> Node:
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2
    
        self.update_height(y)
        self.update_height(x)

        return x

    # Левый поворот
    def rotate_left(self, x: Node) -> Node:
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    # Балансировка узла
    def balance_node(self, node: Node) -> Node:
        if not node:
            return node

        self.update_height(node)

        balance = self.get_balance(node)

        # Левое поддерево тяжелее
        if balance > 1:
            if self.get_balance(node.left) < 0:
                # Левый-правый случай
                node.left = self.rotate_left(node.left)
            # Левый-левый случай
            return self.rotate_right(node)

        # Правое поддерево тяжелее
        if balance < -1:
            if self.get_balance(node.right) > 0:
                # Правый-левый случай
                node.right = self.rotate_right(node.right)
            # Правый-правый случай
            return self.rotate_left(node)

        return node

    def __insert(self, node: Node, value) -> Node:
        if node is None:
            return Node(value)
        
        if node.value < value:
            node.right = self.__insert(node.right, value)
        else:
            node.left = self.__insert(node.left, value)
        
        return self.balance_node(node)

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    # Поиск элемента
    @staticmethod
    def __find(node: Node, value):
        if not node:
            return None
        if node.value == value:
            return node
        elif node.value < value:
            return AVLTree.__find(node.right, value)
        else:
            return AVLTree.__find(node.left, value)

    def find(self, value):
        return AVLTree.__find(self.root, value)

    @staticmethod
    def __find_min(node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    def __delete_node(self, node: Node, value) -> Node:
        if not node:
            return None
        
        if value < node.value:
            node.left = self.__delete_node(node.left, value)
        elif value > node.value:
            node.right = self.__delete_node(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            temp = AVLTree.__find_min(node.right)
            node.value = temp.value
            node.right = self.__delete_node(node.right, temp.value)
        
        return self.balance_node(node)

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)





    
  


    
  
    