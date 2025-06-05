def ChkCapital(ch):
    
    if  ch>='A' and ch<='Z':
        return True
    else:
        return False
        
def main():
    
    print("Enter Character")
    a=input()
    
    ret=ChkCapital(a)
    print(ret)
    
if __name__=="__main__":
    main()