def PrintDigCount(lst):
    
    for num in lst:
        print(len(str(num)))
        
    
def main():
    a=[]
    print("Enter 8 Numbers")
    for i in range(8):
        a.append(int(input()))
    PrintDigCount(a)
    
if __name__=="__main__":
    main()