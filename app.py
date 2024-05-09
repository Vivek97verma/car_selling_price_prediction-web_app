import streamlit as st
import pickle
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# open the pickle file in read-binary mode
with open('lr_model_car_price_prediction.pkl','rb') as file:
    #load the pickle model
    lr1=pickle.load(file)
with open('dt_model_car_price_prediction.pkl','rb') as file:
    dt1=pickle.load(file)
with open('rf_model_car_price_prediction.pkl','rb') as file:
    rf1=pickle.load(file)
with open('ad_model_car_price_prediction.pkl','rb') as file:
    ad1=pickle.load(file)
    
    
st.title('car selling price prediction app')

st.header('fill the detail to generate the selling price')

options= st.sidebar.selectbox('select ML model',['Lin_Reg','Random_Forest','Decision_Tree','AdaBoost'])


# Form widgets
# Input box,slider,drop down

year=st.slider('Year',1992,2017)
km_driven=st.slider('km_driven',5000,120000)
fuel=st.selectbox('fuel',['Diesel','Petrol','CNG','LPG','Electric'])
seller_type=st.selectbox('seller_type',['Individual','Dealer','Trustmark Dealer'])
transmission=st.selectbox('transmission',['Manual','Automatic'])
owner=st.selectbox('owner',['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])
car_name=st.selectbox('car_name',['Maruti','Hyundai','Mahindra','Tata','Ford','Honda','Toyota','Chevrolet','Renault',
                                  'Volkswagen','Nissan','Skoda','Fiat','Audi','Datsun','BMW','Mercedes-Benz','others'])


if st.button('Predict'):
    if  transmission=='Manual':
        transmission=1
    else:
        transmission=0
        
    if  owner=='First Owner':
        owner=0
        
    elif owner=='Fourth & Above Owner':
        owner=1
        
    elif owner=='Second Owner':
        owner=2
    
    elif owner=='Test Drive Car':
        owner=3
        
    else:
        owner=4
        
        
    if seller_type=='Dealer':
        seller_type=0
        
    if seller_type=='Individual':
        seller_type=1
        
    if seller_type=='Trustmark Dealer':
        seller_type=2
        
        
    if car_name=='Audi':
        car_name=0
        
    if car_name=='BMW':
        car_name=1
        
    if car_name=='Chevrolet':
        car_name=2
        
    if car_name=='Datsun':
        car_name=3
    
    if car_name=='Fiat':
        car_name=4
        
    if car_name=='Ford':
        car_name=5
        
    if car_name=='Honda':
        car_name=6
        
    if car_name=='Hyundai':
        car_name=7
        
    if car_name=='Mahindra':
        car_name=8
        
    if car_name=='Maruti':
        car_name=9
        
    if car_name=='Mercedes-Benz':
        car_name=10
        
    if car_name=='Nissan':
        car_name=11
        
    if car_name=='Renault':
        car_name=12
        
    if car_name=='Skoda':
        car_name=13
        
    if car_name=='Tata':
        car_name=14
        
    if car_name=='Toyota':
        car_name=15
        
    if car_name=='Volkswagen':
        car_name=16
        
    if car_name=='':
        car_name=17
    else:
        car_name=33
        
        
    if fuel=='CNG':
        fuel=0
        
    if fuel=='Diesel':
        fuel=1
        
    if fuel=='Electric':
        fuel=2
        
    if fuel=='LPG':
        fuel=3
        
    else:
        fuel=4
        
        
        
    test=np.array([year,km_driven,fuel,seller_type,transmission,owner,car_name])
    test=test.reshape(1,7)
    if options == "Lin_Reg":
        st.success(lr1.predict(test)[0])
    elif options == "Decision_Tree":
        st.success(dt1.predict(test)[0])
    else:
        st.success(rf1.predict(test)[0])