import pandas as pd
import streamlit
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

import warnings
warnings.filterwarnings('ignore')
ipl = pd. read_csv('ipl_2022_dataset.csv')
ipl.drop('Unnamed: 0',axis=1,inplace = True)
 #print(ipl.head())
print(ipl.columns)
ipl['COST IN $ (CR.)'] = ipl['COST IN $ (CR.)'].fillna(0)
ipl['Cost IN $ (000)'] = ipl['Cost IN $ (000)'].fillna(0)
ipl['2021 Squad'] = ipl['2021 Squad'].fillna('Not participated')
teams = ipl[ipl['COST IN $ (CR.)']>0]['Team'].unique()
print(teams)
ipl['status'] = ipl['Team'].replace(teams,'sold')
print(ipl)
