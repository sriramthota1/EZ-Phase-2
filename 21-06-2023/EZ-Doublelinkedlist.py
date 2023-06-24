#double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head.prev=nb
        self.head=nb
    def insert_last(self,data):
        nl=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nl
        nl.prev=temp
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.prev=temp
        np.next=temp.next
        temp.next.prev=np
        temp.next=np
    def delete_first(self):
        temp=self.head
        self.head=temp.next
    def delete_last(self):
        temp=self.head.next
        prev=self.head
        if temp==None:
            print("Linked list is empty")
        else:
            while temp.next:
                temp=temp.next
                prev=prev.next
            prev.next=None
            temp.prev=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
         
        
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<--> ",end="")
                temp=temp.next

obj=DLL()
n1=Node(10)
obj.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
#obj.display()
obj.insert_begin(100)
obj.display()
print("")
obj.insert_last(120)
obj.display()
print("")
obj.insert_position(2,80)
obj.display()
print("")
obj.delete_first()
obj.display()
print("")
obj.delete_last()
obj.display()
print("")
obj.delete_position(2)
obj.display()
