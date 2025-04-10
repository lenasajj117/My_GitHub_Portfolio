from datetime import datetime


def calculate_long_tour_hire(vehicle_no, package_type, start_date, end_date, start_km_reading, end_km_reading):
    # Example rates (in a real application, retrieve these from a database)
    base_rate, max_km, extra_km_rate, overnight_stay_rate = get_long_tour_package_info(vehicle_no, package_type)

    # Calculate duration in days
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    duration_days = (end_date - start_date).days

    # Calculate charges
    base_hire_charge = base_rate * duration_days
    extra_km_charge = max(0, end_km_reading - start_km_reading - max_km * duration_days) * extra_km_rate
    overnight_stay_charge = overnight_stay_rate * (duration_days - 1)

    return base_hire_charge, overnight_stay_charge, extra_km_charge


def get_long_tour_package_info(vehicle_no, package_type):
    # Retrieve package info based on the vehicle_no and package_type
    # In a real application, these values would be retrieved from a database
    package_info = {
        ("suv", "long_tour"): (300, 500, 0.7, 50),
        # Add more packages as needed
    }
    return package_info.get((vehicle_no, package_type), (0, 0, 0, 0))


# Test the function
base_hire_charge, overnight_stay_charge, extra_km_charge = calculate_long_tour_hire("suv", "long_tour", "2023-04-01",
                                                                                    "2023-04-04", 0, 550)
print(
    f"Base hire charge: ${base_hire_charge}, Overnight stay charge: ${overnight_stay_charge}, Extra km charge: ${extra_km_charge}")
