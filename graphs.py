import pandas as pd
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


file = "master.xlsx"
data = pd.read_excel(file, header=0)
print(data)

sns.jointplot(data=data, x="W_Strikes", y="W_Strike_Percentage", hue="KO?")
plt.show()

master_ko  = data[data["KO?"]]
master_dec = data[~data["KO?"]]


fig, ax = plt.subplots()
sns.histplot(data=master_ko , x="W_Distance_Percentage", color='cyan'        , label='KO',  stat='percent')
sns.histplot(data=master_dec, x="W_Distance_Percentage", color='teal'        , label='DEC', stat='percent')
ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
sns.histplot(data=master_ko , x="W_Clinch_Percentage"  , color='midnightblue', label='KO', stat='percent')
sns.histplot(data=master_dec, x="W_Clinch_Percentage"  , color='mediumslateblue', label='DEC', stat='percent')
ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
sns.histplot(data=master_ko , x="W_Ground_Percentage"  , color='lightsalmon' , label='KO', stat='percent')
sns.histplot(data=master_dec, x="W_Ground_Percentage"  , color='r' , label='DEC', stat='percent')
ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
sns.histplot(data=master_ko , x="W_Head_Percentage"  , color='lightsalmon' , label='KO', stat='percent')
sns.histplot(data=master_dec, x="W_Head_Percentage"  , color='r' , label='DEC', stat='percent')
ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
sns.histplot(data=master_ko , x="W_Body_Percentage", color='cyan'        , label='KO',  stat='percent')
sns.histplot(data=master_dec, x="W_Body_Percentage", color='teal'        , label='DEC', stat='percent')
ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
sns.histplot(data=master_ko , x="W_Legs_Percentage"  , color='midnightblue', label='KO', stat='percent')
sns.histplot(data=master_dec, x="W_Legs_Percentage"  , color='mediumslateblue', label='DEC', stat='percent')
ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
plt.tight_layout()
plt.show()

#Solo se utilizan las luchas de 3 rounds debido a que no se encuentra el tiempo de pelea total se estima a que en primedio es en la mitad del round que termina
master_ko = master_ko.drop(master_ko[master_ko['Max_round'] == 5].index)
master_dec = master_dec.drop(master_dec[master_dec['Max_round'] == 5].index)
master_ko = master_ko.drop(master_ko[master_ko['PER'] >= 500].index)
master_dec = master_dec.drop(master_dec[master_dec['PER'] >= 500].index)
sns.histplot(data=master_ko , x="PER", stat='density', bins=10, label='KO' , color='seagreen')
sns.histplot(data=master_dec, x="PER", stat='density', bins=10, label='DEC', color='darkorchid')
plt.show()