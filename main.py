#Paquetes
import pandas as pd
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

#Carga de Datos
file = "dataufc.csv"
data = pd.read_csv(file, header=0)
pd.set_option('display.max_rows', None)

#Categorias importantes para el analisis
importantes = ["B_Name", "R_Name"]
fighter = ["B", "R"]

for f in fighter:
    for i in range(1, 6):
        head     = f + "__Round" + str(i) + "_Strikes_Head Significant Strikes_Landed"
        body     = f + "__Round" + str(i) + "_Strikes_Body Significant Strikes_Landed"
        legs     = f + "__Round" + str(i) + "_Strikes_Legs Significant Strikes_Landed"
        ground   = f + "__Round" + str(i) + "_Strikes_Ground Significant Strikes_Landed"
        clinch   = f + "__Round" + str(i) + "_Strikes_Clinch Significant Strikes_Landed"
        distance = f + "__Round" + str(i) + "_Strikes_Distance Strikes_Landed"
        total_l  = f + "__Round" + str(i) + "_Strikes_Significant Strikes_Landed"
        total_a  = f + "__Round" + str(i) + "_Strikes_Significant Strikes_Attempts"
        importantes.append(head)
        importantes.append(body)
        importantes.append(legs)
        importantes.append(ground)
        importantes.append(clinch)
        importantes.append(distance)
        importantes.append(total_l)
        importantes.append(total_a)
importantes.append("winby")
importantes.append("winner")
importantes.append("Last_round")
importantes.append("Max_round")


areas = ["Head", "Body", "Legs", "Ground", "Clinch", "Distance", "Total_L", "Total_A"]
categories = ["Winner", "Multiplier", "Method"]
for f in fighter:
    for area in areas:
        categories.append(f + "_" + area)


#Limpieza por datos que me interesan y eliminacion de nulos
final_data = data[(data['winby'] == 'KO/TKO') | (data['winby'] == 'DEC')][importantes].copy()
final_data = final_data[final_data['winner'].isin(['red', 'blue'])]
final_data.dropna(subset=["B__Round1_Strikes_Significant Strikes_Attempts"], inplace=True)
final_data.dropna(subset=["R__Round1_Strikes_Significant Strikes_Attempts"], inplace=True)
final_data = final_data.reset_index(drop=True)


#Acorto los nombres de las columnas para que sea menos engorroso
for f in fighter:
    for i in range(1, 6):
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Head Significant Strikes_Landed": f + "_R" + str(i) + "_Head"},
            inplace=True)
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Body Significant Strikes_Landed": f + "_R" + str(i) + "_Body"},
            inplace=True)
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Legs Significant Strikes_Landed": f + "_R" + str(i) + "_Legs"},
            inplace=True)
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Ground Significant Strikes_Landed": f + "_R" + str(i) + "_Ground"},
            inplace=True)
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Clinch Significant Strikes_Landed": f + "_R" + str(i) + "_Clinch"},
            inplace=True)
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Distance Strikes_Landed": f + "_R" + str(i) + "_Distance"},
            inplace=True)
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Significant Strikes_Landed": f + "_R" + str(i) + "_Total_L"},
            inplace=True)
        final_data.rename(
            columns={f + "__Round" + str(i) + "_Strikes_Significant Strikes_Attempts": f + "_R" + str(i) + "_Total_A"},
            inplace=True)


for category in categories:
    final_data[category] = pd.Series()

areas          = ["Head", "Body", "Legs", "Ground", "Clinch", "Distance"]
areas_extended = ["Head", "Body", "Legs", "Ground", "Clinch", "Distance", "Total_L", "Total_A"]

#Datos en los cuales realizare el analisis
final_categories = ["W_Strike_Difference", "W_Strike_Percentage","W_Strikes"]
for area in areas:
    string1 = "W_" + area + "_Difference"
    string2 = "W_" + area
    string3 = "W_" + area + "_Percentage"
    final_categories.append(string1)
    final_categories.append(string2)
    final_categories.append(string3)
final_categories.append("KO?")
final_categories.append("Fight_Time_Multiplier")
final_categories.append("PER")



#Hago que todas las celdas sean 0 para luego insertar los datos y si hay un NaN(debido a
#las peleas en las cuales solo hay 3 rounds vs 5) la suma no arroje un NaN
i = 0
while i < len(final_data):
    for f in fighter:
        for area in areas_extended:
            for j in range(1, 6):
                    final_data.loc[i, f + "_" + area] = 0
    i += 1

