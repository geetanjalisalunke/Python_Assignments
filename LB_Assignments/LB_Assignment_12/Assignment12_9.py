def ChkSpecial(ch1):
    if ch1.isalnum():
        return False
    else:
        return True 
        
def main():
    
    print("Enter Character")
    a=input()
    
    ret=ChkSpecial(a)
    print(ret)
    
if __name__=="__main__":
    main()