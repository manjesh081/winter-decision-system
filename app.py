import streamlit as st

st.title("Winter Health Decision System")

name = st.text_input("Enter your name")
temp = st.number_input("Room temperature (°C)", min_value=0, max_value=50)
cold = st.selectbox("Do you feel cold often?", ["Yes", "No"])
water = st.selectbox("Do you drink warm water daily?", ["Yes", "No"])

if st.button("Get Decision"):
    if temp < 10 and cold == "Yes":
        st.write(f"{name}, high cold risk ❄️ Use warm clothes")
    elif water == "No":
        st.write(f"{name}, drink warm water daily ☕")
    else:
        st.write(f"{name}, you are healthy ✅")
