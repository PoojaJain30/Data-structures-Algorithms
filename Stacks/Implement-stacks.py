#implement Stack
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def __str__(self):
        return str(self.__dict__)
    
    def peek(self):
        return self.top.value 
    
    def push(self,value):
        new_Node = Node(value)
        if self.top == None:
            self.top = new_Node
            self.bottom = new_Node
        else:
            new_Node.next = self.top
            self.top = new_Node
        self.length += 1
        return self.printStack()
        
    def pop(self):
        if self.top == None:
            return None
        if self.top == self.bottom:
            self.bottom = None

        next_node = self.top.next
        self.top = next_node
        self.length -= 1
        return self.printStack()
        
            
    def printStack(self):
        stacks = []
        current_node = self.top
        while(current_node != None):
            stacks.append(current_node.value)
            current_node = current_node.next
        return stacks
            
my_stack = Stack()
my_stack.push(20)
my_stack.printStack()
my_stack.push(19)
my_stack.push(29)
my_stack.push(39)
my_stack.printStack()
my_stack.peek()
my_stack.pop()