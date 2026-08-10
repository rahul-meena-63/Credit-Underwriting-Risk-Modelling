import streamlit as st
import pandas as pd
import pickle
import xgboost # XGBoost import karna mat bhoolna

st.set_page_config(page_title="Bank Loan Priority Predictor", layout="wide")

# --- UI Setup for Banking Context ---
st.title("🏦 Bank Loan Priority Predictor")
st.write("Upload customer data to categorize them based on loan priority (analyzing credit score, salary, EMI records, education, etc.).")

# --- Model Loading (Exact same syntax style as your screenshot) ---
@st.cache_resource
def load_ml_model():
    filename = 'best_model.pkl'
    # Loading exactly how you saved it, using 'rb' (read-binary)
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model

best_model = load_ml_model()

# --- CSV Uploader ---
st.subheader("Upload Unseen Customer Data")
uploaded_file = st.file_uploader("Upload CSV file (Must contain 50 features)", type=["csv"])

if uploaded_file is not None:
    # CSV read karna
    customer_data = pd.read_csv(uploaded_file)
    st.write("Preview of Customer Data:", customer_data.head(3))
    
    # Predict Button
    if st.button("Categorize Customers (Predict Priority)"):
        try:
            # Model se prediction lena
            predictions = best_model.predict(customer_data)
            
            # Prediction ko nayi column banakar add karna
            customer_data['Loan_Priority_Category'] = predictions
            
            st.success("✅ Customers Categorized Successfully!")
            st.write("Final Results:")
            st.dataframe(customer_data.head(10)) # Top 10 rows show karega
            
            # User ko result download karne ka option dena
            csv = customer_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Categorized Data as CSV",
                data=csv,
                file_name='loan_priority_results.csv',
                mime='text/csv',
            )
        except Exception as e:
            st.error(f"Error aayi hai: {e}. Kripya check karein ki data me exactly 50 columns hain ya nahi.")
            