#Implement array and array methods 
#BIG O for Lookup,Push,Pop items is O(1) and for inserting and deleting item from any index is O(n).

class ImplementArray:
    
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self):
        return str(self.__dict__)
    
    # access element from an index   
    def getItem(self,index):
        return self.data[index]
    
    #add element at the end
    def pushItem(self,item):
        self.length += 1
        self.data[self.length-1] = item
    
    #remove the element from the end
    def popItem(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem
    
    #Remove element at given index
    def removeAtIndex(self,index):
        #index given, shift element from index to end of list one position forward 
        self.shiftItemsLeft(index)
        
    #Shift elements to left from the given index    
    def shiftItemsLeft(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
     
    #Add element at given index
    def addAtIndex(self,index,item):
        #insert element at given index , increase length by 1 and shift all element from index to right
        self.shiftItemsRight(index,item)
        self.data[index] = item
        
    #Shift elements to rigth from the given index   
    def shiftItemsRight(self,index,item):
        self.length += 1
        self.data[self.length-1] = ''
        for i in range(self.length-1,index,-1):
            self.data[i]= self.data[i-1]    

            
           
my_arr = ImplementArray()
print(my_arr)
my_arr.pushItem('hi')
my_arr.pushItem('hello')
my_arr.pushItem('holla')
my_arr.pushItem('heya')
print(my_arr)
print(my_arr.getItem(2))
my_arr.popItem()
print(my_arr)
my_arr.pushItem('heya')
print(my_arr)
my_arr.removeAtIndex(1)
print(my_arr) 
my_arr.addAtIndex(2,'hey')
print(my_arr)