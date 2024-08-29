import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_fuel_consumption(distance_km, consumption_l_100km, fuel_price_l):
    fuel_burned_l = (distance_km / 100) * consumption_l_100km
    cost = fuel_burned_l * fuel_price_l
    return fuel_burned_l, cost

def calculate_travel_costs(distance_km, consumption_l_100km, fuel_price_l, other_costs_l):
    fuel_burned_l, fuel_costs = calculate_fuel_consumption(distance_km, consumption_l_100km, fuel_price_l)
    total_costs = fuel_costs + other_costs_l
    return fuel_burned_l, fuel_costs, total_costs

def get_language_text(language):
    if language == 'en':
        return {
            'language_label': "Choose language:",
            'distance_label': "Distance (km):",
            'consumption_label': "Fuel consumption (L/100 km):",
            'fuel_price_label': "Fuel price (per liter):",
            'other_costs_label': "Other costs:",
            'calculate_button': "Calculate",
            'fuel_consumption': "Fuel consumption: {0} liters",
            'fuel_costs': "Fuel costs: {0}",
            'total_costs': "Total costs: {0}",
            'info_text': (
                "Travel Cost Calculator\n\n"
                "This application calculates the cost of a trip based on the distance, fuel consumption, "
                "fuel price, and any additional costs.\n\n"
                "Author: micsno\n"
                "Email: micsno@pm.me\n"
                "Website: https://www.kouvala.tech"
            )
        }
    elif language == 'fi':
        return {
            'language_label': "Valitse kieli:",
            'distance_label': "Matka (km):",
            'consumption_label': "Polttoaineen kulutus (L/100 km):",
            'fuel_price_label': "Polttoaineen hinta (per litra):",
            'other_costs_label': "Muut kustannukset:",
            'calculate_button': "Laske",
            'fuel_consumption': "Polttoaineen kulutus: {0} litraa",
            'fuel_costs': "Polttoainekustannukset: {0}",
            'total_costs': "Yhteiskustannukset: {0}",
            'info_text': (
                "Matkakustannuslaskuri\n\n"
                "Tämä sovellus laskee matkan kustannukset matkan pituuden, polttoaineen kulutuksen, "
                "polttoaineen hinnan ja muiden kustannusten perusteella.\n\n"
                "Tekijä: micsno\n"
                "Sähköposti: micsno@pm.me\n"
                "Verkko-osoite: https://www.kouvala.tech"
            )
        }
    elif language == 'uk':
        return {
            'language_label': "Оберіть мову:",
            'distance_label': "Відстань (км):",
            'consumption_label': "Споживання пального (л/100 км):",
            'fuel_price_label': "Ціна пального (за літр):",
            'other_costs_label': "Інші витрати:",
            'calculate_button': "Розрахувати",
            'fuel_consumption': "Споживання пального: {0} літрів",
            'fuel_costs': "Вартість пального: {0}",
            'total_costs': "Загальні витрати: {0}",
            'info_text': (
                "Калькулятор витрат на подорож\n\n"
                "Ця програма розраховує витрати на подорож на основі відстані, споживання пального, "
                "ціни пального та будь-яких додаткових витрат.\n\n"
                "Автор: micsno\n"
                "Електронна пошта: micsno@pm.me\n"
                "Веб-сайт: https://www.kouvala.tech"
            )
        }
    elif language == 'fr':
        return {
            'language_label': "Choisissez la langue:",
            'distance_label': "Distance (km):",
            'consumption_label': "Consommation de carburant (L/100 km):",
            'fuel_price_label': "Prix du carburant (par litre):",
            'other_costs_label': "Autres coûts:",
            'calculate_button': "Calculer",
            'fuel_consumption': "Consommation de carburant: {0} litres",
            'fuel_costs': "Coût du carburant: {0}",
            'total_costs': "Coût total: {0}",
            'info_text': (
                "Calculateur de coût de voyage\n\n"
                "Cette application calcule le coût d'un voyage en fonction de la distance, de la consommation de "
                "carburant, du prix du carburant et de tout coût supplémentaire.\n\n"
                "Auteur: micsno\n"
                "Email: micsno@pm.me\n"
                "Site Web: https://www.kouvala.tech"
            )
        }
    elif language == 'de':
        return {
            'language_label': "Sprache auswählen:",
            'distance_label': "Entfernung (km):",
            'consumption_label': "Kraftstoffverbrauch (L/100 km):",
            'fuel_price_label': "Kraftstoffpreis (pro Liter):",
            'other_costs_label': "Sonstige Kosten:",
            'calculate_button': "Berechnen",
            'fuel_consumption': "Kraftstoffverbrauch: {0} Liter",
            'fuel_costs': "Kraftstoffkosten: {0}",
            'total_costs': "Gesamtkosten: {0}",
            'info_text': (
                "Reisekostenrechner\n\n"
                "Diese Anwendung berechnet die Kosten einer Reise basierend auf der Entfernung, dem "
                "Kraftstoffverbrauch, dem Kraftstoffpreis und zusätzlichen Kosten.\n\n"
                "Autor: micsno\n"
                "E-Mail: micsno@pm.me\n"
                "Website: https://www.kouvala.tech"
            )
        }
    else:
        return {}

