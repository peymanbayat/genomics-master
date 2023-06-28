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
    st.sidebar.header('Diabetes Prediction')
    # select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
    # if not st.sidebar.checkbox("Hide", True, key='2'):
    st.title('Diabetes Prediction(Only for Females Above 21 Years of Age)')
    st.markdown('This trained dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to predict based on diagnostic measurements whether a patient has diabetes.')
    st.markdown('Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.')

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
    st.markdown('ClinVar's preferred disease name for the concept specified by disease identifiers in CLNDISDB')


    submit = st.button('Predict')
    st.markdown('Outcome: Class variable (0 or 1)')


    if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write('Congratulation!',name,'You are not diabetic')
        else:
            st.write(name,", we are really sorry to say but it seems like you are Diabetic. But don't lose hope, we have suggestions for you:")
            st.markdown('[Visit Here](https://www.mayoclinic.org/diseases-conditions/type-2-diabetes/in-depth/diabetes-prevention/art-20047639#:~:text=Diabetes%20prevention%3A%205%20tips%20for%20taking%20control%201,Skip%20fad%20diets%20and%20make%20healthier%20choices%20)')


def main():
    new_title = '<p style="font-size: 42px;">Welcome The Diabetes Prediction App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)
    read_me = st.markdown("""
    The application is built using Streamlit  
    to demonstrate Diabetes Prediction. It performs prediction on multiple parameters
    [here](https://github.com/).""")
    st.sidebar.title("Select Activity")
    choice = st.sidebar.selectbox(
        "MODE", ("About", "Predict Diabetes"))
    if choice == "Predict Diabetes":
        read_me_0.empty()
        read_me.empty()
        predict()
    elif choice == "About":
        print()


if __name__ == '__main__':
    main()
