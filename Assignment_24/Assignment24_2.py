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
    print("After adding new col",df)
    encode_df=pd.get_dummies(df, columns=['Gender'],drop_first=True)
    print(encode_df)
    
if __name__=="__main__":
    main()