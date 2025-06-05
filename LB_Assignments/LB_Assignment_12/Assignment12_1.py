def ChkAlpha(ch):
    
    if ch>='a' and ch<='z':
        return True
    elif ch>='A' and ch<='Z':
        return True
    else:
        return False
        
def main():
    
    print("Enter Character")
    a=input()
    
    ret=ChkAlpha(a)
    print(ret)
    
if __name__=="__main__":
    main()