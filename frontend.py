import streamlit as st
import requests

# Define the API endpoint
API_URL = 'http://127.0.0.1:3000/predict'

# Set up the Streamlit app
st.title('Iris Flower Prediction App')
st.write("Adjust the sliders to input the features of the Iris flower and get a prediction.")

# Sliders for the Iris features
sepal_length = st.slider('Sepal Length', min_value=0.0, max_value=10.0, step=0.1, value=5.1)
sepal_width = st.slider('Sepal Width', min_value=0.0, max_value=10.0, step=0.1, value=3.5)
petal_length = st.slider('Petal Length', min_value=0.0, max_value=10.0, step=0.1, value=1.4)
petal_width = st.slider('Petal Width', min_value=0.0, max_value=10.0, step=0.1, value=0.2)

# Button to make the prediction
if st.button('Predict'):
    # Prepare the payload for the API
    data = {
        'features': [sepal_length, sepal_width, petal_length, petal_width]
    }

    # Send a POST request to the FastAPI backend
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        result = response.json()
        
        # Display the result with enhanced styling
        st.markdown(f"""
            <div style="font-size:24px; font-weight:bold; color:#1f77b4;">
                Predicted class: <span style="font-size:36px; font-weight:bold; color:#d62728;">{result['class']}</span>
            </div>
        """, unsafe_allow_html=True)
        
    except requests.exceptions.RequestException as e:
        st.error(f'Error making prediction: {e}')
