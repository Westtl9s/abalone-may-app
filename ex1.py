import streamlit as st
import pandas as pd

st.write("""
### Hello!
""")

st.sidebar.header('User Input')
st.sidebar.subheader('Please enter your data:')



def get_input():
    #widgets
    v_Sex = st.sidebar.radio('Sex', ['Male','Female','Infant'])
    v_Length = st.sidebar.slider('Length', 0.075, 0.745, 0.506)
    v_Height = st.sidebar.slider('Height', 0.055, 0.60, 0.4)
    v_Diameter = st.sidebar.slider('Diameter', 0.01, 0.24, 0.13)
    v_Whole_weight = st.sidebar.slider('Whole Weight', 0.002, 2.55, 0.78)
    v_Shucked_weight = st.sidebar.slider('Shucked Weight', 0.001, 1.07, 0.3)
    v_Viscera_weight = st.sidebar.slider('Viscera Weight', 0.0005, 0.54, 0.17)
    v_Shell_weight = st.sidebar.slider('Shell Weight', 0.001, 1.005, 0.24)
    

    if v_Sex == 'Male': v_Sex = 'M'
    elif v_Sex == 'Female': v_Sex = 'F'
    else: v_Sex = 'I'

    #dictionary
    data = {'Sex': v_Sex,
            'Length': v_Length,
            'Height': v_Height,
            'Diameter': v_Diameter,
            'Whole_weight': v_Whole_weight,
            'Shucked_weight': v_Shucked_weight,
            'Viscera_weight': v_Viscera_weight,
            'Shell_weight': v_Shell_weight}

    #create data frame
    data_df = pd.DataFrame(data, index=[0])
    return data_df

df = get_input()

st.write(df)

