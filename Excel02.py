import numpy
import pandas as pd
df = pd.read_excel('iATERlist-1.xlsx', engine = 'openpyxl')
a= df.head(8)
print(a)


