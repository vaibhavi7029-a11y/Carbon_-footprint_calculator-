import matplotlib.pyplot as plt

EMISSION_FACTORS = {
    "car": 0.21,
    "bike": 0.05,
    "bus": 0.10,
    "electricity": 0.82,
    "lpg": 2.98
}

print("---- Carbon Footprint Calculator ----")

vehicle = input("Enter transport type (car/bike/bus): ").lower()
distance = float(input("Enter distance travelled (km per day): "))

electricity_units = float(input("Enter electricity usage (units per month): "))
lpg_used = float(input("Enter LPG usage (kg per month): "))

# Monthly transport (30 days)
transport_emission = distance * 30 * EMISSION_FACTORS.get(vehicle, 0)
electricity_emission = electricity_units * EMISSION_FACTORS["electricity"]
lpg_emission = lpg_used * EMISSION_FACTORS["lpg"]

total_emission = transport_emission + electricity_emission + lpg_emission

print("\nTotal Carbon Footprint:", round(total_emission, 2), "kg CO2/month")

# Suggestions
if total_emission > 300:
    print("Use public transport and reduce electricity usage")
else:
    print("Great job! Keep following sustainable habits")


