def SImpleIntrest(p,n,r):
    return p*n*r
    
def main():
    
    print("Enter principle,rate,interest")
    no1=int(input())
    no2=int(input())
    no3=int(input())
    
    ret=SImpleIntrest(no1,no2,no3)
    print(ret)
    
if __name__=="__main__":
    main()