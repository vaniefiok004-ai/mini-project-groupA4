# **Laptop Price Predictor Application Documentation**

## **1. Executive Summary**

The Laptop Price Predictor is a machine learning-powered web application that estimates laptop prices based on technical specifications. Developed by Computer Engineering Students Group A4, this tool leverages historical laptop pricing data to provide accurate price estimates in Euros, with additional USD conversion.

**Application URL:** https://mini-project-groupa4.streamlit.app/

---

## **2. Project Overview**

### **2.1 Objectives**
- Develop a machine learning model to predict laptop prices based on specifications
- Create an intuitive web interface for price estimation
- Deploy the application for public accessibility
- Provide educational insights into laptop pricing factors

### **2.2 Technical Architecture**
- **Frontend:** Streamlit web framework
- **Backend:** Python with machine learning libraries
- **Model:** Trained regression model with preprocessing pipeline
- **Deployment:** Streamlit Cloud platform

---

## **3. Dataset Description**

### **3.1 Data Source**
The application uses the laptop_price.csv dataset containing comprehensive laptop specifications and pricing information.

### **3.2 Dataset Features**
The dataset includes the following features:

| Feature | Description | Type |
|---------|-------------|------|
| laptop_ID | Unique identifier | Categorical |
| Company | Manufacturer (Acer, Apple, Asus, Dell, HP, Lenovo, MSI, Samsung, Toshiba) | Categorical |
| Product | Product name | Text |
| TypeName | Laptop category (Notebook, Ultrabook, Gaming, Workstation, 2 in 1 Convertible) | Categorical |
| Inches | Screen size in inches | Numerical |
| ScreenResolution | Display resolution | Text |
| Cpu | Processor specifications | Text |
| Ram | Memory size in GB | Numerical |
| Memory | Storage details | Text |
| Gpu | Graphics card information | Text |
| OpSys | Operating system | Categorical |
| Weight | Device weight in kg | Numerical |
| Price_euros | Target variable - price in Euros | Numerical |

---

## **4. Data Preprocessing & Feature Engineering**

### **4.1 Data Cleaning Process**
- Handled missing values and inconsistent data formats
- Standardized categorical variables
- Extracted numerical values from text fields
- Removed irrelevant or duplicate entries

### **4.2 Feature Engineering**
The preprocessing pipeline includes:

1. **Screen Resolution Processing:**
   - Extracted X_res (horizontal resolution)
   - Extracted Y_res (vertical resolution)  
   - Calculated Pixels (total pixel count)

2. **Storage Processing:**
   - Extracted Storage_Size_GB from Memory field
   - Identified Storage_Type (SSD, HDD, Flash, Hybrid)

3. **Binary Features:**
   - Touchscreen (0/1)
   - IPS_Panel (0/1)

4. **Categorical Encoding:**
   - One-hot encoding for Company, TypeName, and Storage_Type
   - Feature scaling using StandardScaler

---

## **5. Model Development**

### **5.1 Model Architecture**
The application uses a machine learning regression model trained on the preprocessed laptop dataset. The model pipeline includes:

1. **Feature Selection:** Identified most relevant features for price prediction
2. **Scaling:** StandardScaler normalization for numerical features
3. **Training:** Regression algorithm optimized for price prediction accuracy

### **5.2 Model Files**
Three key model files are saved and loaded:
- laptop_price_model.joblib - Trained regression model
- scaler.joblib - Feature scaling transformer
- feature_names.joblib - Column names for input features

---

## **6. Web Application Features**

### **6.1 User Interface Components**

#### **Main Input Section:**
- **Basic Specifications (Left Column):**
  - Screen Size: 10.0-20.0 inches
  - RAM: 4GB to 64GB options
  - Weight: 0.5-5.0 kg
  - Storage Size: 128GB to 2048GB

- **Advanced Features (Right Column):**
  - Touchscreen: Yes/No
  - IPS Panel: Yes/No
  - Company: 10 major manufacturers
  - Laptop Type: 5 categories
  - Storage Type: 4 options

#### **Sidebar Information:**
- About This Tool description
- Last Updated timestamp

#### **Prediction Output:**
- Price in Euros (€)
- USD conversion (approximate)
- Input summary in expandable section
- Error handling with user-friendly messages

### **6.2 Key Functionalities**

1. **Real-time Prediction:** Instant price estimation upon clicking "Predict Price 💰"
2. **Input Validation:** Ensures all inputs are within valid ranges
3. **Error Handling:** Graceful error management with informative messages
4. **Responsive Design:** Works across different screen sizes
5. **Currency Conversion:** Automatic EUR to USD conversion

---

## **7. System Requirements**

### **7.1 User Requirements**
- **Web Browser:** Modern browser (Chrome, Firefox, Safari, Edge)
- **Internet Connection:** Required for accessing the deployed application
- **JavaScript:** Enabled for full functionality

### **7.2 Development Requirements**
```python
# Core Dependencies
streamlit>=1.0.0
pandas>=1.3.0
numpy>=1.21.0
joblib>=1.0.0
scikit-learn>=1.0.0

# Additional requirements
python>=3.8
```

### **7.3 Deployment Requirements**
- **Platform:** Streamlit Cloud
- **Memory:** Sufficient for model loading and inference
- **Storage:** Space for model files and application code

