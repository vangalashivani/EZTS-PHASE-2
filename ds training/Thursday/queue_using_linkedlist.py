class node():
    def _init_(self,data):
        self.data=data
        self.next=None
class queue:
    def _init_(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            ret=self.head.data
            self.head=self.head.next
            return ret
    def display(self):
     if self.head is None:
            print("\nstack is empty\n")
     else:

            temp=self.head#temp assigned to first node
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print(" ")
                temp=temp.next
obj=queue()
while(1):
    ch=int(input("\nenter your choice:\n1-enqueue\n2-dequeue\n3-display\n4-quit"))
    if ch==1:
        n=int(input("\nenter element:\n"))
        obj.enqueue(n)
    elif ch==2:
        obj.dequeue()
    elif ch==3:
        obj.display()
    elif ch==4:
        break
    else:
        print("\nplease enter valid option!\n")
            
    
