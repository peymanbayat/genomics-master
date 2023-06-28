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
    st.title('GenomicsMaster Prediction Product')
    st.markdown('This trained dataset is originally collected by GenomicsMaster Company.')
    st.markdown('A Genome-Base Tool to Predict Future Possible Illnesses')

    name = st.text_input("Name:")
    pregnancy = st.number_input("CHROM:")
    st.markdown('Chromosome the variant is located on')

    glucose = st.number_input("POS:")
    st.markdown('Position on the chromosome the variant is located on')

    bp =  st.number_input("REF:")
    st.markdown('Reference Allele')

    skin = st.number_input("ALT:")
    st.markdown('Alternaete Allele')

    insulin = st.number_input("AF_ESP:")
    st.markdown('Allele frequencies from GO-ESP')


    bmi = st.number_input("CLNDISDB:")
    st.markdown('Tag-value pairs of disease database name and identifier')

    dpf = st.number_input("CLNDISDBINCL:")
    st.markdown('For included Variant: Tag-value pairs of disease database name and identifier')


    age = st.number_input("CLNDN:")
    st.markdown('Preferred ClinVar disease name for the concept specified by disease identifiers in CLNDISDB')


    submit = st.button('Predict')
    st.markdown('Outcome: Class variable (0 or 1)')


    if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write('Congratulation!',name,'The Probability of Your Ilness is Very Low')
        else:
            st.write(name,", The Probability of Your Ilness is Relatively High")
             

def main():
    new_title = '<p style="font-size: 42px;">Welcome Ilnesses Possibility Prediction App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)
    read_me = st.markdown("""
    The application is built using Streamlit  
                                  """)
    
    st.sidebar.title("Select Activity")
    choice = st.sidebar.selectbox(
        "MODE", ("About", "Predict Future Possible Illnesses"))
    if choice == "Predict Illness":
        read_me_0.empty()
        read_me.empty()
        predict()
    elif choice == "About":
        print()


if __name__ == '__main__':
    main()
