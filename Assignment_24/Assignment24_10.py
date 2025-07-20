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

    df.boxplot(column='English')
    plt.title("English Marks")
    plt.xlabel("English Marks")
    plt.show()

    
if __name__=="__main__":
    main()