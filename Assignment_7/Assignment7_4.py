import functools as f

def product(no1,no2):
    return no1*no2

def main():
    a=[]
    print("Enter the number")
    no=int(input())
    
    for i in range(no):
        a.append(int(input()))
    
    ans=f.reduce(product,a)
    print("Product of give numbers is :",ans)
    
if __name__=="__main__":
    main()
    