import LB_Assignment_2_module as module
            
def main():
    
    print("Enter First number")
    no1=int(input())
    print("Enter Second number")
    no2=int(input())
    
    print("Even Numbers")
    module.PrintEven(no1)
    print()
    
    print("Display Even Factors")
    module.DisplayEvenFactor(no1)
    
    print("Display common factors")
    module.DisplayComFactor(no1,no2)
    
    print("Display large common factor")
    module.DisplayComFactorLarge(no1,no2)
    
    print("Swapped Number is")
    module.swapnumber(no1,no2)
    
    print("Start")
    module.PrintStart(no1)
    print()
    
    print("Fibonacci Series")
    module.Fibonacci(no1)
    
    print("Enter First Character")
    value1=input()
    print("Enter Second Character")
    value2=input()
    module.SwapChar(value1,value2)
    
    print("Converted Character")
    module.DisplayConvert(value1)
    
    print("Check Vowels")
    module.ChkVowel(value1)

if __name__=="__main__":
    main()