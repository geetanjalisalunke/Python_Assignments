import LB_Assignment1_module as module


def main():
    
    print("Enter the First Number")
    no1=int(input())
    print("Enter the Second Number")
    no2=int(input())
    
    ret=module.Divide(no1,no2)
    print(ret)
    
    module.display()
    
    module.displayx()
    
    ret=module.Chk(no1)
    print(ret)
    
    module.displays(no1)
    
    module.displaysx(no1)
    
    module.displaychar(no1)
    
    ret=module.Substract(no1)
    print(ret)
    
    module.displayHello(no1)

if __name__=="__main__":
    main()