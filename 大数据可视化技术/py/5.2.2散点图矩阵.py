import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
crime = pd.read_csv('..//csv//crimeRatesByState2005.csv')
crime = crime[crime.state != 'United States']
crime = crime[crime.state != 'District of Columbia']
crime = crime.drop(['state'],axis=1)
crime = crime.drop(['population'],axis=1)
g = sns.pairplot(crime,diag_kind='kde',kind='reg')
plt.show()