import streamlit as st

st.set_page_config(
    page_title="Carbon Footprint Calculator",
    page_icon="🌍"
)

st.title("🌱 Carbon Footprint Calculator")
st.write("Calculate your approximate carbon footprint and learn how to reduce it.")

st.header("🚗 Transportation")
km = st.slider("Kilometers travelled per week", 0, 1000, 50)
transport_emission = km * 0.21  # kg CO2 per km (average)

st.header("⚡ Electricity Usage")
electricity = st.number_input(
    "Monthly electricity consumption (kWh)",
    min_value=0
)
electricity_emission = electricity * 0.82  # kg CO2 per kWh (India avg)

st.header("🍽️ Lifestyle")
diet = st.selectbox(
    "Your diet type",
    ["Vegetarian", "Mixed", "Non-Vegetarian"]
)

if diet == "Vegetarian":
    diet_emission = 100
elif diet == "Mixed":
    diet_emission = 150
else:
    diet_emission = 200

total_emission = (
    transport_emission
    + electricity_emission
    + diet_emission
)

st.header("📊 Your Carbon Footprint Result")


st.markdown(
    f"""
    <h1 style="text-align:center; color:#2E7D32;">
        🌱 {total_emission:.2f} kg CO₂
    </h1>
    """,
    unsafe_allow_html=True
)

st.caption(
    "Your estimated monthly carbon footprint. ")
   
st.subtittle(
      "This is an approximate value based on transportation, electricity usage, and lifestyle."
)
