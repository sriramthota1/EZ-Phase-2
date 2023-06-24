# LInked list
#creating node-declaration & defination
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_last(self,data):
        nl=Node(data)
        curr=self.head
        if curr==None:
            print("Linked list is empty")
        else:
            while curr.next:
                curr=curr.next
            curr.next=nl
    def insert_at_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temo=first node
            while temp.next  :
                print(temp.data,end="-> ")
                #temp.data means first node's data
                temp=temp.next#establishing link
            print(temp.data)
    def delete_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
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
    def delete_pos(self,pos):

        

        
        
               
                    

obj=singlelinkedlist()
#node creation-initialising
n=Node(10)# so n.data in Node class will be 10
obj.head=n# assigning first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
n6=Node(70)
n5.next=n6


print("Before inserting 100 at begining")
obj.display()
print("After Inserting 100 at begining")
obj.insert_begining(100)
obj.display()
print("")
print("Before inserting 110 at last")
obj.display()
print("After Inserting 110 at last")
obj.insert_last(110)
obj.display()
print("")
print("Before inserting 120 at given position")
obj.display()
print("After Inserting 120 at given position")
obj.insert_at_position(8,120)
obj.display()
print("")
print("After deleting fist node")
obj.delete_first()
obj.display()
print("")
print("After deleting last node")
obj.delete_last()
obj.display()
print("")
print("before deleting at given position ")
obj.display()
print("")
print("After deleting at given positio ")
obj.delete_pos(2)
obj.display()
print("")













"""
#get one matrix as input,display diagonal elements,non diagonal,upper diagonal,lower diagonal elements.

n=int(input("enter the size of the matrix"))
matrix=[]
for i in range(0,n):
    r=[]
    for j in range(0,n):
        r.append(int(input()))
    matrix.append(r)
    
#printing the matrix
for i in range(0,n):
    for j in range(0,n):
        print(matrix[i][j],end=" ")
    print("")
#
DE=[]
NDE=[]
UDE=[]
LDE=[]
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            DE.append(matrix[i][j])
        if i!=j:
            NDE.append(matrix[i][j])
        if i<j:
            UDE.append(matrix[i][j])
        if i>j:
            LDE.append(matrix[i][j])
print("Diagonal elements:",DE)
print("Non-Diagonal elements:",NDE)
print("Upper-Diagonal elements:",UDE)
print("Lower-Diagonal elements:",LDE)

 
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")

for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")


"""