---

## **8. Application Usage Guide**

### **8.1 Accessing the Application**
1. Navigate to: https://mini-project-groupa4.streamlit.app/
2. Wait for the application to load
3. Model files will be automatically loaded on first access

### **8.2 Making Predictions**

#### **Step 1: Enter Basic Specifications**
- Set screen size using the number input
- Select RAM from dropdown menu
- Input weight value
- Specify storage size

#### **Step 2: Configure Advanced Features**
- Choose touchscreen availability
- Select IPS panel option
- Pick manufacturer from company list
- Select laptop type category
- Choose storage technology

#### **Step 3: Get Prediction**
- Click "Predict Price 💰" button
- View estimated price in Euros
- Check USD conversion
- Expand input summary if needed

### **8.3 Understanding Results**
- **Primary Output:** Price in Euros (€)
- **Secondary Output:** Approximate USD equivalent
- **Input Summary:** Review all entered specifications
- **Disclaimer:** Important limitations and usage notes

---

## **9. Model Performance & Validation**

### **9.1 Training Process**
The model was trained using the laptop_data_clean.ipynb notebook with the following process:
1. Data exploration and analysis
2. Feature engineering and preprocessing
3. Model training and hyperparameter tuning
4. Performance evaluation and validation
5. Model serialization for deployment

### **9.2 Performance Metrics**
Based on the training process, the model demonstrates:
- Optimized performance for price estimation
- Robust handling of various laptop configurations
- Consistent predictions across different price ranges

---

## **10. Limitations & Disclaimers**

### **10.1 Model Limitations**
- **Data Currency:** Based on historical pricing data
- **Market Dynamics:** May not reflect current market conditions
- **Regional Variations:** Prices may vary by geographic location
- **Special Cases:** Limited handling of custom/special edition models

### **10.2 Usage Disclaimers**
- Educational and informational purposes only
- Not professional purchasing advice
- Verify prices through official retailers
- Results are estimates, not guaranteed prices

---

## **11. Technical Implementation Details**

### **11.1 Application Architecture**
```python
# Core Application Structure
streamlit_app.py          # Main application file
├── Model Loading         # @st.cache_resource decorator
├── Sidebar Creation      # Information panel
├── Input Interface       # User input components
├── Prediction Logic      # Model inference
└── Results Display       # Output formatting
```

### **11.2 Key Code Components**

#### **Model Loading:**
```python
@st.cache_resource
def load_model():
    model = joblib.load('laptop_price_model.joblib')
    scaler = joblib.load('scaler.joblib')
    feature_names = joblib.load('feature_names.joblib')
    return model, scaler, feature_names
```

#### **Feature Processing:**
- One-hot encoding for categorical variables
- Feature scaling using saved scaler
- Input validation and error handling

#### **Prediction Pipeline:**
- DataFrame creation with proper feature names
- Feature scaling transformation
- Model inference and result formatting

---

## **12. Deployment & Maintenance**

### **12.1 Deployment Platform**
- **Service:** Streamlit Cloud
- **Repository:** GitHub integration
- **URL:** https://mini-project-groupa4.streamlit.app/
- **Automatic Updates:** Synced with repository changes

### **12.2 Maintenance Considerations**
- **Model Updates:** Periodic retraining with new data
- **Dependency Management:** Keep libraries updated
- **Performance Monitoring:** Track application usage and errors
- **User Feedback:** Collect and incorporate user suggestions

---

## **13. Future Enhancements**

### **13.1 Potential Improvements**
- **Enhanced Features:** Additional laptop specifications
- **Model Accuracy:** Advanced algorithms and more data
- **User Experience:** Improved interface and visualizations
- **Currency Support:** Multiple currency options
- **Comparison Tools:** Side-by-side laptop comparisons

### **13.2 Scalability Options**
- **Database Integration:** Dynamic data updates
- **API Development:** Programmatic access
- **Mobile Optimization:** Native mobile experience
- **Multi-language Support:** International accessibility

---

## **14. Repository Information**

### **14.1 Project Structure**
```
mini-project-groupA4/
├── streamlit_app.py           # Main application
├── laptop_data_clean.ipynb    # Model training notebook
├── laptop_price.csv          # Training dataset
├── laptop_price_model.joblib # Trained model
├── scaler.joblib             # Feature scaler
├── feature_names.joblib      # Feature names
└── README.md                 # Project documentation
```

### **14.2 Version Control**
- **Repository:** vaniefiok004-ai/mini-project-groupA4
- **Platform:** GitHub
- **Branch:** main
- **Collaboration:** Group A4 team development

---

## **15. Conclusion**

The Laptop Price Predictor successfully demonstrates the application of machine learning in real-world pricing estimation. The application provides an intuitive interface for users to estimate laptop prices based on specifications, while maintaining transparency about its limitations and appropriate usage contexts.

The project showcases the complete machine learning pipeline from data preprocessing through model deployment, serving as an educational tool and practical demonstration of predictive analytics in consumer electronics pricing.

---

**Document Version:** 1.0  
**Last Updated:** September 15, 2025  
**Prepared by:** Computer Engineering Students Group A4  
**Application URL:** https://mini-project-groupa4.streamlit.app/

---