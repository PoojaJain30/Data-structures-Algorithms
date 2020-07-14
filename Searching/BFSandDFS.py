#Implement Binary Search Tree traversal using Breadth first search and depth first serach (inorder,preorder,postorder)

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
                
    # breadth first traversal         
    def breadth_first_traversal(self):
        queue = []
        lis = []
        current_node = self.root
        queue.append(current_node)
        while(len(queue) > 0):
            current_node = queue.pop(0)
            lis.append(current_node.value)
            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)
        return lis
    #depth first traversal
    def inorder(self,node,lis):
        if (node.left != None):
            self.inorder(node.left,lis)
        lis.append(node.value)
        if (node.right != None):
            self.inorder(node.right,lis)    
        return lis
    
    def preorder(self,node,lis):
        lis.append(node.value)
        if (node.left != None):
            self.preorder(node.left,lis)
        if (node.right != None):
            self.preorder(node.right,lis)    
        return lis
    
    def postorder(self,node,lis):
        if (node.left != None):
            self.postorder(node.left,lis)
        if (node.right != None):
            self.postorder(node.right,lis) 
        lis.append(node.value)
        return lis
    
    def dfs_inorder(self):
        return self.inorder(self.root,[])
    
    def dfs_preorder(self):
        return self.preorder(self.root,[])
    
    def dfs_postorder(self):
        return self.postorder(self.root,[])
    
   
            
            

my_tree = BST()
my_tree.insert(9) 
my_tree.insert(4)
my_tree.insert(20)
my_tree.insert(1)
my_tree.insert(6)
my_tree.insert(15)
my_tree.insert(170)
my_tree.printt(my_tree.root)
#my_tree.lookup(15)
print("BFS",my_tree.breadth_first_traversal())
print("DFS-In",my_tree.dfs_inorder())
print("DFS-Pre",my_tree.dfs_preorder())
print("DFS-Post",my_tree.dfs_postorder())
