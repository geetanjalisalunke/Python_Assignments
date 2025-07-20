import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    data={"name":["Amit","Geetanjali","Pooja"],
          "English":[85,90,78],
          "Science":[92,88,80],
          "Math":[75,85,82]
       }
    df=pd.DataFrame(data)
    df['Total']=df['English']+df['Science']+df['Math']
    df.plot.bar(x='name',y='Total')
    plt.title("Student Marks")
    plt.xlabel("Student name")
    plt.ylabel("Marks")
    plt.grid()
    plt.show()
if __name__=="__main__":
    main()