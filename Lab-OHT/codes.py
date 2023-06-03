s = []
top = None

def isEmpty(stk):
    if(stk==[]):
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk)-1

def s_pop(stk):
    if(isEmpty(stk)):
        return ('UnderFlow!')
    else:
        i = stk.pop()
        if (len(stk)==0):
            top = None
        else:
            top = len(stk) - 1
    return i

def peek(stk):
    if (isEmpty(stk)):
        return ('UnderFlow!')
    else:
        top = len(stk)-1
        return stk[top]

def display(stk):
    if (isEmpty(stk)):
        return ('UnderFlow!')
    else:
        top = len(stk)-1
        print(stk[top], "<---Top")
        for i in range(top-1, -1, -1):
            print (stk[i])


for i in range(6):
    x = int(input("Enter element: "))
    push(s,x)
print("\n")

display(s)

print("\n")


item=s_pop(s)
if (item=='UnderFlow!'):
    print('UnderFlow! Stack is Empty!')
else:
    print("%d is popped"%item)

print("\n")

for i in range(3):
    item = s_pop(s)
    if (item == 'UnderFlow!'):
        print('UnderFlow! Stack is Empty!')
    else:
        print("%d is popped" % item)
print("\n")

display(s)

print("\n")

item=peek(s)
if (item=='UnderFlow!'):
    print('UnderFlow! Stack is Empty!')
else:
    print("%d is at the top"%item)

print("\n")

item=isEmpty(s)
if (item=='True'):
    print('UnderFlow! Stack is Empty!')
else:
    print('Stack is not Empty:')
    display(s)

print("\n")