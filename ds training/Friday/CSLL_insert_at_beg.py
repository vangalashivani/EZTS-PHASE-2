class Node:
    def __init__(self,data):
         self.data=data
         self.next=None
    
class singlelinkedlist:
    def __init__(self):
     self.head=None
    def del_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
def del_At_last(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
def del_At_pos(self,pos):
    temp=self.head.next
    prev=self.head
    #2 iterations
    for i in range(1,pos-1):
        temp=temp.next
        prev=prev.next
        prev.next=temp.next
        temp.next=None





    
