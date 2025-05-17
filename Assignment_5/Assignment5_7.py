def Area_of_reactangle(length,width):
   return length*width

def Perimeter_of_reactangle(length,width):
    return 2*(length+width)

def main():
    
    print("Enter Length")
    length=int(input())
    print("Enter Width")
    width=int(input())
    Area=Area_of_reactangle(length,width)
    print("Area :",Area)
    Ans=Perimeter_of_reactangle(length,width)
    print("Perimeter :",Ans)
    
if __name__=="__main__":
    main()
    