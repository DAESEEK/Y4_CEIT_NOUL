from types import AsyncGeneratorType
import numpy as np
import pandas as pd
s = pd.Series([0,0.25,0.5,0.75,1.0])
print(s)

data =[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(data)
print(a)
print(a.dtype)

a=a.astype(np.float64)
print(a)
print(a[0][2])

print(a[2])
print(a.dtype)
