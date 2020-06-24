#Implement HashTables: Concidering senarios for collision
# Big O for hash table is O(1) { O(n) in case of collision}
class ImplementHashTable:
    
    def __init__(self,length):
        self.length = length
        self.data = ['None']*self.length
        self.address = []
        print(self.data)
        
    def __str__(self):
        return str(self.__dict__)
    # hash function to gereate adress for the keys        
    def _hash(self,key):
        has = 0
        for i in key:
            has = (has + (ord(i))) % self.length
        return has

    # set key value by hashing the key       
    def setKey(self,key,value):
        get_addr = self._hash(key)
        if self.data[get_addr] == 'None':  
            self.data[get_addr] = []
        self.data[get_addr].append([key,value]) 
        self.address.append(get_addr)

    # get the value of given key 
    def getKey(self,key):
        get_addr = self._hash(key)
        current_bucket = self.data[get_addr]
        if current_bucket != 'None':
            for i in range(0,len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]

    #get an array of all the keys      
    def getAllkeys(self):
        keys = []
        for i in range(0,self.length):
            if self.data[i] != 'None':
                if len(self.data[i]) > 1:
                    for j in range(0,len(self.data[i])):
                        keys.append(self.data[i][j][0])
                else:
                    keys.append(self.data[i][0][0])
        return keys
    

myTable = ImplementHashTable(50)
myTable.setKey('grapes',1000)
myTable.setKey('banana',2000)
myTable.setKey('apple',0)
myTable.setKey('gra',10)
myTable.setKey('gr',80)
print(myTable.getKey('gr'))
print(myTable)
print(myTable.getAllkeys())