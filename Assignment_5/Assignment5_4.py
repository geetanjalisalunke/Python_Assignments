def Lagest_three(no1,no2,no3):
    max=no1
    if no2>no1 and no2>no3:
        max=no2
    elif no3>no1 and no3>no2:
        max=no3
    return max

def main():
    
    print("Enter the Three Numbers")
    no1=int(input()) 
    no2=int(input())
    no3=int(input())
    ans=Lagest_three(no1,no2,no3)
    print("Largest Number is :",ans)
    
if __name__=="__main__":
    main()
    