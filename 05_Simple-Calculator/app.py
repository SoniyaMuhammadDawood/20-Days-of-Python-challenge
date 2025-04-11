import streamlit as st

st.set_page_config(page_title="Simple-calculator", page_icon="🔢", layout="centered")
st.title("**Simple Calculator🔢 ➗✖️➕➖**")
st.write("**Enter two numbers and choose operation**")


st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(to right, #effbf0, #eeaecd);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("**Enter First Number**", value=0.0)
    with col2:
        num2 = st.number_input("**Enter Second Number**", value=0.0)

    operation = st.selectbox("**Select operation**", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

    if st.button("**Calculate**"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"                # show this symbol on UI
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (*)":
                result = num1 * num2
                symbol = "*"
            else:
                if num2 == 0:
                    return st.error("Error: Division by zero!")
                result = num1 / num2
                symbol = "/"
            st.success(f"{num1} {symbol} {num2} = {result}")

        except Exception as e:
            st.error(f"An error occured: {str(e)}")

# ye line hm Python Internal interperinor ko btane ke leye likhte hen ke konsa fun ose hme app start hote he sbse pehle run karna hai

if __name__ == "__main__":
    main()