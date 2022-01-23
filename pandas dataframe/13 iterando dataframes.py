import pandas
import pandas as pd
import numpy as np

# Creemos nuestro df para trabajar...
data = { 'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
         'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
         'age': [41, 28, 33, 34, 38, 31, 37],
         'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
         }
row_labels = [101, 102, 103, 104, 105, 106, 107]
df = pd.DataFrame(data=data, index=row_labels)
df['django-score'] = [71, 95, 88, 79.0, 91, 91, 80]
df['js-score'] = [71, 95, 88, 79.0, 91, 91, 80]
wgts = pd.Series(data=[0.4, 0.3, 0.3], index=['py-score', 'django-score', 'js-score'])
df['total-score'] = np.sum(df[wgts.index] * wgts, axis=1)
'''
       name         city  age  py-score  django-score  js-score  total-score
101  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
102     Ann      Toronto   28      79.0          95.0      95.0         88.6
103    Jana       Prague   33      81.0          88.0      88.0         85.2
104      Yi     Shanghai   34      80.0          79.0      79.0         79.4
105   Robin   Manchester   38      68.0          91.0      91.0         81.8
106    Amal        Cairo   31      61.0          91.0      91.0         79.0
107    Nori        Osaka   37      84.0          80.0      80.0         81.6
'''


