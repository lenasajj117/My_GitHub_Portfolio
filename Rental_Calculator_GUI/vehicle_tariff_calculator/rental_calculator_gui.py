import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def calculate_total_rent(vehicle_no, rented_date, return_date, with_driver):
    # Sample rates (replace with stored values or database queries)
    rates = {
        "small_car": {"daily": 30, "weekly": 180, "monthly": 720},
        "sedan_car": {"daily": 40, "weekly": 240, "monthly": 960},
        "suv": {"daily": 60, "weekly": 360, "monthly": 1440},
        "jeep": {"daily": 70, "weekly": 420, "monthly": 1680},
        "van": {"daily": 50, "weekly": 300, "monthly": 1200},
    }

    # Driver daily rate
    driver_rate = 20 if with_driver else 0

    # Convert vehicle_no to lowercase for case-insensitive comparison
    vehicle_no = vehicle_no.lower()

    # Calculate rental duration
    rented_date = datetime.strptime(rented_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")
    rental_duration = (return_date - rented_date).days

    # Calculate total rent
    total_rent = 0
    if rental_duration >= 30:
        months = rental_duration // 30
        rental_duration %= 30
        total_rent += months * rates[vehicle_no]["monthly"]
    if rental_duration >= 7:
        weeks = rental_duration // 7
        rental_duration %= 7
        total_rent += weeks * rates[vehicle_no]["weekly"]
    total_rent += rental_duration * rates[vehicle_no]["daily"]

    # Add driver cost if applicable
    total_rent += rental_duration * driver_rate

    return total_rent



class RentCalculatorGUI:
    def __init__(self, root):
        self.root = root
        root.title("Rent Calculator")

        # Labels and entry fields for rental calculation
        self.rental_frame = tk.LabelFrame(root, text="Rental Calculation")
        self.rental_frame.grid(row=0, column=0, padx=10, pady=10)

        self.vehicle_no_label = tk.Label(self.rental_frame, text="Vehicle Type:")
        self.vehicle_no_label.grid(row=0, column=0)
        self.vehicle_no_entry = tk.Entry(self.rental_frame)
        self.vehicle_no_entry.grid(row=0, column=1)

        self.rented_date_label = tk.Label(self.rental_frame, text="Rented Date (YYYY-MM-DD):")
        self.rented_date_label.grid(row=1, column=0)
        self.rented_date_entry = tk.Entry(self.rental_frame)
        self.rented_date_entry.grid(row=1, column=1)

        self.return_date_label = tk.Label(self.rental_frame, text="Return Date (YYYY-MM-DD):")
        self.return_date_label.grid(row=2, column=0)
        self.return_date_entry = tk.Entry(self.rental_frame)
        self.return_date_entry.grid(row=2, column=1)

        self.with_driver_label = tk.Label(self.rental_frame, text="With Driver (True/False):")
        self.with_driver_label.grid(row=3, column=0)
        self.with_driver_entry = tk.Entry(self.rental_frame)
        self.with_driver_entry.grid(row=3, column=1)

        # Button for rental calculation
        self.rental_button = tk.Button(self.rental_frame, text="Calculate Rental", command=self.calculate_rental)
        self.rental_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Result label for rental calculation
        self.rental_result_label = tk.Label(self.rental_frame, text="")
        self.rental_result_label.grid(row=5, column=0, columnspan=2)

        # Labels and entry fields for day tour hire calculation
        self.day_tour_frame = tk.LabelFrame(root, text="Day Tour Hire Calculation")
        self.day_tour_frame.grid(row=1, column=0, padx=10, pady=10)

        self.vehicle_no_label2 = tk.Label(self.day_tour_frame, text="Vehicle Type:")
        self.vehicle_no_label2.grid(row=0, column=0)
        self.vehicle_no_entry2 = tk.Entry(self.day_tour_frame)
        self.vehicle_no_entry2.grid(row=0, column=1)

        self.package_type_label = tk.Label(self.day_tour_frame, text="Package Type:")
        self.package_type_label.grid(row=1, column=0)
        self.package_type_entry = tk.Entry(self.day_tour_frame)
        self.package_type_entry.grid(row=1, column=1)

        self.start_time_label = tk.Label(self.day_tour_frame, text="Start Time (HH:MM):")
        self.start_time_label.grid(row=2, column=0)
        self.start_time_entry = tk.Entry(self.day_tour_frame)
        self.start_time_entry.grid(row=2, column=1)

        self.end_time_label = tk.Label(self.day_tour_frame, text="End Time (HH:MM):")
        self.end_time_label.grid(row=3, column=0)
        self.end_time_entry = tk.Entry(self.day_tour_frame)
        self.end_time_entry.grid(row=3, column=1)

        self.start_km_label = tk.Label(self.day_tour_frame, text="Start KM Reading:")
        self.start_km_label.grid(row=4, column=0)
        self.start_km_entry = tk.Entry(self.day_tour_frame)
        self.start_km_entry.grid(row=4, column=1)

        self.end_km_label = tk.Label(self.day_tour_frame, text="End KM Reading:")
        self.end_km_label.grid(row=5, column=0)
        self.end_km_entry = tk.Entry(self.day_tour_frame)
        self.end_km_entry.grid(row=5, column=1)

        # Button for day tour hire calculation
        self.day_tour_button = tk.Button(self.day_tour_frame, text="Calculate Day Tour Hire",
                                         command=self.calculate_day_tour)
        self.day_tour_button.grid(row=6, column=0, columnspan=2, pady=5)

        # Result label for day tour hire calculation
        self.day_tour_result_label = tk.Label(self.day_tour_frame, text="")
        self.day_tour_result_label.grid(row=7, column=0, columnspan=2)

        # Labels and entry fields for long tour hire calculation
        self.long_tour_frame = tk.LabelFrame(root, text="Long Tour Hire Calculation")
        self.long_tour_frame.grid(row=2, column=0, padx=10, pady=10)

        self.vehicle_no_label3 = tk.Label(self.long_tour_frame, text="Vehicle Type:")
        self.vehicle_no_label3.grid(row=0, column=0)
        self.vehicle_no_entry3 = tk.Entry(self.long_tour_frame)
        self.vehicle_no_entry3.grid(row=0, column=1)

        self.package_type_label2 = tk.Label(self.long_tour_frame, text="Package Type:")
        self.package_type_label2.grid(row=1, column=0)
        self.package_type_entry2 = tk.Entry(self.long_tour_frame)
        self.package_type_entry2.grid(row=1, column=1)

        self.start_date_label = tk.Label(self.long_tour_frame, text="Start Date (YYYY-MM-DD):")
        self.start_date_label.grid(row=2, column=0)
        self.start_date_entry = tk.Entry(self.long_tour_frame)
        self.start_date_entry.grid(row=2, column=1)

        self.end_date_label = tk.Label(self.long_tour_frame, text="End Date (YYYY-MM-DD):")
        self.end_date_label.grid(row=3, column=0)
        self.end_date_entry = tk.Entry(self.long_tour_frame)
        self.end_date_entry.grid(row=3, column=1)

        self.start_km_label2 = tk.Label(self.long_tour_frame, text="Start KM Reading:")
        self.start_km_label2.grid(row=4, column=0)
        self.start_km_entry2 = tk.Entry(self.long_tour_frame)
        self.start_km_entry2.grid(row=4, column=1)

        self.end_km_label2 = tk.Label(self.long_tour_frame, text="End KM Reading:")
        self.end_km_label2.grid(row=5, column=0)
        self.end_km_entry2 = tk.Entry(self.long_tour_frame)
        self.end_km_entry2.grid(row=5, column=1)

        # Button for long tour hire calculation
        self.long_tour_button = tk.Button(self.long_tour_frame, text="Calculate Long Tour Hire",
                                          command=self.calculate_long_tour)
        self.long_tour_button.grid(row=6, column=0, columnspan=2, pady=5)

        # Result label for long tour hire calculation
        self.long_tour_result_label = tk.Label(self.long_tour_frame, text="")
        self.long_tour_result_label.grid(row=7, column=0, columnspan=2)

    def calculate_rental(self):
        # Get user input for rental calculation
        vehicle_no = self.vehicle_no_entry.get()
        rented_date = self.rented_date_entry.get()
        return_date = self.return_date_entry.get()
        with_driver = self.with_driver_entry.get().lower() == "true"

        # Calculate total rent
        try:
            total_rent = calculate_total_rent(vehicle_no, rented_date, return_date, with_driver)
            # Display the result for rental calculation
            self.rental_result_label.config(text=f"Total Rental Cost: ${total_rent:.2f}")
        except Exception as e:
            # Handle invalid input or calculation errors
            messagebox.showerror("Error", f"An error occurred: {e}")

    def calculate_day_tour(self):
        # Get user input for day tour hire calculation
        vehicle_no = self.vehicle_no_entry2.get()
        package_type = self.package_type_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()
        start_km = float(self.start_km_entry.get())
        end_km = float(self.end_km_entry.get())

        # Calculate day tour hire cost (sample calculation)
        # Replace with actual calculation based on package type, time, and distance
        day_tour_cost = (end_km - start_km) * 0.5  # Example calculation

        # Display the result for day tour hire calculation
        self.day_tour_result_label.config(text=f"Day Tour Hire Cost: ${day_tour_cost:.2f}")

    def calculate_long_tour(self):
        # Get user input for long tour hire calculation
        vehicle_no = self.vehicle_no_entry3.get()
        package_type = self.package_type_entry2.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        start_km = float(self.start_km_entry2.get())
        end_km = float(self.end_km_entry2.get())

        # Calculate long tour hire cost (sample calculation)
        # Replace with actual calculation based on package type, dates, and distance
        long_tour_cost = (end_km - start_km) * 0.5  # Example calculation

        # Display the result for long tour hire calculation
        self.long_tour_result_label.config(text=f"Long Tour Hire Cost: ${long_tour_cost:.2f}")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = RentCalculatorGUI(root)
    root.mainloop()
