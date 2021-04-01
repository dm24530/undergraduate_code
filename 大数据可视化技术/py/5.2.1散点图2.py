import ggplot as gp
import pandas as pd
import numpy as np
crime = pd.read_csv("..//csv//crimeRatesByState2005.csv")
crime2 = crime[crime.state != 'United States']
crime2 = crime2[crime.state != 'District of Columbia']
# print(gp.ggplot(gp.aes(x='murder',y='burglary'),data=crime)+gp.geom_point(color='blue'))
print(gp.ggplot(gp.aes(x='murder',y='burglary'),data=crime2)+gp.geom_point()+gp.stat_smooth(method='loess',color='red'))