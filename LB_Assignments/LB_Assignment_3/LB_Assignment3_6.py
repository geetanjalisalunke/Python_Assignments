def Binary(no):
    
    res=[]
    b=[]
    while (no>0):
        
        ans=no%2
        no=int(no/2)
        res.append(ans)
    
    for i in range (len(res)-1,-1,-1):
        b.append(res[i])
    
    print("".join(map(str,b)))

def main():
    
    print("Enter Number")
    radius=int(input())
    Binary(radius)
    
if __name__=="__main__":
    main()