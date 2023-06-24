 #Get one dynamic array for the given size and do all the operation of DS:- insert,delete,search,sort
def func():
  
    while(1):
        print("1]insert")
        print("2]delete")
        print("3]search")
        print("4]sort")
        print("5]display")
        print("6]Exit")
        print("select the option to perform")
        op=int(input())
        if op==1:
            insert()
        elif op==2:
            delete()
        elif op==3:
            search()
        elif op==4:
            sorting()
        elif op==5:
            display()
        elif op==6:
            print(" ------program terminated----") 
            break
        else:
            print("select the correct option")

def insert():
    
    print("enter the element to insert")
    ins=int(input())
    l1.append(ins)
    print(l1)
    
def delete():

    print("enter the number to delete")
    dele=int(input())
    if dele in l1:
        l1.remove(dele)
        print("element deleted successfully")
    else:
        print("element not found")
   
def search():
    
    print("enter search element")
    se=int(input())
    flag=0
    for i in l1:
        if i==se:
            flag=1
    if flag==1:
        print("element found")
    else:
        print("element not found")
        
def sorting():
    l1.sort()
    print(l1)
    
def display():
    print(l1)
        

print("enter the size of the array")
n=int(input())
l1=[]
print("enter the elements")
for i in range(0,n):
    l1.append(int(input()))
print(l1)
func()








        
    
