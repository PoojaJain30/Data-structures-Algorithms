#Implement LinkedList

class ImplementLinkedList:
    
    def __init__(self,value):
        self.head = {
            'value':value,
            'next': None  
        }
        self.tail = self.head
        self.length = 1
        
    def __str__(self):
        return str(self.__dict__)
    
    #insert a node at the beginning 
    def prependNode(self,value):
        new_node = {
            'value':value,
            'next': None 
            }
        print(self.head)
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1
        return self.printList()
    
    #insert a node at the end 
    def appendNode(self,value):
        new_node = {
            'value':value,
            'next': None 
            }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self.printList()
    
    #print linkedlist as a list 
    def printList(self):
        linkedlist = []
        current_node = self.head
        while(current_node != None):
            linkedlist.append(current_node['value'])
            current_node = current_node['next']
        return linkedlist
    
    #insert node at the given index
    def insertNode(self,index,value):
        if (index < 0):
            print("Error: Index can't be negative")
        if(index == 0):
            print("index 0")
            return self.prependNode(value)
        if(index >= self.length):
            return self.appendNode(value)
        
        new_node = {
            'value':value,
            'next': None 
            }
        leading_node = self.getIndexNode(index-1)
        trailing_node = leading_node['next']
        leading_node['next'] = new_node
        new_node['next'] = trailing_node
        self.length += 1
        return self.printList()
    
    #get the current node based on index        
    def getIndexNode(self,index):
        counter = 0
        current_node = self.head
        while(counter != index):
            current_node = current_node['next']
            counter +=1
        return current_node
    
    #remove node at the given index
    def removeNode(self,index):
        if (index < 0):
            print("Error: Index can't be negative")
        leading_node = self.getIndexNode(index-1)
        removing_node = leading_node['next']
        leading_node['next'] = removing_node['next']
        self.length -= 1
        return self.printList()
    
    
    
my_list = ImplementLinkedList(10)
my_list.prependNode(5)
my_list.appendNode(15)
my_list.printList()
my_list.prependNode(1)
my_list.printList()
my_list.insertNode(2,8)
my_list.insertNode(0,9)
my_list.insertNode(1,19)
my_list.insertNode(21,19)
my_list.printList()
my_list.removeNode(1)
my_list.printList()

