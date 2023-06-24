class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inOrder(root):
    #set current to root of binary tree
    current=root
    stack=[]#initilalize stack
    done=0
    while True:
        #reach the left most Node of the current
        if current is not None:
        #place pointer to a tree node on the stack
        #before traversing the node's left subtree
            stack.append(current)
            current=current.left
#backtrack from empty subtree &visit Node
#at the top of the stack;
#however,if the stack is empty you are done
        elif(stack):
            current=stack.pop()
            print(current.data, end=" ")
#we have visitefd the node and its left
#subtree,Now,it's right subtree's turn
            current=current.right
        else:
            break
    print()

#input



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

inOrder(root)
