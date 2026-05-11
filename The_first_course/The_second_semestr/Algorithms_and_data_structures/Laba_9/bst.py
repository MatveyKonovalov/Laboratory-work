from node import Node

class BinarySearchTree:
    def __init__(self, root: Node = None):
        self.root = root

    # Вставка в дерево
    def __insert(self, node: Node, value):
        if node is None:
            self.root = Node(value)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value)
                return
            self.__insert(node.right, value)
        else:
            if node.left is None:
                node.left = Node(value)
                return
            self.__insert(node.left, value)

    def insert(self, value):
        self.__insert(self.root, value)

    # Поиск элемента
    @staticmethod
    def __find(node: Node, value):
        if not node:
            return None
        if node.value == value:
            return node
        elif node.value < value:
            return BinarySearchTree.__find(node.right, value)
        else:
            return BinarySearchTree.__find(node.left, value)

    def find(self, value):
        return BinarySearchTree.__find(self.root, value)

    # Удаление из дерева
    @staticmethod
    def __find_min_and_delete(parent: Node, node: Node):
        current = node
        prev = parent
        
        while current.left:
            prev = current
            current = current.left
        
        if prev.left == current:
            prev.left = current.right
        else:
            prev.right = current.right
        
        
        current.left = None
        current.right = None
        return current

    @staticmethod
    def __search_parent(root: Node, child: Node):
        if not root or not child or root == child:
            return None
        
        if root.left == child or root.right == child:
            return root
        elif root.value < child.value:
            return BinarySearchTree.__search_parent(root.right, child)
        else:
            return BinarySearchTree.__search_parent(root.left, child)

    def delete_node(self, value):
        node = self.find(value)
        if not node:
            return None
        
        parent = BinarySearchTree.__search_parent(self.root, node)
        
        if not parent:
            if not node.left and not node.right:
                self.root = None
            elif not node.left:
                self.root = node.right
            elif not node.right:
                self.root = node.left
            else:
                min_node = BinarySearchTree.__find_min_and_delete(node, node.right)
                min_node.left = node.left
                min_node.right = node.right
                self.root = min_node
            return None
        
        if not node.left and not node.right:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        
        elif not node.left:
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
        elif not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        
        else:
            min_node = BinarySearchTree.__find_min_and_delete(node, node.right)
            min_node.left = node.left
            min_node.right = node.right
            
            if parent.left == node:
                parent.left = min_node
            else:
                parent.right = min_node
        
        return None
    
 
