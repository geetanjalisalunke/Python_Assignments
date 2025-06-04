def Pattern(no):
    for i in range(no,0,-1):
        print(f"{i}" ," # "*i,end=" ")
    
def main():
    
    print("Enter Number")
    value1=int(input())
    
    Pattern(value1)
    


if __name__=="__main__":
    main()