import streamlit as st
import pandas as pd
import pickle
import xgboost 

st.set_page_config(page_title="Credit Underwriting & Risk Modelling Engine", layout="wide")
#main headers for the app
st.title("🏦 Credit Underwriting & Risk Modelling Engine")
st.write("Upload customer data to evaluate credit risk and generate the Approved_flag.")

# load the saved pickle file
@st.cache_resource
def load_ml_model():
    filename = 'best_model.pkl'
    return pickle.load(open(filename, 'rb'))

best_model = load_ml_model()

st.subheader("Upload Unseen Customer Data")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    customer_data = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:", customer_data.head(3))
    
    if st.button("Predict Credit Risk"):
        try:
            predictions = best_model.predict(customer_data)
            customer_data['Approved_flag'] = predictions
            
            st.success("✅ Credit Risk Evaluated Successfully!")
            st.write("Final Results:")
            st.dataframe(customer_data) 
            
        
            csv = customer_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name='credit_risk_results.csv',
                mime='text/csv',
            )
        except Exception as e:
            # error handling just in case the format is wrong
            st.error(f"Error: {e}. uploaded format is wrong.")
   
     
