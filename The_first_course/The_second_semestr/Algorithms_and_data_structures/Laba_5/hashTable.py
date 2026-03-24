from linkedlist import LinkedListOne

class HashTable:
    def __init__(self, size: int):
        self._buckets = [None] * size
        self._cnt_zap_column = 0

    def _hash_func(self, key):
        return sum(ord(c) for c in str(key)) % len(self._buckets)
    
    def add(self, key, value):
        index = self._hash_func(key)
        
        if self._buckets[index] is None: # Если бакет пустой
            self._buckets[index] = LinkedListOne((key, value))
            self._cnt_zap_column += 1
        
        else:
            place = self._buckets[index]
            t_place = place.search(key) 
            if t_place is None: 
                place.add(key, value)
            else:
                # Если уже имеется элемент с таким ключом делаем перезапись
                t_place.val = (key, value)

    def get(self, key):
        index = self._hash_func(key)
        
        if self._buckets[index] is None:
            raise KeyError("Такого ключа нет")
        
        t_place = self._buckets[index].search(key) 
        if t_place:
            return t_place.val[1]
        raise KeyError("Такого ключа нет")
        
    def del_pair(self, key):
        index = self._hash_func(key)

        if self._buckets[index] is not None:
            # print("success")
            if self._buckets[index].remove(key) == "Head is empty":
                self._cnt_zap_column -= 1

    def return_k(self):
        return f"{self._cnt_zap_column / len(self._buckets):.4f}"

    def new_size(self, new_size: int):
        new_hash_table = HashTable(new_size)
        for bucket in self._buckets:
            if bucket:
                for key, value in bucket:
                    new_hash_table.add(key, value)
        
        self._buckets = new_hash_table._buckets
        self._cnt_zap_column = new_hash_table._cnt_zap_column


def test():
    table1 = HashTable(10)
    
    for i in range(100):
        table1.add(i, "a" * i)


    print(table1.return_k())

    for i in range(10):
        table1.del_pair(i)
        try:
            print(table1.get(i))
        except KeyError:
            # Удаление кидает исключение 
            print(f"Success: {i}")

    table1.new_size(110)
    print(table1.return_k())

    

if __name__ == "__main__":
    test()
    
    
        




