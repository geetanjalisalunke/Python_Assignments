import pandas as pd
import numpy as np

def main():
    
    data={"name":["Amit","Geetanjali","Pooja"],
          "English":[85,90,78],
          "Science":[np.nan,88,80],
          "Math":[75,np.nan,82]
       }
    df=pd.DataFrame(data)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.insert(4, 'Gender', ['M', 'F', 'F'])
    grp_df=df.groupby('Gender')[['English','Science','Math']].mean()
    print(grp_df)
    
if __name__=="__main__":
    main()