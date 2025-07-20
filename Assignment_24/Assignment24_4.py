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
    df.insert(4, 'Gender', ['M', 'F', 'F'])
    df_geeta = df[df['name'] == 'Geetanjali'][['English', 'Science', 'Math']].iloc[0]

    df_geeta.plot.pie( figsize=(6, 6),
        title='Geetanjali - Subject-wise Marks:'
    )
    plt.show()

    
if __name__=="__main__":
    main()