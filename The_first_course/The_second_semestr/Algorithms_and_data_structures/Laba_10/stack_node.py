from record import Record
from hash_func import hash_func
from linked_list import LList

class RecordMap():
    def __init__(self, size: int = 128):
        self.__buckets = [None] * size
        self.capacity = 0

    def __hash_func(self, key: str) -> int:
        return hash_func(key) % len(self.__buckets)
    
    def __len__(self):
        return self.capacity
    
    def __return_bucket(self, key: str) -> LList:
        hash_ind = self.__hash_func(key)
        bucket = self.__buckets[hash_ind]
        return bucket
    
    def add(self, key: str, record: Record) -> bool:
        bucket = self.__return_bucket(key)
        if bucket is None:
            hash_ind = self.__hash_func(key)
            new_node = LList(key, record)
            self.__buckets[hash_ind] = new_node
            self.change_capacity()
            return True
        else:
            check = bucket.search(key)
            if check is None:
                bucket.add(key, record)
                self.capacity += 1
                return True
            return False
        
    def delete(self, key: str):
        bucket = self.__return_bucket(key)
        if bucket:
            self.capacity -= 1
            bucket.delete(key)
    
    def find(self, key: str):
        bucket = self.__return_bucket(key)
        if bucket:
            return bucket.search(key)
        return None
    
    def get_all(self) -> list[Record]:
        data = []
        for bucket in self.__buckets:
            if not bucket:
                continue
            for key, record in bucket:
                data.append(record)
        return data

    def __update_size(self):
        new_table = RecordMap(size=len(self.__buckets) * 2)
        for bucket in self.__buckets:
            if bucket:
                for key, value in bucket:
                    new_table.add(key, value)
        self.__buckets = new_table.__buckets
        self.capacity = new_table.capacity

    def change_capacity(self):
        self.capacity += 1
        if (self.capacity / len(self.__buckets)) > 0.7:
            self.__update_size()


class StackNode():
    def __init__(self, size: int = 128):
        self.uses_var = RecordMap(size=size)
        self.no_uses_var = RecordMap(size=size)

    def add(self, record: Record, is_use: bool):
        if is_use:
            is_add = self.uses_var.add(record.name, record)
            if is_add:
                record.used = True 
        else:
            is_add = self.no_uses_var.add(record.name, record)
        
        if not is_add:
            print(f"Exception: double declaration of '{record.name}'")

    def find(self, name_var: str) -> Record:
        record = self.uses_var.find(name_var)
        if record:
            return record
        return self.no_uses_var.find(name_var)

    def delete_var(self, name_var: str):
        self.uses_var.delete(name_var)
        self.no_uses_var.delete(name_var)

    def change_use_in(self, name_var: str):
        in_use = self.uses_var.find(name_var)
        in_no_use = self.no_uses_var.find(name_var)

        if not in_use and not in_no_use:
            print(f"Exception: var '{name_var}' not in node")
        elif in_use:
            # Уже используется - ничего не делаем
            pass
        elif in_no_use:
            # ✅ Переносим из no_uses в uses и обновляем флаг
            self.no_uses_var.delete(name_var)
            self.uses_var.add(name_var, in_no_use)
            in_no_use.used = True  # ✅ Важно: обновляем флаг в Record

    def get_no_use_in(self) -> list[Record]:
        return self.no_uses_var.get_all()
    
    def __len__(self):
        return len(self.no_uses_var) + len(self.uses_var)