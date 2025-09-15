import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# Load the saved model, scaler, and feature names
@st.cache_resource
def load_model():
    model = joblib.load('laptop_price_model.joblib')
    scaler = joblib.load('scaler.joblib')
    feature_names = joblib.load('feature_names.joblib')
    return model, scaler, feature_names

# Load model components
model, scaler, feature_names = load_model()

# Sidebar for additional info
with st.sidebar:
    st.markdown("### 📊 About This Tool")
    st.write("This AI-powered tool predicts laptop prices based on technical specifications using machine learning.")
    
    st.markdown("---")
    st.markdown(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}")

# Streamlit app
st.title('🖥️ Laptop Price Predictor')
st.write('Enter laptop specifications to predict the price in Euros')

# Create input fields
col1, col2 = st.columns(2)

with col1:
    st.subheader('Basic Specifications')
    inches = st.number_input('Screen Size (Inches)', min_value=10.0, max_value=20.0, value=15.6, step=0.1)
    ram = st.selectbox('RAM (GB)', [4, 6, 8, 12, 16, 32, 64])
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=2.0, step=0.1)
    storage_size = st.number_input('Storage Size (GB)', min_value=128, max_value=2048, value=256, step=128)

with col2:
    st.subheader('Advanced Features')
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips_panel = st.selectbox('IPS Panel', ['No', 'Yes'])
    
    # Company selection
    companies = ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Samsung', 'Toshiba', 'Other']
    company = st.selectbox('Company', companies)
    
    # Laptop type
    type_options = ['Notebook', 'Ultrabook', 'Gaming', 'Workstation', '2 in 1 Convertible']
    laptop_type = st.selectbox('Laptop Type', type_options)
    
    # Storage type
    storage_type = st.selectbox('Storage Type', ['SSD', 'HDD', 'Flash', 'Hybrid'])

# Calculate derived features
pixels = 1920 * 1080  # Default resolution, you can make this more sophisticated
x_res = 1920
y_res = 1080

# Create prediction button
if st.button('Predict Price 💰'):
    try:
        # Create input dataframe
        input_data = pd.DataFrame(columns=feature_names)
        input_data.loc[0] = 0  # Initialize with zeros
        
        # Set basic features
        input_data.loc[0, 'Inches'] = inches
        input_data.loc[0, 'Ram'] = ram
        input_data.loc[0, 'Weight'] = weight
        input_data.loc[0, 'Storage_Size_GB'] = storage_size
        input_data.loc[0, 'Touchscreen'] = 1 if touchscreen == 'Yes' else 0
        input_data.loc[0, 'IPS_Panel'] = 1 if ips_panel == 'Yes' else 0
        input_data.loc[0, 'X_res'] = x_res
        input_data.loc[0, 'Y_res'] = y_res
        input_data.loc[0, 'Pixels'] = pixels
        
        # Set company (one-hot encoded)
        company_col = f'Company_{company}'
        if company_col in input_data.columns:
            input_data.loc[0, company_col] = 1
        
        # Set laptop type (one-hot encoded)
        type_col = f'TypeName_{laptop_type}'
        if type_col in input_data.columns:
            input_data.loc[0, type_col] = 1
        
        # Set storage type (one-hot encoded)
        storage_col = f'Storage_Type_{storage_type}'
        if storage_col in input_data.columns:
            input_data.loc[0, storage_col] = 1
        
        # Scale the features
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Display results
        st.success(f'Predicted Laptop Price: **€{prediction:.2f}**')
        
        # Additional insights
        st.info(f'This translates to approximately **${prediction * 1.1:.2f} USD**')
        
        # Display input summary
        with st.expander('Input Summary'):
            st.write(f'• Screen Size: {inches}" inches')
            st.write(f'• RAM: {ram} GB')
            st.write(f'• Weight: {weight} kg')
            st.write(f'• Storage: {storage_size} GB {storage_type}')
            st.write(f'• Company: {company}')
            st.write(f'• Type: {laptop_type}')
            st.write(f'• Touchscreen: {touchscreen}')
            st.write(f'• IPS Panel: {ips_panel}')
            
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        st.write("Please check that all model files are properly loaded and the input features match the training data.")

# Add footer with model info
st.markdown('---')
st.write('**Model Information:**')
st.write('This model was trained on laptop pricing data to provide accurate price estimates.')

# Detailed disclaimer with orange warning
st.warning("""
** ⚠️ Disclaimer: ** 
This price predictor uses past laptop data to estimate prices. Results may not match current market trends or actual retail costs.
Limitations:
It may not reflect new models, brand pricing, special editions, refurbished items, or warranty differences.
Note:
This is for learning only—not professional buying advice.
Please verify prices through official retailers before making purchases.
""")