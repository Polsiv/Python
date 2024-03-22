import streamlit as st

def abc(base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet[:base]

def TenToN(number, base):
  intPart = ""
  fracPart = ""
  coc = 1
  decimal = 0

  numberInt = int(number)
  numberFrac = float(number - numberInt)
  while coc != 0:
    pos = int(numberInt % base)
    intPart += abc(base)[pos]
    coc = numberInt // base
    numberInt = coc
  intPart = intPart[::-1]

  while decimal != 4:
    actNum = numberFrac * base
    fracPart += str(abc(base)[int(actNum)])
    numberFrac = actNum - int(actNum)
    decimal += 1
  return intPart + '.' + fracPart

def NtoTen(number, base):
  digitNumber = number.split('.')
  intPart = digitNumber[0]
  fracPart = digitNumber[1] if len(digitNumber) > 1 else "0"
  newNumber = intPart + fracPart

  charToValue = {}
  for i, char in enumerate(abc(base)):
    charToValue[char] = i

  counter = len(intPart) - 1
  convertedNum = 0
  for i in newNumber:
    convertedNum += charToValue[i] * (base**counter)
    counter -= 1
  return round(convertedNum, 4)

def OBtoFB(number, originBase, finalBase):
  return TenToN(NtoTen(number, originBase), finalBase)

def main():
    st.title("Calculator App")

    calculator_type = st.sidebar.radio("Calculator Type", ["Base Calculator", "Basic Calculator","Important Bases"])

    if calculator_type == "Base Calculator":
        base_calculator()
    elif calculator_type == "Basic Calculator":
        basic_calculator()
    elif calculator_type=="Important Bases":
        important_calculator()

def base_calculator():
    st.subheader("Base Calculator")

    number_to_convert = st.text_input("Enter the number to convert:")
    input_base = st.number_input("Enter the input base (2-36):", min_value=2, max_value=36, step=1)
    convert_base = st.number_input("Enter the base to convert (2-36):", min_value=2, max_value=36, step=1)

    if st.button("Convert"):
        if number_to_convert and input_base and convert_base:
            try:
                converted_number = TenToN(NtoTen(number_to_convert.upper(), input_base), convert_base)
                st.success(f"The converted number is: {converted_number}")
            except ValueError:
                st.error("Invalid input. Please check your input and try again.")
        else:
            st.warning("Please fill in all the required fields.")

def basic_calculator():
    st.subheader("Basic Calculator")

    base= st.number_input("Enter the input base (2-36):", min_value=2, max_value=36, step=1)
    n1=st.text_input("Enter the first number:")
    n2=st.text_input("Enter the second number:")
    num1 = NtoTen(n1,base)
    num2 = NtoTen(n2,base)

    operation = st.selectbox("Select operation", ["+", "-", "*", "/", ""])

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

        st.success(f"{n1} {operation} {n2} is: {TenToN(result,base)} in base {base}")
        st.success(f"{num1} {operation} {num2} is: {result} in Decimal")

def important_calculator():
    st.subheader("Important Bases Calculator")
    number_to_convert = st.number_input("Enter the number to convert:")
    if st.button("Convert"):
        if number_to_convert:
            try:
                binary_result = TenToN(number_to_convert, 2)
                octal_result = TenToN(number_to_convert, 8)
                hexadecimal_result = TenToN(number_to_convert, 16)

                st.write(f"Binario: {binary_result}")
                st.write(f"Octal: {octal_result}")
                st.write(f"Hexadecimal: {hexadecimal_result}")
            except ValueError:
                st.error("Invalid input. Please check your input and try again.")
        else:
            st.warning("Please fill in all the required fields.")


main()