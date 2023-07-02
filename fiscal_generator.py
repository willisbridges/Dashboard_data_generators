import csv
from datetime import datetime, timedelta
import random

# Define the start date and end date for the time series (56 years)
start_date = datetime(1967, 1, 1)
end_date = datetime(2023, 12, 31)

# Define the list of revenue metrics
revenue_metrics = [
    "Total Revenue",
    "Ticket Revenue",
    "Onboard Revenue",
    "Excursion Revenue",
    "Ancillary Revenue",
    "Net Revenue",
    "Revenue per Passenger",
    "Occupancy Rate",
    "Revenue Yield",
    "Passenger Yield",
    "Passenger Spread",
    "Repeat Passenger Revenue",
    "Seasonal Revenue",
    "Revenue Growth Rate",
    "Market Share",
    "Revenue by Destination",
    "Revenue by Ship"
]

# Generate and write the dataset to CSV
filename = "cruise_revenue_time_series.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", *revenue_metrics])

    current_date = start_date
    while current_date <= end_date:
        row = [current_date.strftime("%Y-%m-%d")]

        for _ in range(len(revenue_metrics)):
            row.append(round(random.uniform(1000000, 5000000), 2))  # Random values for demonstration

        writer.writerow(row)

        current_date = current_date + timedelta(days=365)  # Assuming each year is 365 days

print(f"Dataset generated and saved as '{filename}' in the current directory.")
