#create a stack using user input and print even and odd numbers from the stack
stack=[]
eve=[]
odd=[]

def push():
    print("enter the size of stack")
    size=int(input())
    for i in range(size):
        element=int(input("enter the element"))
        stack.append(element)
    for i in stack:
        if i%2==0:
            eve.append(i)
        else:
            odd.append(i)
    print(stack)
def pop_element():
    print("1 or 2")
    pop=int(input())
    if pop==1:
        if not eve:
            print("stack is empty")
        else:
            s=eve.pop()
            print("Removed element:",s)
            print(eve)
    elif pop==2:
        if not eve:
            print("stack is empty")
        else:
            r=odd.pop()
            print("Removed element:",r)
            print(odd)
        
        
def display():
    print("1 or 2")
    c=int(input())
    if c==1:
        print(eve)
    elif c==2:
        print(odd)

while True:
    print("select operation 1.push 2.pop 3.display 4.Top 5.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()

    elif choice==4:
        if not stack:
            print("Stack is empty")
        else:
            print(stack[-1])
    elif choice==5:
        break
    else:
        print("Enter the correct number")
