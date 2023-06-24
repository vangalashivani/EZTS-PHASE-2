class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class sll:
    def _init_(self):
        self.head=None
    def del_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        print("deleted successfully")
    def del_at_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        print("deleted successfully")
    def del_at_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        print("deleted successfully")
    def dispaly(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#temp assigned to first node
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
obj=sll()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
obj.dispaly()
print("\nenter 1-delete at beg\n2-delete at end\n3-delete at pos\n4-display")
while(1):
    n=int(input("\nenter choice:"))
    if n==1:
        obj.del_at_beg()
    elif n==2:
        obj.del_at_end()
    elif n==3:
        p=int(input("enter position to delete:"))
        obj.del_at_pos(p)
    elif n==4:
        obj.dispaly()
    else:
        print("invalid")
