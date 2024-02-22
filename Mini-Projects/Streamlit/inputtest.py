import streamlit as st

# Define the Streamlit app layout
st.title("User Input Example")

# Text input widget
user_input = st.text_input("Enter your name", "Your name")

# Number input widget
user_age = st.number_input("Enter your age", min_value=0, max_value=150, value=30)

# Selectbox widget
selected_option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

# Button to trigger an action
if st.button("Submit"):
    st.write(f"Name: {user_input}")
    st.write(f"Age: {user_age}")
    st.write(f"Selected Option: {selected_option}")
