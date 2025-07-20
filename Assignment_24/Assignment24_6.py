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
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df['Total']=df['English']+df['Science']+df['Math']
    df['Status'] = np.where(df['Total'] > 250, 'Pass', 'Fail')
    pass_count = (df['Status'] == 'Pass').sum()
    print("Total Students passed :",pass_count)

    
if __name__=="__main__":
    main()