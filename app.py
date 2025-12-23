import streamlit as st
import csv
from datetime import datetime

# ------------------ APP HEADER ------------------
st.set_page_config(page_title="Winter Decision System", page_icon="❄️")

st.title("❄️ Winter Health Decision Support System")
st.markdown("This app analyzes your winter lifestyle and gives instant, practical advice.")

# ------------------ SIDEBAR ------------------
st.sidebar.title("ℹ️ About App")
st.sidebar.write("• Real-time decision system")
st.sidebar.write("• Rule-based logic with scoring")
st.sidebar.write("• Built using Python & Streamlit")
st.sidebar.write("• Developer: Manjesh Sahani")

# ------------------ USER INPUT FORM ------------------
st.markdown("## 🧊 Winter Lifestyle Input Form")

name = st.text_input("Enter your name")

temp = st.number_input(
    "Average room temperature (°C)",
    min_value=0,
    max_value=50,
    help="Enter approximate room temperature"
)

cold = st.selectbox("Do you feel cold often?", ["Yes", "No"])
water = st.selectbox("Do you drink warm water daily?", ["Yes", "No"])
heater = st.selectbox("Do you use a room heater?", ["Yes", "No"])
exercise = st.selectbox("Do you exercise during winter?", ["Yes", "No"])

# ------------------ DECISION BUTTON ------------------
if st.button("🔍 Get Winter Health Decision"):

    if name == "":
        st.warning("Please enter your name.")
    else:
        # ------------------ SCORING LOGIC ------------------
        score = 0

        if temp < 10:
            score += 3
        if cold == "Yes":
            score += 2
        if water == "No":
            score += 2
        if heater == "No":
            score += 1
        if exercise == "No":
            score += 1

        # ------------------ RISK LEVEL ------------------
        if score >= 6:
            risk = "HIGH RISK ❄️"
            color = "error"
        elif score >= 3:
            risk = "MEDIUM RISK ⚠️"
            color = "warning"
        else:
            risk = "LOW RISK ✅"
            color = "success"

        # ------------------ RESULT DISPLAY ------------------
        st.markdown("## 📊 Decision Result")

        if color == "error":
            st.error(f"{name}, your winter health status: {risk}")
        elif color == "warning":
            st.warning(f"{name}, your winter health status: {risk}")
        else:
            st.success(f"{name}, your winter health status: {risk}")

        st.markdown(f"**Risk Score:** {score}")

        # ------------------ ADVICE SECTION ------------------
        st.markdown("## 🩺 Personalized Advice")

        if temp < 10:
            st.write("• Keep your room warm and avoid cold air.")
        if cold == "Yes":
            st.write("• Wear thermal and warm clothes.")
        if water == "No":
            st.write("• Drink warm water regularly.")
        if heater == "No":
            st.write("• Use a room heater if possible.")
        if exercise == "No":
            st.write("• Do light exercise or stretching daily.")

        if score <= 2:
            st.write("• Great job! Maintain your healthy winter habits 👍")

        # ------------------ SAVE DATA ------------------
        try:
            with open("responses.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    datetime.now(),
                    name,
                    temp,
                    cold,
                    water,
                    heater,
                    exercise,
                    score,
                    risk
                ])
        except:
            st.info("Data storage not available in this environment.")

        st.markdown("---")
        st.markdown("✅ **Decision generated instantly using rule-based logic**")
