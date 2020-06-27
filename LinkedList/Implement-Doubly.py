#implement Doubly linked list
class ImplementDoublyLinkedList:
    
    def __init__(self,value):
        self.head = {
            'value':value,
            'next': None,
            'prev': None
        }
        self.tail = self.head
        self.length = 1
        
    def __str__(self):
        return str(self.__dict__)
    
    #insert a node at the beginning 
    def prependNode(self,value):
        new_node = {
            'value':value,
            'next': None,
            'prev': None
            }
        print(self.head)
        new_node['next'] = self.head
        self.head['prev'] = new_node
        self.head = new_node
        self.length += 1
        return self.printList()
    
    #insert a node at the end 
    def appendNode(self,value):
        new_node = {
            'value':value,
            'next': None,
            'prev': None
            }
        self.tail['next'] = new_node
        new_node['prev'] = self.tail
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
            'next': None, 
            'prev': None
            }
        leading_node = self.getIndexNode(index-1)
        trailing_node = leading_node['next']
        leading_node['next'] = new_node
        trailing_node['prev'] = new_node
        new_node['prev'] = leading_node
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
        trailing_node = removing_node['next']
        leading_node['next'] = trailing_node
        trailing_node['prev'] = leading_node
        self.length -= 1
        return self.printList()
    

new_list = ImplementDoublyLinkedList(20)
#print(new_list)
new_list.printList()
new_list.prependNode(18)
#print(new_list)
new_list.prependNode(10)
new_list.appendNode(6)
new_list.insertNode(2,12)
new_list.removeNode(3)