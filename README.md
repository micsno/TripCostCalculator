# Trip Cost Calculator

This is a Python code that calculates the cost of a trip based on the distance traveled, fuel efficiency of the vehicle, and the current price of fuel. 

## Installation

1. Clone the repository: `git clone https://github.com/micsno/TripCostCalculator.git`
2. Navigate to the project directory: `cd TripCostCalculator`

## Usage

1. Open the `TripCostCalculator.py` file in your preferred Python IDE.
2. Modify the values of `distance`, `fuel_efficiency`, and `fuel_price` variables according to your trip details.
3. Run the script.
4. The program will display the total cost of the trip.

## Example

```python
distance = 200  # in kilometers
fuel_efficiency = 10  # in kilometers per liter
fuel_price = 1.5  # in dollars per liter

total_cost = distance / fuel_efficiency * fuel_price
print(f"The total cost of the trip is ${total_cost:.2f}")
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
