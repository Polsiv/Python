import streamlit as st

from baseCalculator import decimal_to_base, base_to_decimal

def main():
    st.title("Calculator App")
    
    # Sidebar options
    calculator_type = st.sidebar.radio("Calculator Type", ["Base Calculator", "Basic Calculator", "App Calculator"])
    
    if calculator_type == "Base Calculator":
        base_calculator()
    elif calculator_type == "Basic Calculator":
        basic_calculator()
    elif calculator_type == "App Calculator":
        app_calculator()

def base_calculator():
    st.subheader("Base Calculator")

    number_to_convert = st.text_input("Enter the number to convert:")
    input_base = st.number_input("Enter the input base (2-36):", min_value=2, max_value=36, step=1)
    convert_base = st.number_input("Enter the base to convert (2-36):", min_value=2, max_value=36, step=1)

    if st.button("Convert"):
        if number_to_convert and input_base and convert_base:
            try:
                converted_number = decimal_to_base(base_to_decimal(number_to_convert.upper(), input_base), convert_base)
                st.success(f"The converted number is: {converted_number}")
            except ValueError:
                st.error("Invalid input. Please check your input and try again.")
        else:
            st.warning("Please fill in all the required fields.")

def basic_calculator():

    st.subheader("Basic Calculator")
    
    input_base = st.number_input("Enter the input base (2-36):", min_value=2, max_value=36, step=1)
    num1 = base_to_decimal(st.text_input("Enter the number to convert:").upper(), input_base)
    num2 = base_to_decimal(st.text_input("Enter the other number to convert:").upper(), input_base)

    operation = st.selectbox("Select operation", ["+", "-", "*", "/"])

    if st.button("Calculate"):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                return
            result = num1 / num2

        st.success(f"Result: {result}")

def app_calculator():
    st.subheader("App Calculator")

    number_to_convert = st.number_input("Enter the number to convert:")
    st.success(f"Hex: {decimal_to_base(number_to_convert, 16)}")
    st.success(f"Octal: {decimal_to_base(number_to_convert, 8)}")
    st.success(f"Binary: {decimal_to_base(number_to_convert, 2)}")

    st.image("caught-in.gif")

main()
