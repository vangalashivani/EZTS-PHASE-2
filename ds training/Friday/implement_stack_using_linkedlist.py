class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=None(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
         if self.head is None:
             return None
         else:
            popped=self.head.data
            sekf.head=self.head.next
            return popped
obj_stack=stack()
while True:
    print("push <value>")
    print("pop")
    print("quit")
    do=input("what would you like to do?") .split()
    print("do",do)
    print("do[0]",do[0])
    operation=do[0].strip().lower()
    if operation=="push":
        obj_stack.push(int(do[1]))
    elif operation=="pop":
        popped=obj_stack.pop()
        if popped is None:
            print("stack is empty")
        else:
            print("popped value:",int(popped))
    elif operation =="quit":
            break
            
