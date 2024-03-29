import pandas as pd
import pickle as pk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go


    # Fonction pour afficher l'histogramme de la distribution des prix de vente
import streamlit as st
import pandas as pd

def afficher_graphiques(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['selling_price'], kde=True, color='skyblue', edgecolor='black')
    plt.title('Distribution des prix de vente', fontsize=16, color='navy')
    plt.xlabel('Prix de vente', fontsize=14, color='navy')
    plt.ylabel('Fréquence', fontsize=14, color='navy')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(fontsize=12, color='navy')
    plt.yticks(fontsize=12, color='navy')
    st.pyplot()

    avg_price_by_brand = df.groupby('name')['selling_price'].mean().sort_values(ascending=False)
    top_10_brands = avg_price_by_brand.head(10)

    fig = go.Figure(data=[go.Bar(
        x=top_10_brands.values,
        y=top_10_brands.index,
        orientation='h',
        marker_color='blue'
    )])

    fig.update_layout(
        title="Top 10 des marques par prix moyen",
        xaxis_title="Prix moyen",
        yaxis_title="Marque",
        yaxis=dict(autorange="reversed")
    )

    fig.show()

    plt.figure(figsize=(12, 8))
    avg_price_by_year = df.groupby('year')['selling_price'].mean()
    avg_price_by_year.plot(kind='line', marker='o', color='royalblue', linewidth=2)
    plt.title('Prix moyen par année de fabrication', fontsize=18, color='navy', fontweight='bold')
    plt.xlabel('Année de fabrication', fontsize=14, color='navy')
    plt.ylabel('Prix moyen (en €)', fontsize=14, color='navy')
    plt.xticks(fontsize=12, color='navy')
    plt.yticks(fontsize=12, color='navy')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(df['selling_price'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Prix de vente')
    plt.ylabel('Fréquence')
    plt.title('Distribution des prix de vente des voitures')

    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink',
              'lightsteelblue', 'lightseagreen', 'lightgrey', 'lightcyan', 'lightyellow',
              'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightsalmon',
              'lightpink', 'lightsteelblue', 'lightseagreen', 'lightgrey', 'lightcyan']

    for i, patch in enumerate(plt.gca().patches):
        patch.set_facecolor(colors[i % len(colors)])

    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='fuel', y='selling_price', data=df, palette='muted')
    plt.xlabel('Type de carburant')
    plt.ylabel('Prix de vente')
    plt.title('Répartition des prix de vente par type de carburant')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.scatter(df['km_driven'], df['selling_price'], alpha=0.5, color='blue')
    plt.xlabel('Kilométrage parcouru', fontsize=12, fontweight='bold', color='darkblue')
    plt.ylabel('Prix de vente', fontsize=12, fontweight='bold', color='darkblue')
    plt.title('Relation entre le kilométrage et le prix de vente', fontsize=14, fontweight='bold', color='darkgreen')
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='seller_type', y='selling_price', data=df, estimator=np.mean, palette='coolwarm')
    plt.xlabel('Type de vendeur', fontsize=12, fontweight='bold', color='darkblue')
    plt.ylabel('Prix de vente moyen', fontsize=12, fontweight='bold', color='darkblue')
    plt.title('Prix de vente moyen par type de vendeur', fontsize=14, fontweight='bold', color='darkgreen')
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='owner', y='selling_price', data=df, palette='muted')
    plt.xlabel('Nombre de propriétaires', fontsize=12, fontweight='bold', color='darkblue')
    plt.ylabel('Prix de vente', fontsize=12, fontweight='bold', color='darkblue')
    plt.title('Prix de vente des voitures en fonction du nombre de propriétaires', fontsize=14, fontweight='bold', color='darkgreen')
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='transmission', y='selling_price', data=df, palette='pastel')
    plt.xlabel('Type de transmission', fontsize=12, fontweight='bold', color='darkblue')
    plt.ylabel('Prix de vente', fontsize=12, fontweight='bold', color='darkblue')
    plt.title('Prix de vente des voitures en fonction du type de transmission', fontsize=14, fontweight='bold', color='darkgreen')
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.show()