def update_texts(language):
    texts = get_language_text(language)
    
    language_label.config(text=texts['language_label'])
    distance_label.config(text=texts['distance_label'])
    consumption_label.config(text=texts['consumption_label'])
    fuel_price_label.config(text=texts['fuel_price_label'])
    other_costs_label.config(text=texts['other_costs_label'])
    calculate_button.config(text=texts['calculate_button'])

def display_results():
    try:
        # Read user inputs
        distance_km = float(distance_entry.get())
        consumption_l_100km = float(consumption_entry.get())
        fuel_price_l = float(fuel_price_entry.get())
        other_costs_l = float(other_costs_entry.get())
        
        # Calculate costs
        fuel_burned, fuel_costs, total_costs = calculate_travel_costs(distance_km, consumption_l_100km, fuel_price_l, other_costs_l)
        
        # Get language texts
        language = language_var.get()
        texts = get_language_text(language)
        
        # Format results
        result_text = (texts['fuel_consumption'].format(round(fuel_burned, 2)) + "\n" +
                       texts['fuel_costs'].format(round(fuel_costs, 2)) + "\n" +
                       texts['total_costs'].format(round(total_costs, 2)))
        
        # Update result label
        result_label.config(text=result_text)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def show_info():
    language = language_var.get()
    texts = get_language_text(language)
    messagebox.showinfo("Information", texts['info_text'])

def close_app():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Travel Cost Calculator")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Close", command=close_app)

# Create help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Info", command=show_info)

# Language selection
language_var = tk.StringVar(value='en')
language_combo = ttk.Combobox(root, textvariable=language_var, values=['en', 'fi', 'uk', 'fr', 'de'])
language_combo.grid(row=1, column=0, padx=10, pady=5, sticky="w")
language_combo.set('en')
language_combo.bind("<<ComboboxSelected>>", lambda e: update_texts(language_var.get()))

# Labels and Inputs
language_label = tk.Label(root)
language_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

distance_label = tk.Label(root)
distance_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
distance_entry = tk.Entry(root)
distance_entry.grid(row=2, column=1, padx=10, pady=5)

consumption_label = tk.Label(root)
consumption_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
consumption_entry = tk.Entry(root)
consumption_entry.grid(row=3, column=1, padx=10, pady=5)

fuel_price_label = tk.Label(root)
fuel_price_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
fuel_price_entry = tk.Entry(root)
fuel_price_entry.grid(row=4, column=1, padx=10, pady=5)

other_costs_label = tk.Label(root)
other_costs_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
other_costs_entry = tk.Entry(root)
other_costs_entry.grid(row=5, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, command=display_results)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Results
result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Initialize texts
update_texts(language_var.get())

# Run the application
root.mainloop()
