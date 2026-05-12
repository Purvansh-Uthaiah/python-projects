import streamlit as st
import plotly.graph_objs as go

st.title("BMI calculator")
st.header("BMI means body mass index")
st.subheader("Do not worry BMI is not the ultimate health index")

unit = st.sidebar.selectbox("Select the Unit", ["U.S Units", "Metric Units"])
age = st.sidebar.number_input("Select the Age", min_value=1, max_value=100, value=28)
gender = st.radio("Gender", ['Male','Female'],horizontal = True)
bmi_val = 0

col1, col2 = st.columns(2)

if unit == 'U.S Units':
    with col1:
        ht_ft = st.selectbox("Feet", list(range(1, 9)), index=5)
    with col2:
        ht_in = st.selectbox("Inches", list(range(0, 12)), index=0)
    wt_pd = st.number_input("Weight in pounds", value=140.00)
    if st.button("Calculate BMI") == True:
      bmi_val = st.write((wt_pd)/((ht_ft*12+ht_in)**2)*703)

elif unit == 'Metric Units':
    ht_cms = st.number_input("Height in cms", value=170.00)
    wt_kg = st.slider("Weight in kilos", 1.00, 128.00, step=0.5, value=60.0)
    if st.button("Calculate BMI") == True:
        bmi_val = st.write(wt_kg/((ht_cms/100)**2))

fig = go.Figure(go.Indicator(
    mode = 'gauge+number',
    value = bmi_val,
    title = {'text': "BMI Value"},
    gauge = {
        'axis': {'range': [10,40]},
        'steps':[
            {'range': [10,15], 'color': 'Red'},
            {'range':[15,18], 'color': 'Orange'},
            {'range': [18,25], 'color': 'Green'},
            {'range': [25,28], 'color': 'Yellow'},
            {'range': [28,32], 'color': 'Orange'},
            {'range': [32,36], 'color': 'Red'},
            {'range': [36,40], 'color': 'Maroon'}
        ],
        'threshold': {
            'line': {'color': 'White', 'width' : 4},
            'thickness': 0.75,
            'value': bmi_val

        }

    }

))
st.plotly_chart(fig)