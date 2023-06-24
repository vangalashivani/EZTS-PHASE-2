stack=[]
n=int(input("enter number of elements to push in stack:\n"))
def push():
    for i in range(n):
        v=int(input("enter element:"))
        stack.append(v)
def display():
    n=int(input("\nenter\n 1-even numbers\n2- odd numbers\n"))
    if n==1:
        even()
    elif n==2:
        odd()
    else:
        print("\ninvalid!\n")
def even():
    for i in range(len(stack)):
        if stack[i]%2==0:
            print("\neven stack elements:",stack[i],end=" ")
def odd():
    for i in range(len(stack)):
        if stack[i]%2!=0:
            print("\nodd stack elements",stack[i],end=" ")
    
def pop():
    if not stack:
        print("\nstack is empty\n")
    else:
        e=stack.pop()
        print("\nelement removed successfully\n")
while(1):
    ch=int(input("\n1-push\n2-pop\n3-display\n4-quit\nenter your choice:"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("\nplease enter valid option!\n")
