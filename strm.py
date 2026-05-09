import streamlit as st
import plotly.graph_objs as go

st.title("BMI Calculator")
st.header("BMI (Body Mass Index) is a measurement tool that calculates the body fat % of an individual and decides whether he/she is Healthy or not  ")
st.subheader("Caution !!!,BMI is not the ultimate tool measure a persons health. A person in healthy weight range in the BMI might not me healthy, and a person who is not in the healthy weight range might still be healthy if there is more muscle mass. ")

# Selecting the unit and other important parameters
unit = st.sidebar.selectbox("Select the Unit ", ['U.S units', 'Metric Units'])
age = st.sidebar.number_input(label="Select the Age", min_value=1, max_value=100, value=28)
gender = st.radio("Select the Gender", ['Male', 'Female'],horizontal=True)
bmi_val = 0

#creating two columns fo ft
col1, col2 = st.columns(2)

if unit == 'U.S units':
    with col1:
     height_ft = st.selectbox("Feet", list(range(1,9)),index  = 4)
    with col2:
     height_in = st.selectbox("Inches", list(range(0,12)))
    weight_lb = st.number_input(label="Weight in pounds ", value= 140)
    height = (height_ft)*12 + height_in
    if st.button("Calculate BMI"):
        bmi_val = (((weight_lb)/(height)**2)*703)
        st.write(f"Your BMI is :", {bmi_val})

elif unit == 'Metric Units':
    height_cm = st.number_input("Height in Cm's", value = 170)
    weight_kg = st.slider("weight in kilos ", 1.00, 135.00, step = 0.5,value = 60.00 )
    if st.button("Calculate Metric BMI"):
     bmi_val = ((weight_kg)/(height_cm/100)**2)
     st.write(f"Your BMI is :",{bmi_val})


fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = bmi_val,
    title = {'text': "BMI Value"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range':[10,40]},
        'steps': [
            {'range': [10,15], 'color':'Red'},
            {'range': [15,17], 'color':'Orange'},
            {'range': [17,18.5], 'color': 'Yellow'},
            {'range': [18.5,25], 'color': 'Green'},
            {'range': [25,28], 'color': 'Yellow'},
            {'range': [28,32], 'color': 'Orange'},
            {'range': [30,36], 'color': 'Red'},
            {'range': [36,40], 'color': 'Maroon'}
        ],
        'threshold': {
            'line': {'color':'White', 'width': 4},
            'thickness': 0.75,
            'value': bmi_val
        }


    }
))
st.plotly_chart(fig)