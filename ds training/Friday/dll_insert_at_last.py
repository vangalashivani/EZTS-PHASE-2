class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def _init_(self):
        self.head=None
    def ins_at_end(self):
        nn=node(50)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=nn4
        nn.prev=temp
    def display(self):
        if self.head is None:
            print("linked list is empty!")
        else:
            temp=self.head
            print("forward traversal\n")
            while temp.next!=None:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("<->",end=" ")
                temp=temp.next
            print(temp.data,end=" ")
            print("\nbackward traversal\n")
            while temp:
                print(temp.data,end=" ")
                if temp.prev!=None:
                    print("<->",end=" ")
                temp=temp.prev
obj=dll()
n1=node(100)
obj.head=n1
n2=node(200)
n2.prev=n1
n1.next=n2
n3=node(300)
n3.prev=n2
n2.next=n3
n4=node(400)
n4.prev=n3
n3.next=n4
obj.display()
print()
obj.ins_at_end()
obj.display()