i = 0

#Limpieza final de datos
while i < len(final_data):
    for f in fighter:
        for area in areas_extended:
            for j in range(1, 6):
                if not np.isnan(final_data.loc[i, f + "_R" + str(j) +"_" + area]):
                    final_data.loc[i, f + "_" + area] = final_data.loc[i, f + "_" + area] + final_data.loc[i, f + "_R" + str(j) +"_" + area]
    final_data.loc[i, "Winner"] = final_data.loc[i, "winner"]
    final_data.loc[i, "Method"] = final_data.loc[i, "winby"]
    if final_data.loc[i, "winner"] == "blue":
        final_data.loc[i, "Multiplier"] = 1
    elif final_data.loc[i, "winner"] == "red":
        final_data.loc[i, "Multiplier"] = -1
    i += 1

#Realizo todas la sumatorias y operaciones para obtener los datos finales para el analisis
master = pd.DataFrame(columns=final_categories)
i = 0
while i < len(final_data):
    for area in areas:
        master.loc[i,"W_" + area + "_Difference"] = final_data.loc[i, "Multiplier"] * (final_data.loc[i, "B_" + area] - final_data.loc[i, "R_" + area])
        if final_data.loc[i, "Winner"] == "blue":
            master.loc[i, "W_" + area] = final_data.loc[i, "B_" + area]
            master.loc[i,"W_" + area + "_Percentage"] = final_data.loc[i, "B_" + area]/final_data.loc[i, "B_Total_L"]
        elif final_data.loc[i, "Winner"] == "red":
            master.loc[i, "W_" + area] = final_data.loc[i, "R_" + area]
            master.loc[i, "W_" + area + "_Percentage"] = final_data.loc[i, "R_" + area] / final_data.loc[i, "R_Total_L"]
    master.loc[i, "W_Strike_Difference"] = final_data.loc[i, "Multiplier"] * (final_data.loc[i, "B_Total_L"] - final_data.loc[i, "R_Total_L"])
    if final_data.loc[i, "Winner"] == "blue":
        master.loc[i, "W_Strike_Percentage"] = (final_data.loc[i, "B_Total_L"] / final_data.loc[i, "B_Total_A"])
        master.loc[i, "W_Strikes"] = final_data.loc[i, "B_Total_L"]
    elif final_data.loc[i, "Winner"] == "red":
        master.loc[i, "W_Strike_Percentage"] = (final_data.loc[i, "R_Total_L"] / final_data.loc[i, "R_Total_A"])
        master.loc[i, "W_Strikes"] = final_data.loc[i, "R_Total_L"]
    master.loc[i, "Last_round"] = final_data.loc[i, "Last_round"]
    master.loc[i, "Max_round"] = final_data.loc[i, "Max_round"]
    if final_data.loc[i, "winby"] == "KO/TKO":
        master.loc[i, "KO?"] = True
        #Utilizo un multiplicar el tiempo total de lucha para comparar si todas las peleas fuesen de igual tiempo
        master.loc[i, "Fight_Time_Multiplier"] = 3 * 5 / (
                        ((final_data.loc[i, "Last_round"] - 1) * 5 + 2.5))
        if final_data.loc[i, "Last_round"] == 1:
            if master.loc[i, "Fight_Time_Multiplier"] >= 2.5:
                master.loc[i, "Fight_Time_Multiplier"] = 2.5
        if final_data.loc[i, "Last_round"] == 2:
            if master.loc[i, "Fight_Time_Multiplier"] >= 1.5:
                master.loc[i, "Fight_Time_Multiplier"] = 1.5

    if final_data.loc[i, "winby"] == "DEC":
        master.loc[i, "KO?"] = False
        master.loc[i, "Fight_Time_Multiplier"] = 1
    master.loc[i, "PER"] = master.loc[i, "W_Strikes"] * master.loc[i, "Fight_Time_Multiplier"]
    i += 1

#Descarto peleas que tengan mas que el record de golpes, peleas que el ganador no tiene golpes y que el tiempo de lucha es mayor a la cantidad posible por rounds
master = master.drop(master[master['W_Strikes'] >= 581].index)
master = master.drop(master[master['W_Strikes'] <= 1].index)
master = master.drop(master[master['Fight_Time_Multiplier'] < 1].index)
print(master)
#Creo un excel aparte para que cada vez que corro el programa no tenga que obtener los dataframes nuevamente
master.to_excel('master.xlsx', index=False)