class Stack:
    def __init__(self):
        self.stack = []

    def append(self, element):
        self.stack.append(element)

    def pop(self):
        self.__check()
        return self.stack.pop()
    
    def peek(self):
        self.__check()
        return self.stack[-1]
        
    
    def __check(self):
        if not self.stack:
            raise IndexError("Стек пуст")
        
    def get_element(self):
        return self.stack