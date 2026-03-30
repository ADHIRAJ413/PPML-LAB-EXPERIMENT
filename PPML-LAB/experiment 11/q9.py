import pandas as pd
data={
    'math': [90,85,80,95],
    'science': [85,80,90,95],
    'english': [80,90,85,95]
}
df=pd.DataFrame(data)
print("DataFrame:\n",df)
correlation=df.corr()
print("\nCorrelation matrix:\n",correlation)