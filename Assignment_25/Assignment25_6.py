import pandas as pd

def main():
    
    data={
       'Grade':['A+','B','A','C','B+']
    }
    df=pd.DataFrame(data)
    df['Grade'].replace({'A+':'Excellent','A':'Very Good','B+':'Good','B':'Average','C':'Poor'},inplace=True)
    print(df)
    
if __name__=="__main__":
    main()