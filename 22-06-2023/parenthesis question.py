""""s=input()
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
c=0
r=0
for i in range(0,2):
    
    for i in range(0,len(s)):
        if s[i]=='(':
            count1+=count1
            c=i
        elif s[i]==')':
            count2+=count2
            r=i
    for i in range(c,r):
        if s[i]=='[':
            count3=count3+1
        elif s[i]==']':
            count4=count4+1
        elif s[i]=='{':
            count5=count5+1
        elif s[i]=='}':
            count6=count6+1
    if count1==count2 and count3==count4 and count5==count6:
        print("True")
    else:
        print("False")

"""
stack=[]
s=input()
n=len(s)
c=0
flag=1
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
            c+=1
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if stack==[]:
                flag=0
                break
            if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
                stack.pop()
                c-=1
            else:
                flag=0
                break
        else:
            flag=-1
            break
    if flag==0 or c!=0:
        print(False)
    elif flag==-1:
        print("Invalid Paranthesis")
    else:
        print(True)




#another code

while True:
    a = input()
    for i in a:
        if i.isalpha() or i.isdigit():
            k=10
            print('invalid response')
            continue
    if len(a)%2==1:
        print('no')
        continue
    b = []
    k = 1
    if a[0]==')' or a[0]=='}' or a[0]==']':
        print('no')
        continue
    for i in a:
        if i == '(' or i == '[' or i == '{':
            b.append(i)
        elif i == ')' or i == ']' or i == '}' and not len(b)==0:
            if i == ')' and b[-1] == '(' and not len(b)==0:
                b.pop()
            elif i == ']' and b[-1] == '[' and not len(b)==0:
                b.pop()
            elif i == '}' and b[-1] == '{' and not len(b)==0:
                b.pop()
            else:
                k = 10
    if len(b)!=0:
        print('no')
    elif k == 10 :
        print('no')
    else:
        print('yes')
