import random
import csv
import math

# -----------------------------
# Paramètres globaux
# -----------------------------
NB_LIGNES = 1200
FICHIER_SORTIE = "consommation_electrique.csv"

jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
saisons = ["Printemps", "Été", "Automne", "Hiver"]
meteo_types = ["Ensoleillé", "Nuageux", "Pluvieux", "Neigeux"]

# -----------------------------
# Fonctions utilitaires
# -----------------------------

def est_ferie(jour):
    return jour in ["Samedi", "Dimanche"]

def effet_temperature(temp):
    """
    Consommation minimale vers 20°C.
    Chauffage si froid, climatisation si chaud.
    """
    return abs(temp - 20) * 0.8

def effet_heure(heure):
    """
    Variation douce de la consommation sur la journée :
    - minimum la nuit
    - pic le matin
    - pic plus fort le soir
    """
    # Cycle journalier lissé
    cycle_jour = 10 * math.sin((heure - 6) * math.pi / 12)

    # Pic du soir (retour à la maison)
    pic_soir = 8 * math.exp(-0.5 * ((heure - 19) / 2) ** 2)

    return cycle_jour + pic_soir

def effet_saison(saison):
    if saison == "Hiver":
        return 15
    elif saison == "Été":
        return 10
    elif saison == "Automne":
        return 5
    else:
        return 0

def effet_meteo(meteo):
    if meteo == "Neigeux":
        return 10
    elif meteo == "Pluvieux":
        return 5
    else:
        return 0

def effet_prix(prix_kwh):
    """
    Sobriété énergétique quand le prix augmente
    """
    return -(prix_kwh - 10) * 0.3

def temperature_ressentie(temp, vent):
    """
    Refroidissement éolien simplifié
    """
    return temp - (vent * 0.05)

# -----------------------------
# Génération du dataset
# -----------------------------

with open(FICHIER_SORTIE, mode="w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)

    # En-têtes CSV
    writer.writerow([
        "jour_semaine",
        "jour_ferie",
        "heure",
        "saison",
        "meteo",
        "temperature",
        "vitesse_vent",
        "prix_kwh",
        "consommation_gw"
    ])

    for _ in range(NB_LIGNES):
        jour = random.choice(jours_semaine)
        ferie = est_ferie(jour)
        heure = random.randint(0, 23)
        saison = random.choice(saisons)
        meteo = random.choice(meteo_types)

        temperature = random.randint(-10, 40)
        vent = random.randint(0, 100)
        prix_kwh = random.randint(10, 50)

        temp_ress = temperature_ressentie(temperature, vent)

        # Base nationale moyenne
        consommation = 50

        # Effets cumulés
        consommation += effet_temperature(temp_ress)
        consommation += effet_heure(heure)
        consommation += effet_saison(saison)
        consommation += effet_meteo(meteo)
        consommation += effet_prix(prix_kwh)

        # Effet jour ouvré / férié
        if not ferie:
            consommation += 10
        else:
            consommation -= 5

        # Bruit aléatoire
        consommation += random.uniform(-5, 5)

        # Clamp réaliste
        # consommation = max(20, min(100, round(consommation, 2)))
        consommation = round(consommation, 2)

        writer.writerow([
            jour,
            ferie,
            heure,
            saison,
            meteo,
            temperature,
            vent,
            prix_kwh,
            consommation
        ])

print(f"Dataset généré avec succès : {FICHIER_SORTIE}")
