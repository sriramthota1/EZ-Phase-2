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
           self.last_node.next=Node(data)
           self.last_node=self.last_node.next

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


a_llist=LinkedList()
n=int(input("How many elements would you like to insert"))
for i in range(n):
    data=int(input("enter data"))
    a_llist.append(data)
print("The Linked List:",end=" ")
a_llist.display()
