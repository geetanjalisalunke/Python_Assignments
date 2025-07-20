import pandas as pd
import numpy as np

def main():
    
    data={
       'Department':['HR','IT','Finance','HR','IT']
    }
    df=pd.DataFrame(data)
    df_decoded=pd.get_dummies(df,columns=['Department'],drop_first=True)
    print(df_decoded)
    
if __name__=="__main__":
    main()