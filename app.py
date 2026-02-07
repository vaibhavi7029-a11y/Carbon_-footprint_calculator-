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
    "Your estimated monthly carbon footprint. "
    "This is an approximate value based on transportation, electricity usage, and lifestyle."
)

# CSS styling
st.markdown("""
<style>
.result-box {
    text-align: center;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    font-size: 18px;
}
.high {
    background-color: #FFE6E6;
    color: #B00020;
}
.low {
    background-color: #E6F4EA;
    color: #1B5E20;
}
</style>
""", unsafe_allow_html=True)

# Logic
if total_emission > 300:
    st.markdown(f"""
    <div class="result-box high">
        🚨 <b>High Carbon Footprint!</b><br><br>
        🌍 Your emission is <b>{total_emission:.2f} kg CO₂/month</b><br>
        🚍 Use public transport<br>
        💡 Save electricity<br>
        🌱 Choose sustainable lifestyle
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="result-box low">
        ✅ <b>Great Job!</b><br><br>
        🌿 Your emission is <b>{total_emission:.2f} kg CO₂/month</b><br>
        🌱 You are living sustainably<br>
        👏 Keep it up!
    </div>
    """, unsafe_allow_html=True)

