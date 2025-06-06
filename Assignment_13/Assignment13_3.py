class Arithmetic:
    
    def __init__(self,A):
        self.value=A
        
    def ChkPrime(self):
        
        cnt=0
        for i in range(1,(self.value)+1):
            if self.value%i==0:
                cnt=cnt+1
        if cnt==2:
            return True
        else:
            return False
        
    def ChkPerfect(self):
        sum=0
        for i in range(1,self.value):
            if self.value%i==0:
                sum=sum+i
        if sum==self.value:
            return True
        else:
            return False
        
    def Factors(self):
        a=[]
        for i in range(1,self.value):
            if self.value%i==0:
                a.append(i) 
        return a
    
    def SumFactors(self):
        sum=0
        lst=self.Factors()
        for i in lst:
            sum=sum+i
        return sum+self.value
    
def main():
    
    obj1=Arithmetic(28)
    obj2=Arithmetic(13)
    
    ret=obj1.ChkPerfect()
    print(ret)
    ret=obj1.ChkPrime()
    print(ret)
    ret=obj1.Factors()
    print(ret)
    ret=obj1.SumFactors()
    print(ret)
    
    ret=obj2.ChkPrime()
    print(ret)
    
if __name__=="__main__":    
    main()