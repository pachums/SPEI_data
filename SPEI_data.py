'''
PROYECTO DE ALBERTO
20/10/20

Tratamiento de dataframe para unificar los datos SPEI_12
'''

import pandas as pd
import numpy as np
import os

#Lectura de los 346 archivos
for base, dirs, files in os.walk("E:/Trabajos I+D/Alberto_CLIMVAC/Datos_sequia"):
    print("Read files")
    
df=pd.read_excel("E:/Trabajos I+D/Alberto_CLIMVAC/Canarias/0can.xlsx")
list_category=df.columns[3:13]

for j in range(0,len(list_category)):
    category=list_category[j]
    print(category)

    for i in np.linspace(0,31,32):
        i=int(i)  
        
        df=pd.read_excel(f"E:/Trabajos I+D/Alberto_CLIMVAC/Canarias/{i}can.xlsx")
        
        if i==0:
            new = pd.DataFrame(columns=['[61-89]', '[91-19]'], index=range(1))
            new.insert(2,'CoordX',df.loc[0,'cordx'])
            new.insert(3,'CoordY',df.loc[0,'cordy'])
            
            var=df[[category]]
            var=var.to_numpy()
            new.at[0,'[61-89]']=int(sum(var[0:29]))
            new.at[0,'[91-19]']=int(sum(var[30:59]))
    
        
        var=df[[category]]
        var=var.to_numpy()
        new.at[i,'[61-89]']=int(sum(var[0:29]))
        new.at[i,'[91-19]']=int(sum(var[30:59]))
    
        new.at[i,'CoordX']=df.loc[0,'cordx']
        new.at[i,'CoordY']=df.loc[0,'cordy']
 
    # Save new DataFrame
    #new=new.T
    new.to_excel(f'E:/Trabajos I+D/Alberto_CLIMVAC/Output_canarias_v2/{category}.xlsx')
    print(f'{category}.xlsx done successfully')





