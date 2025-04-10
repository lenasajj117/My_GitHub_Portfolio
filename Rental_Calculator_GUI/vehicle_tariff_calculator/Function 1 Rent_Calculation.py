from datetime import datetime, timedelta


def calculate_total_rent(vehicle_no, rented_date, return_date, with_driver):
    # Example rates (in a real application, retrieve these from a database)
    daily_rate = get_daily_rate(vehicle_no)
    weekly_rate = get_weekly_rate(vehicle_no)
    monthly_rate = get_monthly_rate(vehicle_no)
    driver_daily_rate = get_driver_rate() if with_driver else 0

    # Calculate the rental duration
    rented_date = datetime.strptime(rented_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")
    rental_duration = (return_date - rented_date).days

    # Calculate total rent
    total_rent = 0
    while rental_duration > 0:
        if rental_duration >= 30:
            total_rent += monthly_rate
            rental_duration -= 30
        elif rental_duration >= 7:
            total_rent += weekly_rate
            rental_duration -= 7
        else:
            total_rent += daily_rate
            rental_duration -= 1

    # Add driver cost if required
    if with_driver:
        total_rent += driver_daily_rate * (return_date - rented_date).days

    return total_rent


def get_daily_rate(vehicle_no):
    # Retrieve the daily rate based on the vehicle_no
    rates = {
        "small_car": 30,
        "sedan_car": 40,
        "suv": 60,
        "jeep": 70,
        "van": 50
    }
    return rates.get(vehicle_no, 0)


def get_weekly_rate(vehicle_no):
    # Retrieve the weekly rate based on the vehicle_no
    rates = {
        "small_car": 180,
        "sedan_car": 240,
        "suv": 360,
        "jeep": 420,
        "van": 300
    }
    return rates.get(vehicle_no, 0)


def get_monthly_rate(vehicle_no):
    # Retrieve the monthly rate based on the vehicle_no
    rates = {
        "small_car": 720,
        "sedan_car": 960,
        "suv": 1440,
        "jeep": 1680,
        "van": 1200
    }
    return rates.get(vehicle_no, 0)


def get_driver_rate():
    # Example daily rate for a driver
    return 20


# Test the function
total_rent = calculate_total_rent("sedan_car", "2023-04-01", "2023-04-10", True)
print(f"Total rent (sedan car, 10 days with driver): ${total_rent}")
