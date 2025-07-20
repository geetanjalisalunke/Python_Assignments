import pandas as pd

def main():
    
    data={"name":["Amit","Geetanjali","Pooja"],
          "English":[85,90,78],
          "Science":[92,88,80],
          "Math":[75,85,82]
       }
    df=pd.DataFrame(data)
    df['name'].replace('Pooja','puja',inplace=True)
    print(df)
         
if __name__=="__main__":
    main()