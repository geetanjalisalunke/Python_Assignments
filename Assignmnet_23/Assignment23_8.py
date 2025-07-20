import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    data={"name":["Amit","Geetanjali","Pooja"],
          "English":[85,90,78],
          "Science":[92,88,80],
          "Math":[75,85,82]
       }
    df=pd.DataFrame(data)
    amit_scores = df[df['name'] == 'Amit'][['English', 'Science', 'Math']].iloc[0]
    print(amit_scores)
    df.plot(title='Line Chart', xlabel=[['name'][0]], ylabel=['English','Science','Math'], figsize=(10, 6), color=['blue','red','green'], linewidth=2)
    plt.grid()
    plt.show()
if __name__=="__main__":
    main()