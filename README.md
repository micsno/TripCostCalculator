# Trip Cost Calculator

This is a Python code that calculates the cost of a trip based on the distance traveled, fuel efficiency of the vehicle, and the current price of fuel. 

## Installation

1. Clone the repository: `git clone https://github.com/micsno/TripCostCalculator.git`
2. Navigate to the project directory: `cd TripCostCalculator`

## Usage

**Run the application:**

- From Python IDE: Open the TripCostCalculator.py file in your preferred Python IDE and run the script.
- As a standalone executable: If you created an executable, simply double-click TripCostCalculator.exe to run the application.

**Interact with the application:**

- Select your preferred language from the dropdown.
- Enter the distance traveled, fuel consumption, fuel price, and additional costs.
- Choose the type of fuel from the dropdown.
- The application will automatically update the total trip cost, fuel consumption, fuel costs, and CO2 emissions as you enter or modify the values.

## Example

Here is how you can use the Python script for calculating costs (for running it in a Python environment, not applicable for the standalone executable):

```python
distance = 200  # in kilometers
fuel_efficiency = 10  # in liters per 100 kilometers
fuel_price = 1.5  # in dollars per liter
additional_costs = 20  # in dollars
fuel_type = 'Petrol'  # or 'Diesel'

total_cost = distance / 100 * fuel_efficiency * fuel_price + additional_costs
print(f"The total cost of the trip is ${total_cost:.2f}")

```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Author
- Author: micsno
- Email: micsno@pm.me
- Website: https://www.kouvala.tech