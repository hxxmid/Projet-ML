import pandas as pd

# Charger les données depuis le fichier CSV
data = pd.read_csv('Cardetails.csv')

# Filtrer les lignes où la colonne 'name' est égale à 1
filtered_data = data.loc[data['name'] == 1]

# Calculer le maximum et le minimum de la colonne 'km_driven'
max_km_driven = filtered_data['km_driven'].max()
min_km_driven = filtered_data['km_driven'].min()

print("Maximum de 'km_driven' pour 'name' = 1:", max_km_driven)
print("Minimum de 'km_driven' pour 'name' = 1:", min_km_driven)
