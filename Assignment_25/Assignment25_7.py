import pandas as pd

def main():
    
    data={
       'Age':[18,12,25,30,35]
    }
    df=pd.DataFrame(data)
    #X_normalized = (X - X_min) / (X_max - X_min)
    df['X_normalized']=(df['Age']-df['Age'].min())/(df['Age'].max()-df['Age'].min())
    print(df)
    
if __name__=="__main__":
    main()