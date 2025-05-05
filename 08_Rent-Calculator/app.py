import streamlit as st
# Inpute we need from user
# Total Rent
# Total food orderd for snacking
# electricity unit spend
# electricity per unit
# Person living in the room/flat

# Output 
# Total amount you've to pay is

st.set_page_config(page_title="Rent Calculator", page_icon="📇", layout="centered")
st.header("🏠 Rent & Utility Calculator📊")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #b6fbff, #6dd5ed);
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="
        background: linear-gradient(to right, #e0f7fa, #0096c7);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    ">
        <h4 style="color: #333; margin: 0;">This calculator helps you fairly split rent, food, and electricity bills among roommates.</h4>
    </div>
    """,
    unsafe_allow_html=True
)


rent = st.number_input(" 🏦 **Enter your Flat/Hostel rent amount:**", min_value=0.0)
food = st.number_input("🍽️  **Enter the total food cost:**", min_value=0.0)
electricity_spend = st.number_input("⚡  **Enter the total of electricity unit used:**", min_value=0.0)
charge_per_unit = st.number_input("💡  **Enter the charge per unit:**", min_value=0.0)
person = st.number_input("🧍‍♂️   **Enter the number of persons living in the room:**", min_value=1)

if st.button("Calculate"):
    if rent == 0.0:
        st.warning("🏦 Rent amount is required!")
    elif electricity_spend == 0.0:
        st.warning("⚡ Electricity usage is required!")
    elif charge_per_unit == 0.0:
        st.warning("💡 Charge per unit is required!")
    elif person == 1:
        st.info("Only one person entered. You'll pay the full amount.")
    else:
        total_bill = electricity_spend * charge_per_unit
        output = (rent + food + total_bill) / person
        st.success(f"Each person will pay = {round(output,2)} ")
    