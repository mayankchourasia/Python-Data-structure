class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key


def insert(root,node):
        if root is None:
            root=Node
        else:
            if root.val<node.val:
                if root.right is None:
                    root=node
                else:
                    insert(root.right,node)
            elif root.val > node.val:
                if root.left is None:
                    root=node
                else:
                    insert(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)       

root=raw_input("Enter Root Element:\t")
def main():
    
    r = Node(root)
    while True:
        print ("-"*50)
        print ("Word Dictionary using Binary Search Tree")
        print ("1.Insert Element")
        print ("2.Show Tree")
        print ("3.Delete Element")
        print ("4.Exit")
        print "-"*50
        ch=input("Enter Your Choice")
        if ch==1:
            val=raw_input("Enter Word to be inserted:\t")
        
            insert(r,Node(val))
        
        if ch==2:
            print ("Your Tree in INORDER :\n")
            inorder(r)

        if ch==3:
            d = raw_input("Enter The Word to delete")
            deletenode(r,Node(d) )  

        if ch==4:
            print ("Thank You")
            break     

if __name__=='__main__':
    main()