# Charger le modèle
model = pk.load(open('model.pkl','rb'))

# Charger les données sur les voitures
cars_data = pd.read_csv('Cardetails.csv')

# Fonction pour extraire la marque à partir du nom
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()

cars_data['name'] = cars_data['name'].apply(get_brand_name)

# Interface utilisateur avec Streamlit
st.header('Prévision du prix des voitures')

tabs = ["Modèle ML", "Graphiques"]
page = st.sidebar.selectbox("Choisissez une page", tabs)
# Sidebar pour choisir entre le modèle ML et les graphiques


# Page pour le modèle ML
if page == "Modèle ML":
    name = st.selectbox('Sélectionnez la marque de la voiture', cars_data['name'].unique())
    year = st.slider('Année de fabrication de la voiture', 1994,2024)
    km_driven = st.slider('Nombre de km parcourus', 11,200000)
    fuel = st.selectbox('Type de carburant', cars_data['fuel'].unique())
    seller_type = st.selectbox('Type de vendeur', cars_data['seller_type'].unique())
    transmission = st.selectbox('Type de transmission', cars_data['transmission'].unique())
    owner = st.selectbox('Nombre de mains', cars_data['owner'].unique())
    mileage = st.slider('KM par Litre', 10,40)
    engine = st.slider('Moteur CC', 700,5000)
    max_power = st.slider('Maximum d''énergie', 32,200)
    seats = st.slider('Nombre de sièges', 5,10)

    if st.button("Prédire"):
        input_data_model = pd.DataFrame(
        [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]],
        columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])

        input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
           'Fourth & Above Owner', 'Test Drive Car'],
                               [1,2,3,4,5], inplace=True)
        input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4], inplace=True)
        input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3], inplace=True)
        input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2], inplace=True)
        input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
           'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
           'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
           'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
           'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                              [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],inplace=True)

        car_price = model.predict(input_data_model)

        # Suppose car_price[0] représente le prix en roupies indiennes
        car_price_in_inr = car_price[0]
        # Conversion de roupies indiennes en euros
        car_price_in_euro = car_price_in_inr / 1000 * 11

        # Vérifier si le prix en euros est négatif
        if car_price_in_euro < 0:
            st.markdown("Données entrées incorrectes.")
        else:
            # Arrondir le prix en euros à quatre chiffres après la virgule
            car_price_in_euro_rounded = round(car_price_in_euro, 4)
            # Arrondir le prix en roupies indiennes à quatre chiffres après la virgule
            car_price_in_dza_rounded = round(car_price_in_inr, 4)

            # Afficher le prix en euros et en roupies indiennes avec quatre chiffres après la virgule
            st.markdown('Le prix de la voiture sera {:.4f} euros'.format(car_price_in_euro_rounded))
            st.markdown('Le prix de la voiture sera {:.4f} DZA'.format(car_price_in_dza_rounded))

