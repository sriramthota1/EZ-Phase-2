class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            np=Node(data)
            np.next=self.head
            self.head=np
    def pop(self):
        if self.head is None:
            print("Stack is empty")
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp=self.head
            while temp.next:
                print(temp.data,end="->")
                temp=temp.next
            print(temp.data)
obj=stack()
while True:
    print("select any choice")
    print("1] push")
    print("2] pop")
    print("3] display")
    print("4] quit")
    choice=int(input())
    if choice==1:
        ele=int(input("enter the element to push"))
        obj.push(ele)
        print("successfully inserted element")
    elif choice==2:
        s=obj.pop()
        print("popped element:",s)
    elif choice==3:
        obj.display()
    elif choice==4:
        break
    else:
        print("Enter the correct choice")
        
        
            
        
