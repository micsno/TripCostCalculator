def calculate_fuel_consumption(distance_km, consumption_l_100km, fuel_price_eur_l):
    fuel_burned_l = (distance_km / 100) * consumption_l_100km
    cost_eur = fuel_burned_l * fuel_price_eur_l
    return fuel_burned_l, cost_eur

def calculate_travel_costs(distance_km, consumption_l_100km, fuel_price_eur_l, other_costs_eur):
    fuel_burned_l, fuel_costs = calculate_fuel_consumption(distance_km, consumption_l_100km, fuel_price_eur_l)
    total_costs = fuel_costs + other_costs_eur
    return fuel_burned_l, fuel_costs, total_costs

while True:
    distance_km = float(input("Enter the distance of the trip in kilometers: "))
    consumption_l_100km = float(input("Enter the fuel consumption of the car in liters per 100 km: "))
    fuel_price_eur_l = float(input("Enter the price of fuel in euros per liter: "))
    other_costs_eur = float(input("Enter other travel costs in euros: "))

    fuel_burned, fuel_costs, total_costs = calculate_travel_costs(distance_km, consumption_l_100km, fuel_price_eur_l, other_costs_eur)

    print("\nFuel consumption:", round(fuel_burned, 2), "liters")
    print("Fuel costs:", round(fuel_costs, 2), "euros")
    print("Total costs:", round(total_costs, 2), "euros")

    choice = input("Do you want to calculate again? (yes/no): ")
    if choice.lower() != "yes":
        break
