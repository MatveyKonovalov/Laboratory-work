from linked_list import LList
from hash_func import hash_func
from stack_node import StackNode
from record import Record


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        self.__check()
        return self.__stack.pop()
    
    def peek(self):
        if self.is_empty(): 
            return None
        return self.__stack[-1]
    
    def is_empty(self) -> bool:
        return len(self.__stack) == 0
    
    def __check(self):
        if not self.__stack:
            raise IndexError("Стек пуст")
    
    def get_all(self) -> list:
        return self.__stack.copy()
    
    def __len__(self):
        return len(self.__stack)
    
    def __iter__(self):
        for scope in range(len(self.__stack) - 1, -1, -1):
            yield self.__stack[scope]


class Table:
    def __init__(self, size: int = 16):
        if size <= 0:
            raise ValueError("Incorrect size: size must >= 0")
        self.__buckets = [None] * size # Бакеты: ключ - имя области, значение StackNode
        self.capacity = 0 # Заполняемость
        self.scope_stack = Stack()  # Стек областей

    def __hash_func(self, key: str) -> int:
        return hash_func(key) % len(self.__buckets)

    def change_capacity(self):
        self.capacity += 1
        # Обновление размера таблицы при выскокой заполняемости
        if (self.capacity / len(self.__buckets)) > 0.7:
            self.__update_size()

    def __return_bucket(self, key: str) -> LList:
        hash_ind = self.__hash_func(key)
        return self.__buckets[hash_ind]

    
    def enter_scope(self, scope_name: str):
        self.scope_stack.push(scope_name)

    
    def exit_scope(self):
        if self.scope_stack.is_empty():
            return
        scope_name = self.scope_stack.pop()
        self.delete_zone(scope_name)

    def current_scope(self) -> str:
        return self.scope_stack.peek()

    def add(self, scope: str, record: Record, is_use: bool = False):
        bucket = self.__return_bucket(scope)

        if not bucket:
            new_stack_node = StackNode()
            new_stack_node.add(record=record, is_use=is_use)
            hash_ind = self.__hash_func(scope)
            new_llist = LList(head_key=scope, head_value=new_stack_node)
            self.__buckets[hash_ind] = new_llist
        else:
            stackNode = self.__search_in(bucket, scope)
            if stackNode:
                existing = stackNode.find(record.name)
                if existing:
                    print(f"Ошибка: повторное объявление '{record.name}' в области '{scope}' (строка {record.line})")
                    return False
                stackNode.add(record, is_use)
            else:
                new_stack_node = StackNode()
                new_stack_node.add(record=record, is_use=is_use)
                bucket.add(scope, new_stack_node)

        self.change_capacity()
        return True

    @staticmethod
    def __search_in(list_zones: LList, zone_name: str) -> StackNode:
        for key, stackNode in list_zones:
            if key == zone_name:
                return stackNode
        return None

    def __search_stack_node(self, zone) -> StackNode:
        bucket = self.__return_bucket(zone)
        if bucket:
            return self.__search_in(bucket, zone)
        return None

    # Поиск с учётом вложенности (от текущей к глобальной)
    def find_recursive(self, name_var: str) -> Record:
        for scope in self.scope_stack:
            record = self.find(scope, name_var)
            if record:
                return record
        return None

    # Поиск только в указанной области
    def find(self, scope: str, name_var: str) -> Record:
        stackNode = self.__search_stack_node(scope)
        if stackNode:
            return stackNode.find(name_var)
        return None

    def delete_zone(self, scope: str):
        bucket = self.__return_bucket(scope)
        if bucket:
            stack_node = bucket.search(scope)
            if stack_node:
                self.capacity -= len(stack_node)
            bucket.delete(scope)

    def delete_var(self, scope: str, name_var: str):
        stackNode = self.__search_stack_node(scope)
        if stackNode:
            self.capacity -= 1
            stackNode.delete_var(name_var)

    def change_use_in(self, scope: str, name_var: str):
        stackNode = self.__search_stack_node(scope)
        if stackNode:
            stackNode.change_use_in(name_var)
        else:
            print(f"Exception: var '{name_var}' not in node")

    def get_no_use_in(self, scope: str) -> list[Record]:
        stackNode = self.__search_stack_node(scope)
        if stackNode:
            return stackNode.get_no_use_in()
        return []

    def __add_stackNode(self, key: str, stackNode: StackNode):
        bucket = self.__return_bucket(key)
        if bucket is None:
            hash_ind = self.__hash_func(key)
            new_list = LList(key, stackNode)
            self.__buckets[hash_ind] = new_list
        else:
            bucket.add(key, stackNode)

    def __update_size(self):
        new_table = Table(size=len(self.__buckets) * 2)
        for scope in self.scope_stack.get_all():
            new_table.enter_scope(scope)
        
        for bucket in self.__buckets:
            if bucket:
                for key, value in bucket:
                    new_table.__add_stackNode(key, value)
        
        self.__buckets = new_table.__buckets
        self.capacity = new_table.capacity
        self.scope_stack = new_table.scope_stack


    def __len__(self) -> int:
        return self.capacity
    
    
    def get_stats(self):
        return {
            'buckets': len(self.__buckets),
            'records': self.capacity,
            'load_factor': self.capacity / len(self.__buckets) if len(self.__buckets) > 0 else 0,
            'active_scopes': len(self.scope_stack),
            'current_scope': self.current_scope()
        }