# Page pour les graphiques
else:
    df = pd.read_csv('Cardetails.csv')

    def plot_price_distribution(df):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df['selling_price'], kde=True, color='skyblue', edgecolor='black', ax=ax)
        ax.set_title('Distribution des prix de vente', fontsize=16, color='navy')
        ax.set_xlabel('Prix de vente', fontsize=14, color='navy')
        ax.set_ylabel('Fréquence', fontsize=14, color='navy')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.tick_params(axis='x', labelsize=12, colors='navy')
        ax.tick_params(axis='y', labelsize=12, colors='navy')
        st.pyplot(fig)


    # Fonction pour afficher le top 10 des marques par prix moyen
    def plot_top_10_brands(df):
        avg_price_by_brand = df.groupby('name')['selling_price'].mean().sort_values(ascending=False).head(10)
        fig = go.Figure(data=[go.Bar(
            x=avg_price_by_brand.values,
            y=avg_price_by_brand.index,
            orientation='h',
            marker_color='blue'
        )])
        fig.update_layout(
            title="Top 10 des marques par prix moyen",
            xaxis_title="Prix moyen",
            yaxis_title="Marque",
            yaxis=dict(autorange="reversed")
        )
        st.plotly_chart(fig)


    # Fonction pour afficher la relation entre l'année de fabrication et le prix moyen
    def plot_avg_price_by_year(df):
        avg_price_by_year = df.groupby('year')['selling_price'].mean()
        fig, ax = plt.subplots(figsize=(12, 8))
        avg_price_by_year.plot(kind='line', marker='o', color='royalblue', linewidth=2, ax=ax)
        ax.set_title('Prix moyen par année de fabrication', fontsize=18, color='navy', fontweight='bold')
        ax.set_xlabel('Année de fabrication', fontsize=14, color='navy')
        ax.set_ylabel('Prix moyen (en €)', fontsize=14, color='navy')
        ax.tick_params(axis='x', labelsize=12, colors='navy')
        ax.tick_params(axis='y', labelsize=12, colors='navy')
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)


    # Fonction pour afficher la distribution des prix de vente avec des couleurs différentes
    def plot_price_distribution_colors(df):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df['selling_price'], bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Prix de vente')
        ax.set_ylabel('Fréquence')
        ax.set_title('Distribution des prix de vente des voitures')
        colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink',
                  'lightsteelblue', 'lightseagreen', 'lightgrey', 'lightcyan', 'lightyellow',
                  'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightsalmon',
                  'lightpink', 'lightsteelblue', 'lightseagreen', 'lightgrey', 'lightcyan']
        for i, patch in enumerate(ax.patches):
            patch.set_facecolor(colors[i % len(colors)])
        st.pyplot(fig)


    def plot_price_by_seller_type(df):
        fig = plt.figure(figsize=(10, 6))
        sns.barplot(x='seller_type', y='selling_price', data=df, estimator=np.mean, palette='coolwarm')
        plt.xlabel('Type de vendeur', fontsize=12, fontweight='bold', color='darkblue')
        plt.ylabel('Prix de vente moyen', fontsize=12, fontweight='bold', color='darkblue')
        plt.title('Prix de vente moyen par type de vendeur', fontsize=14, fontweight='bold', color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        st.pyplot(fig)  # Display the plot in Streamlit


    def plot_price_by_km_driven(df):
        plt.figure(figsize=(10, 6))
        plt.scatter(df['km_driven'], df['selling_price'], alpha=0.5, color='blue')
        plt.xlabel('Kilométrage parcouru', fontsize=12, fontweight='bold', color='darkblue')
        plt.ylabel('Prix de vente', fontsize=12, fontweight='bold', color='darkblue')
        plt.title('Relation entre le kilométrage et le prix de vente', fontsize=14, fontweight='bold',
                  color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()


    def plot_price_by_owner(df):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='owner', y='selling_price', data=df, palette='muted')
        plt.xlabel('Nombre de propriétaires', fontsize=12, fontweight='bold', color='darkblue')
        plt.ylabel('Prix de vente', fontsize=12, fontweight='bold', color='darkblue')
        plt.title('Prix de vente des voitures en fonction du nombre de propriétaires', fontsize=14, fontweight='bold',
                  color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()
    # Autres fonctions pour les autres graphiques ...
    def plot_price_by_transmission(df):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='transmission', y='selling_price', data=df, palette='pastel')
        plt.xlabel('Type de transmission', fontsize=12, fontweight='bold', color='darkblue')
        plt.ylabel('Prix de vente', fontsize=12, fontweight='bold', color='darkblue')
        plt.title('Prix de vente des voitures en fonction du type de transmission', fontsize=14, fontweight='bold',
                  color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()
    # Fonction pour afficher tous les graphiques
    def display_all_plots(df):
        plot_avg_price_by_year(df)
        plot_price_distribution_colors(df)
        plot_top_10_brands(df)
        plot_price_distribution(df)
        plot_price_by_km_driven(df)
        plot_price_by_km_driven(df)
        plot_price_by_owner(df)
        plot_price_by_transmission(df)
        # Appeler d'autres fonctions pour afficher d'autres graphiques ici




    # Charger les données
    df = pd.read_csv('Cardetails.csv')

    # Appeler la fonction pour afficher tous les graphiques
    display_all_plots(df)


