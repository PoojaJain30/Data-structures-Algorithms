#Implement Binary Search Tree

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
class BST:
    
    def __init__(self):
        self.root = None
        
    def __str__(self):
        return str(self.__dict__)
    
    
    #insert value in the tree
    def insert(self,value):
        new_node = Node(value)
        #first(root)node
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value :
                    #left
                    if current_node.left == None:
                        current_node.left = new_node
                        return current_node
                    else:
                        current_node = current_node.left
                elif value >= current_node.value :
                    #right
                    if current_node.right == None:
                        current_node.right = new_node
                        return current_node
                    else:
                        current_node = current_node.right
                        
    #find whether value exists in the tree or not
    def lookup(self,value):
        current_node = self.root
        while True:
            if current_node == None:
                return False
            elif current_node.value == value:
                return True
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
               
    #print tree 
    def printt(self,curr_node):
        if curr_node != None:
                self.printt(curr_node.left)
                print(str(curr_node.value))
                self.printt(curr_node.right)

my_tree = BST()
my_tree.insert(9) 
#print(my_tree.root.value)
#my_tree.printTree()
my_tree.insert(4)
my_tree.insert(20)
my_tree.insert(1)
my_tree.insert(6)
my_tree.insert(15)
my_tree.insert(170)
my_tree.printt(my_tree.root)
my_tree.lookup(15)