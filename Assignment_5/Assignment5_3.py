def Chk_vote_eligibility(no):
    if no<=0:
        print("Enter the correct Age")
    elif no>=18 :
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote")

def main():
    
    print("Enter the Age")
    no=int(input())
    Chk_vote_eligibility(no)
    
if __name__=="__main__":
    main()
    