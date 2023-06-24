class node:
    def __init__(self,key):
      self.left=None
      self.right=None
      self.val=key
def printinorder(root):
        if root:
            printinorder(root.left)
            print(root.val,end=" ")
            printinorder(root.right)
def printpostorder(root):
        if root:
            printpostorder(root.left)
            printpostorder(root.right)
            print(root.val,end=" ")
def printpreorder(root):
        if root:
            print(root.val,end=" ")
            printpreorder(root.left)
            printpreorder(root.right)
root=node(100)
root.left=node(400)
root.right=node(500)
root.left.left=node(700)
root.left.right=node(600)
root.left.right.left=node(900)
print("pre-order")
printpreorder(root)
print("in-order")
printinorder(root)
print("post-order")
printpostorder(root)


            
            



            
            


            
            
