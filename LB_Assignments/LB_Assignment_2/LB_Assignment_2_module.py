def PrintEven(no):
    
    if no<=0:
        return -1
    for i in range(2,(no*2)+1,2):
            print(i,end=" ")
        
def DisplayEvenFactor(no):
    if no<=0:
        return -1
    for i in range(2,no):
        if no%i==0 and i%2==0:
            print(i)

def DisplayComFactor(no1,no2):
    for i in range(2,no1):
        if no1%i==0 and no2%i==0 :
            print(i)
    
def DisplayComFactorLarge(no1,no2):
    max=0
    for i in range(2,no1):
        if no1%i==0 and no2%i==0 :
            max=i
    print(max)

def SwapChar(A,B):
    C=''
    
    C=A
    A=B
    B=C
    
    print("Swapped Character is :",A,B)

def swapnumber(a,b):
    
    a = a + b
    b = a - b  
    a = a - b  
    print(a,b)

def PrintStart(no):
    
    for i in range (no):
        print("*",end=" ")
        
def DisplayConvert(value1):
    if value1>='A' and value1<='Z':
        print(chr(ord(value1)+32))
    if value1>='a' and value1<='z':
        print(chr(ord(value1)-32))
        
def Fibonacci(no):
    
    f_num=0
    s_num=1
    sum=0
    
    print(f_num)
    print(s_num)
    
    for i in range(no-2):
        
        sum=f_num+s_num
        f_num=s_num
        s_num=sum
        print(sum)
        
def ChkVowel(ch):
    
    lst=['a','e','i','o','u','A','E','I','O','U']
    
    if ch in lst:
        print("Vowels")
    else:
        print("Not a Vowels")
        