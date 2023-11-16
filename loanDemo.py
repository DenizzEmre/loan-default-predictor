import streamlit as st
import pickle
import pandas as pd

# Load the logistic regression model
with open("logistic_regression_app.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app layout
def main():
    st.title("Loan Default Prediction")

    # User inputs for the original features
    credit_type = st.selectbox('Credit Type', options=['EQUI', 'EXP', 'CIB', 'CRIF', 'Other'])
    lump_sum_payment = st.selectbox('Lump Sum Payment', options=['LPSM', 'Not LPSM'])
    security_type = st.selectbox('Security Type', options=['Direct', 'Indirect', 'Other'])
    ltv = st.number_input('Loan to Value Ratio (LTV)', min_value=0.0, max_value=100.0, format='%.2f')
    neg_ammortization = st.selectbox('Negative Ammortization', options=['Yes', 'No'])

    # Function to prepare the inputs
    def prepare_inputs(credit_type, lump_sum_payment, security_type, ltv, neg_ammortization):
        # Create DataFrame with raw input data
        input_data = pd.DataFrame({
            'credit_type': [credit_type],
            'lump_sum_payment': [lump_sum_payment],
            'security_type': [security_type],
            'ltv': [ltv],
            'neg_ammortization': [neg_ammortization]
        })

        return input_data

    # Prediction button
    if st.button("Predict Default"):
        input_data = prepare_inputs(credit_type, lump_sum_payment, security_type, ltv, neg_ammortization)
        prediction = model.predict(input_data)[0]
        prediction_text = 'Likely to Default' if prediction == 1 else 'Unlikely to Default'
        st.success(f"Prediction: {prediction_text}")

if __name__ == "__main__":
    main()
