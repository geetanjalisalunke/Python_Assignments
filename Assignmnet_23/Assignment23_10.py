import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    data={"name":["Amit","Geetanjali","Pooja"],
          "English":[85,90,78],
          "Science":[np.nan,88,80],
          "Math":[75,np.nan,82]
       }
    df=pd.DataFrame(data)
    df.drop('English',inplace=True,axis=1)
    print(df)
    
if __name__=="__main__":
    main()