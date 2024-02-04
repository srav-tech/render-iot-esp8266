import pandas as pd
import random
import time

data=[]
count=0

while True:
    h=random.randint(20,100)
    outcome=0
    if(h>=20 and h<40):
        outcome=1
    elif(h>=40 and h<60):
        outcome=2
    elif(h>=60 and h<80):
        outcome=3
    elif(h>=80 and h<100):
        outcome=4
    else:
        outcome=0
    cluster_data=[h,outcome]
    data.append(cluster_data)
    count+=1
    if(count==10):
        dataframe=pd.DataFrame(data)
        dataframe.to_csv('iot.csv')
        count=0
        time.sleep(1)

