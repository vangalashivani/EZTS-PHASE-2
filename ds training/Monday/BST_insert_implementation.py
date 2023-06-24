class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val = key
def insert(root,key):
        if root is None : 
            return  Node(key)
        else:
            if root.val==key:
                return root
            elif root.val<key:
                root.right=insert(root.right,key)
            else:
                 root.left=insert(root.left,key)
        return root
#inorder tranversal
def InOrder(root):
     if root:
          InOrder(root.left)
          print(root.val)
          InOrder(root.right)
n=Node(50)
n=insert(n,30)
n=insert(n,20)
n=insert(n,40)
n=insert(n,70)
n=insert(n,60)
n=insert(n,80)
InOrder(n)



























