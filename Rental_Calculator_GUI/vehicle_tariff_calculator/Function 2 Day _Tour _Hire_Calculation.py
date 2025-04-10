from datetime import datetime


def calculate_day_tour_hire(vehicle_no, package_type, start_time, end_time, start_km_reading, end_km_reading):
    # Example rates (in a real application, retrieve these from a database)
    base_rate, max_km, max_hours, extra_km_rate, waiting_charge_rate = get_package_info(vehicle_no, package_type)

    # Calculate duration in hours
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
    duration = (end_time - start_time).seconds / 3600

    # Calculate charges
    base_hire_charge = base_rate
    extra_km_charge = max(0, end_km_reading - start_km_reading - max_km) * extra_km_rate
    waiting_charge = max(0, duration - max_hours) * waiting_charge_rate

    return base_hire_charge, waiting_charge, extra_km_charge


def get_package_info(vehicle_no, package_type):
    # Retrieve package info based on the vehicle_no and package_type
    # In a real application, these values would be retrieved from a database
    package_info = {
        ("sedan_car", "100km_per_day"): (100, 100, 8, 0.5, 10),
        ("suv", "200km_per_day"): (200, 200, 10, 1, 15),
        # Add more packages as needed
    }
    return package_info.get((vehicle_no, package_type), (0, 0, 0, 0, 0))


# Test the function
base_hire_charge, waiting_charge, extra_km_charge = calculate_day_tour_hire("sedan_car", "100km_per_day",
                                                                            "2023-04-01 08:00", "2023-04-01 18:00", 0,
                                                                            110)
print(f"Base hire charge: ${base_hire_charge}, Waiting charge: ${waiting_charge}, Extra km charge: ${extra_km_charge}")
