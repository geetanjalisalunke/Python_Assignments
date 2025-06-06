class BookStore:
    NoOfBook=0
    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        BookStore.NoOfBook=BookStore.NoOfBook+1
    
    def Display(self):
        print(self.Name)
        print(self.Author)
        print(BookStore.NoOfBook)
    
def main():
    
    obj1=BookStore("Linux System Programming","Robert Love")
    obj1.Display()
    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.Display()
    
    
if __name__=="__main__":    
    main()