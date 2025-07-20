import pandas as pd

def main():
    
    data={"name":["Amit","Geetanjali","Vivek"],
          "English":[85,90,78],
          "Science":[92,88,80],
          "Math":[75,85,82]
       }
    df=pd.DataFrame(data)
    df['Total']=df['English']+df['Science']+df['Math']
    print(df.head())
if __name__=="__main__":
    main()