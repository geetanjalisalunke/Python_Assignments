def ChkDigit(ch):
    
    if  ch>='0' and ch<='9':
        return True
    else:
        return False
        
def main():
    
    print("Enter Character")
    a=input()
    
    ret=ChkDigit(a)
    print(ret)
    
if __name__=="__main__":
    main()