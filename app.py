import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl','rb'))

st.header('Prévision du prix des voitures')

cars_data = pd.read_csv('Cardetails.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
cars_data['name'] = cars_data['name'].apply(get_brand_name)

name = st.selectbox('Sélectionnez la marque de la voiture', cars_data['name'].unique())
year = st.slider('Année de fabrication de la voiture', 1994,2024)
km_driven = st.slider('Nombre de km parcourus', 11,200000)
fuel = st.selectbox('Type de carburant', cars_data['fuel'].unique())
seller_type = st.selectbox('Type de vendeur', cars_data['seller_type'].unique())
transmission = st.selectbox('Type de transmission', cars_data['transmission'].unique())
owner = st.selectbox('Nombre de mains', cars_data['owner'].unique())
mileage = st.slider('Kilométrage de la voiture', 10,40)
engine = st.slider('Moteur CC', 700,5000)
max_power = st.slider('Maximum d''énergie', 32,200)
seats = st.slider('Nombre de sièges', 5,10)


if st.button("Predict"):
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
                          [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                          ,inplace=True)

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
        car_price_in_inr_rounded = round(car_price_in_inr, 4)

        # Afficher le prix en euros et en roupies indiennes avec quatre chiffres après la virgule
        st.markdown('Car Price is going to be {:.4f} euros'.format(car_price_in_euro_rounded))
        st.markdown('Car Price is going to be {:.4f} roupies indiennes'.format(car_price_in_inr_rounded))


