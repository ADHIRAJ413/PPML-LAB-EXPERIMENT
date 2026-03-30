import pandas as pd
data=[10,20,30]
labels=['a','b','c']
series=(pd.Series(data, index=labels))
print("pandas Series:\n",series)
print("Element at index 'b':",series['b'])
