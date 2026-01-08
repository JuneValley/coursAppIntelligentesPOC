import numpy as np
import pandas
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

df = pandas.read_csv("consommation_electrique.csv")

predict_data = [
[5, 1, 0, 3, 0, 18, 73, 34] ,
[5, 1, 1, 3, 0, 18, 76, 34] ,
[5, 1, 2, 3, 0, 20, 75, 34] ,
[5, 1, 3, 3, 0, 19, 81, 34] ,
[5, 1, 4, 3, 0, 18, 74, 34] ,
[5, 1, 5, 3, 0, 20, 82, 34] ,
[5, 1, 6, 3, 0, 18, 81, 34] ,
[5, 1, 7, 3, 0, 19, 80, 34] ,
[5, 1, 8, 3, 0, 20, 82, 34] ,
[5, 1, 9, 3, 0, 20, 81, 34] ,
[5, 1, 10, 3, 0, 18, 78, 34] ,
[5, 1, 11, 3, 0, 19, 81, 34] ,
[5, 1, 12, 3, 0, 19, 82, 34] ,
[5, 1, 13, 3, 0, 20, 82, 34] ,
[5, 1, 14, 3, 0, 20, 73, 34] ,
[5, 1, 15, 3, 0, 18, 73, 34] ,
[5, 1, 16, 3, 0, 18, 73, 34] ,
[5, 1, 17, 3, 0, 20, 74, 34] ,
[5, 1, 18, 3, 0, 18, 77, 34] ,
[5, 1, 19, 3, 0, 19, 81, 34] ,
[5, 1, 20, 3, 0, 20, 78, 34] ,
[5, 1, 21, 3, 0, 19, 74, 34] ,
[5, 1, 22, 3, 0, 18, 80, 34] ,
[5, 1, 23, 3, 0, 19, 72, 34] ,
]

def encode_pipeline(df):
    """Encodage des colonnes catégorielles"""
    df['jour_semaine'] = df['jour_semaine'].astype('category').cat.codes
    df['jour_ferie'] = df['jour_ferie'].astype('category').cat.codes
    df['saison'] = df['saison'].astype('category').cat.codes
    df['meteo'] = df['meteo'].astype('category').cat.codes
    return df

df_clean = encode_pipeline(df)

X = df[['jour_semaine', 'jour_ferie', 'heure', 'saison', 'meteo', 'temperature', 'vitesse_vent', 'prix_kwh']]
y = df['consommation_gw']

clf = RandomForestRegressor()
clf.fit(X, y)

predict_final = []
predict_display = []

for hour in predict_data:
    predict_final.append(clf.predict([[hour[0], hour[1], hour[2], hour[3], hour[4], hour[5], hour[6], hour[7]]]))

for final in predict_final:
    predict_display.append(final[0])

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
plt.bar(x,predict_display)
plt.show()