def Circum(no1):
    return 2*3.14*no1

def main():
    
    print("Enter Radius")
    radius=int(input())
    ret=Circum(radius)
    print(ret)
    
if __name__=="__main__":
    main()