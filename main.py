import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle

pickle_in = open('Diabetes.pkl', 'rb')
classifier = pickle.load(pickle_in)

def predict():
    st.sidebar.header('GenomicsMaster Co.')
    # select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
    # if not st.sidebar.checkbox("Hide", True, key='2'):
    st.title('GenomicsMaster (Illness Prediction Based on Genome)')
    st.markdown('This trained dataset is originally collected by GenomicsMaster Company.')
    st.markdown('It will be very greatful if you share your data in this regard with us.')

    name = st.text_input("Name:")
    pregnancy = st.number_input("CHROM:")
    st.markdown('Chromosome the variant is located on')
    
    glucose = st.number_input("POS:")
    st.markdown('Position on the chromosome the variant is located on')

    bp =  st.number_input("REF:")
    st.markdown('Reference Allele')

    skin = st.number_input("ALT:")
    st.markdown('Alternaete Allele')

   

        

    age = st.number_input("CLNDN:")
    st.markdown('Preferred ClinVar disease name for the concept specified by disease identifiers in CLNDISDB:')



    submit = st.button('Predict')
    st.markdown('Outcome: Class variable (0 or 1)')

    if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write('Congratulation!', name,'It seems you have selected a fit type of Antibiotic')
        else:
            st.write(name,", It seems you can choose a more fitted Antibiotic")

def main():
    new_title = '<p style="font-size: 42px;">Welcome The Congenital Disabilities Prediction App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)
    read_me = st.markdown("""
    The application is built using Streamlit  
    to demonstrate Fit Type of Antibiotic Prediction. It performs prediction on multiple parameters
                                  """)
    st.sidebar.title("Select Activity")
    choice = st.sidebar.selectbox(
        "MODE", ("About", "Predict Antibiotic Type Effects"))
    if choice == "Predict Antibiotic Type Effects":
        read_me_0.empty()
        read_me.empty()
        predict()
    elif choice == "About":
        print()


if __name__ == '__main__':
    main()
    
