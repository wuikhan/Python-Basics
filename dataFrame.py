#activate virtual environment
#source activate virtualEnvironment
#install numpy - conda install numpy
#install pandas - conda install pandas
#run the program
#python programname.py

import numpy as np
import pandas as pd

data = {'Company':
                        ['GOOG','GOOG','MSFT','MSFT','FB','FB'],
            'Person':
                        ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
            'Sales':
                        [200,120,340,124,243,350]
       }

df = pd.DataFrame(data)
print (df)

byCompanyName = df.groupby('Company')
print (byCompanyName.mean())