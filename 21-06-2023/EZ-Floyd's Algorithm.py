class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #insert a new node at the begining
    def push(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def detectAndRemoveLoop(self):
        if self.head is None: #LL Empty
            return
        if self.head.next is None:#LL has one node
            return
        slow_p=self.head
        fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            #if slow_p and fast_p meet at some point
            #there iss a loop
            if slow_p==fast_p:
                print("Meeting Point",slow_p.data)
                slow_p==self.head
                #finding the begining of the loop
                while(slow_p.next!=fast_p.next):
                    slow_p=slow_p.next
                    fast_p=fast_p.next


                    #since fast.next is the looping point
                print("start of loop",fast_p.next.data)
                fast_p.next=None #remove loop
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next


llist=LinkedList()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)

#creating a loop for testing
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next

#llist.printlist()
llist.detectAndRemoveLoop()
print("Linked List After removing loop")
llist.printlist()


                
