import pandas as pd
import numpy as np

def main():
    
    data={
       'Name':['A','B','C'],
       'Age':[21.0,22.0,23.0]
    }
    df=pd.DataFrame(data)
    print("Before conversion:",df['Age'].dtype)
    df['Age']=df['Age'].astype(int)
    print("After conversion:",df['Age'].dtype)
    
if __name__=="__main__":
    main()