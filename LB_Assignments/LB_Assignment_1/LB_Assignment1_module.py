def Divide(no1,no2):
    if no2==0:
        return -1
    return no1/no2

def display():
    for i in range (5):
        print("Marvellous",end=" ")
        
def displayx():
    for i in range (5,0,-1):
        print(i,end=" ")
        
def Chk(no):
    if no%5==0:
        return True
    else:
        return False

def displays(no):
    for i in range(no):
        print("*",end=" ")
        
def displaysx(no):
    i=1
    while (i<=no):
        print("*",end=' ')
        i=i+1
        
def displaychar(ch):
    print(ch)
    
def Substract(no):
    return no-5

def displayHello(no):
    if no<10:
        print("Hello")
    else:
        print("Demo")