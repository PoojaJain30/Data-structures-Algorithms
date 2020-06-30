#Implement with Array / Lists

class Stack:
    def __init__(self):
        self.array = []
        
    def __str__(self):
        return str(self.__dict__)
    
    def peek(self):
        return self.array[len(self.array)-1]
    
    def push(self,value):
        self.array.append(value)
        return self.array
        
    def pop(self):
        self.array.pop(len(self.array)-1)
        return self.array
        
            
   
            
my_stack = Stack()
my_stack.push(20)
my_stack.push(19)
my_stack.push(29)
my_stack.push(39)
my_stack.peek()
my_stack.pop()