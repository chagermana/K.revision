#binary search tree
# each node has at most two children: a left and a right
#the left child contains a value smaller than the current node
#the right child contains a value larger than the current node
#it keeps things sorted for fast searching,insertion and deletion

class Node:
    #constructor
    def __init__(self,data):
        self.left = None
        self.right = None # pointers to the left and right
        self.data = data # value of the node stored

        #insert
    def insert(self,data):
        if self.data:#checks if this node has a value
            if data < self.data:
                if self.left is None:#if the new value is smaller, we try to insert it on the left
                    # if theres no left child, create one, if a left child exists we call insert on it recursively
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data: #if the new value is greater, go to the right
                # if theres no right child, create one. If one exists, insert it recursively there
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
            else:# if the node has no data yet(this is very rare if youre using the constructor properly),assign it
                self.data=data

    # search() method looks through the BST to find a specific value(call key)
    def search(self,key):
        # is the key smaller than the current node?
        if key < self.data:
            if self.left is None:#
                return str(key)+"Not found"
            return self.left.search(key)

        # is the key greater than the current node?
        elif key > self.data:
            if self.right is None:
                return str(key)+"Not found"
            return self.right.search(key)

        # if the key is equal to the current node
        else:
            print(str(self.data)+'is found')

    #inorder traversal: left subtree->current node->right subtree(ascending order)
    #useful when you need to retrieve elements in order
    #uses recursion to handle left and right subtrees automatically
    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.data,"->",end="")
        if self.right:
            self.right.Inorder()

    #root->left subtree -> right subtree, parent first
    def Preorder(self):
        print(self.data,"->",end="") #step1:visit the current node
        if self.left:
            self.left.Preorder() #Step2:traverse the left subtree
        if self.right:
            self.right.Preorder() # Step3:traverse the right subtree

    #left subtree ->right subtree ->root
    def Postorder(self):
        if self.left:
            self.left.Postorder()#step1:traverse the left subtree
        if self.right:
            self.right.Postorder()#step2:traverse the right subtree
        print(self.data,"->",end="")#step3:visit the current node

#create the root of the BST
root=Node(50)

#insert some nodes
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)

#inorder traversal (should print in ascending order)
print("inorder traversal:")
root.Inorder()
print("\n")

#preorder traversal(root first)
print("Preorder traversal:")
root.Preorder()
print("\n")

#postorder traversal (root last)
print("Postorder traversal:")
root.Postorder()
print("\n")

#search for existing and non-existing values
print("Search tests:")
root.search(60)
root.search(25)
