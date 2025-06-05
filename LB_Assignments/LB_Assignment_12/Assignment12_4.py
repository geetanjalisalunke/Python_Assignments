def ChkSmall(ch):
    
    if  ch>='a' and ch<='z':
        return True
    else:
        return False
        
def main():
    
    print("Enter Character")
    a=input()
    
    ret=ChkSmall(a)
    print(ret)
    
if __name__=="__main__":
    main()