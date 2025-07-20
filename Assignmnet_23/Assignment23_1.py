import pandas as pd

def main():
    
    data={"name":["Amit","Geetanjali","Vivek"],
          "English":[85,90,78],
          "Science":[92,88,80],
          "Math":[75,85,82]
       }
    df=pd.DataFrame(data)
    print("Shape of DataFrame:",df.shape)
    print("Column information of DataFrame :",df.columns.tolist())
    print("Datatype of Dataframe :",df.dtypes)
    print("Information abount DataFrame: ",df.describe())

if __name__=="__main__":
    main()