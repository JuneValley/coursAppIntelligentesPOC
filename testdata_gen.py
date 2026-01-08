import random

predict_data = []

# -----------------------------
# Paramètres fixes pour la journée
# -----------------------------
jour_semaine = random.randint(0, 6)          # 0 = Lundi, 6 = Dimanche
jour_ferie = 1 if jour_semaine >= 5 else 0
saison = random.randint(0, 3)                # 0=Printemps, 3=Hiver
meteo = random.randint(0, 3)                 # 0=Ensoleillé, 3=Neigeux

# Conditions météo globales de la journée
temperature_jour = random.randint(-10, 40)
vitesse_vent_jour = random.randint(0, 100)
prix_kwh_jour = random.randint(10, 50)

# -----------------------------
# Génération horaire
# -----------------------------
for heure in range(24):
    # Petite variation horaire réaliste
    temperature = temperature_jour + random.randint(-1, 1)
    vitesse_vent = max(0, vitesse_vent_jour + random.randint(-5, 5))

    predict_data.append([
        jour_semaine,
        jour_ferie,
        heure,
        saison,
        meteo,
        temperature,
        vitesse_vent,
        prix_kwh_jour
    ])

# -----------------------------
# Affichage
# -----------------------------
for ligne in predict_data:
    print(ligne, ',')
