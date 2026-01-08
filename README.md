# POC de prédiction de la consommation électrique d'un pays

Ce POC a pour objectif de démontrer la possibilité de prédire la consommation électrique d'un pays à l'aide de variables connues qui ont un impact sur la consommation.
Le dépôt présente 4 fichiers :
- `consommation_electrique.csv` est le jeu de données utilisé pour entraîner le modèle de prédiction
- `dataset_gen.py` permet de générer un dataset fictif
- `testdata_gen.py` permet de générer des données fictives pour tester le modèle
- `model.py` est le script qui entraîne le modèle à partir du jeu de données, le teste sur des données fictives et en affiche les résultats dans un graphique.

## Comment faire une prédiction

Vous pouvez utiliser le dataset déjà existant ou bien en générer un nouveau en lançant le script `dataset_gen.py`.
Vous pouvez utiliser les données de test présentes dans le script `model.py` ou en générer des nouvelles en lançant le script `testdata_gen.py` et en copiant les données dans le tableau `predict_data`.

Pour obtenir la prédiction sur la journée, lancer le script `model.py` et un graphique de la consommation par heure s'affichera.

<img width="554" height="413" alt="image" src="https://github.com/user-attachments/assets/4cf68c28-7933-4c83-83a5-08c7c4739e42" />
