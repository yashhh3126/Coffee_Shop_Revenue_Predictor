import streamlit as st
import pandas as pd
import pickle

# Load the trained model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# App title and description
st.title("Coffee Shop Daily Revenue Predictor")
st.markdown("""
This app predicts the daily revenue of a coffee shop based on various factors.
Adjust the parameters in the sidebar to see how they affect the predicted revenue.
""")

# Sidebar with input features
st.sidebar.header("Input Features")

customers_per_day = st.sidebar.slider(
    "Number of Customers Per Day",
    min_value=0,
    max_value=1000,
    value=200,
    help="Average number of customers visiting the coffee shop per day"
)

avg_order_value = st.sidebar.slider(
    "Average Order Value ($)",
    min_value=0.0,
    max_value=20.0,
    value=5.0,
    step=0.1,
    help="Average amount spent by each customer per visit"
)

operating_hours = st.sidebar.slider(
    "Operating Hours Per Day",
    min_value=0,
    max_value=24,
    value=10,
    help="Number of hours the coffee shop is open each day"
)

num_employees = st.sidebar.slider(
    "Number of Employees",
    min_value=1,
    max_value=50,
    value=5,
    help="Number of employees working at the coffee shop"
)

marketing_spend = st.sidebar.slider(
    "Marketing Spend Per Day ($)",
    min_value=0.0,
    max_value=1000.0,
    value=100.0,
    step=1.0,
    help="Amount spent on marketing per day"
)

foot_traffic = st.sidebar.slider(
    "Location Foot Traffic",
    min_value=0,
    max_value=2000,
    value=500,
    help="Estimated foot traffic at the location per day"
)

# Prepare the input data
input_data = pd.DataFrame({
    'Number_of_Customers_Per_Day': [customers_per_day],
    'Average_Order_Value': [avg_order_value],
    'Operating_Hours_Per_Day': [operating_hours],
    'Number_of_Employees': [num_employees],
    'Marketing_Spend_Per_Day': [marketing_spend],
    'Location_Foot_Traffic': [foot_traffic]
})

# Load the model and make prediction
try:
    model = load_model()
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.header("Prediction Result")

    st.success(f"Estimated Daily Revenue: ${prediction[0]:,.2f}")
    
    # Additional information
    st.info("""
    *Note:* This prediction is based on a machine learning model trained on historical coffee shop data.
    Actual revenue may vary based on factors not included in this model.
    """)
    
    # Visualization
    st.header("Revenue Insights")
    st.write(f"With {customers_per_day} customers per day and an average order value of ${avg_order_value}, "
             f"you can expect a daily revenue of ${prediction[0]:,.2f}.")
    
except Exception as e:
    st.error(f"Error making prediction: {str(e)}")

# Sidebar with additional information
st.sidebar.header("About This App")
st.sidebar.write("""
This application uses a Random Forest Regressor model to predict coffee shop daily revenue.

The model was trained on a dataset containing:
- Number of customers per day
- Average order value
- Operating hours per day
- Number of employees
- Marketing spend per day
- Location foot traffic

The model achieved an R² score of approximately 0.95 on test data.
""")