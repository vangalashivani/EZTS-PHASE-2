stack=[]
def push():
    element=int(input("enter the element"))
    stack.append(element)
    print(element)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
            e=stack.pop()
            print("removed element:",e)
            print(stack)
while True:
    print("select operation 1.push 2.pop 3.quit 4.peek 5.top")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        quit()
    elif choice==4:
        top()
    elif choice==5:
        break
    else:
        print("enter the correct operation")
                
