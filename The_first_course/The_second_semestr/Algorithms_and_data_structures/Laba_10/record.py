class Record:
    def __init__(self, name: str, var_type: str, line: int, scope: str, *another):
        self.name = name
        self.type_name= var_type   
        self.line = line          
        self.scope = scope         
        self.used = False          
        self.another = another

    def check_vision(self, current):
        return self.vision == current
    
    def __str__(self):
        return f"Record({self.name}, {self.type_name}, {self.notification}, {self.another})"
    
    def __ptr__(self):
        return f"Record({self.name}, {self.type_name}, {self.notification}, {self.another})"
    
