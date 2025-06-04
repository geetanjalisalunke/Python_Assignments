def DisplayFloat(lst):

    for num in lst:
        if num>8.9:
            print(num)
    
    
def main():
    a=[]
    print("Enter 5 Numbers")
    for i in range(5):
        a.append(float(input()))
    
    DisplayFloat(a)
    


if __name__=="__main__":
    main()