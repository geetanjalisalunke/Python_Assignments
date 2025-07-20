import pandas as pd
import numpy as np

def main():
    
    data={
       'Marks':[18,np.nan,25,np.nan,35]
    }
    df=pd.DataFrame(data)
    df_interpolated = df.interpolate(method='spline',order=2)
    print(df_interpolated)
    
if __name__=="__main__":
    main()