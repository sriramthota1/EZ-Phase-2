 #create two linked list and display whether they are same or not
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            
            np=Node(data)
            self.last_node.next=np
            self.last_node=np

    def display(self):
        """current=self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next"""
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temo=first node
            while temp.next  :
                print(temp.data,end="-> ")
                #temp.data means first node's data
                temp=temp.next#establishing link
            print(temp.data)
    
            
def equal(llist1, llist2):
        current1 = llist1.head
        current2 = llist2.head
        while (current1 and current2):
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        if current1 is None and current2 is None:
            return True
        else:
            return False

obj=LinkedList()
a_llist=LinkedList()
b_llist=LinkedList()
n1=int(input("How many elements would you like to insert in first list"))

for i in range(n1):
    data=int(input("enter data"))
    a_llist.append(data)
n=int(input("How many elements would you like to insert in second list"))
for i in range(n):
    data=int(input("enter data"))
    b_llist.append(data)
print("The Linked List:",end=" ")
a_llist.display()
b_llist.display()



if equal(a_llist,b_llist):
    print('Linked lists are same.')
else:
    print(' two linked list are not same.')

