class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
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
obj=queue()
while True:
    print("select any choice")
    print("1] enqueue")
    print("2] dequeue")
    print("3] display")
    print("4] quit")
    choice=int(input())
    if choice==1:
        ele=int(input("enter the element to insert"))
        obj.enqueue(ele)
        print("successfully inserted element")
    elif choice==2:
        s=obj.dequeue()
        print("popped element:",s)
    elif choice==3:
        obj.display()
    elif choice==4:
        break
    else:
        print("Enter the correct choice")
        
        
            
        
