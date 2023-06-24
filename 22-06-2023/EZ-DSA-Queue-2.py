queue=[]
def enqueue():
    element=input("enter element")
    queue.append(element)
    print(element,"is added in queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("dequeued element:",e)
def display():
    print(queue)
while True:
    print("select operation")
    print("1.Add 2.Remove 3.show 4.exit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("select correct option")
