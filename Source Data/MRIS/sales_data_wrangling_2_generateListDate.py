import pandas as pd
import numpy as np
import csv
from datetime import datetime, timedelta

Compiled_Data= pd.read_csv('sales.csv')
Compiled_Data_Df= pd.DataFrame(Compiled_Data)
Compiled_Data['CloseDate'] = pd.to_datetime(Compiled_Data['CloseDate'])
Compiled_Data_Df['DOMP_time']= pd.to_timedelta(Compiled_Data_Df['DOMP'],'d')
Compiled_Data_Df['ListDate'] = Compiled_Data['CloseDate'] - Compiled_Data_Df['DOMP_time']
Compiled_Data_Df['IndexMonth2'] = Compiled_Data_Df['ListDate'].map(lambda t: t.replace(day=1))

#print(Compiled_Data_Df[1:5] )
Compiled_Data_Df.to_csv('CompiledDataWithListDate.csv')