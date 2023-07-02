import csv
import random

# Define the list of cruise ship names
cruise_ships = [
    "Norwegian Prima",
    "Norwegian Viva",
    "Celebrity Apex",
    "MSC Virtuosa",
    "Odyssey of the Seas",
    "Enchanted Princess",
    "Mardi Gras",
    "Scarlet Lady",
    "AIDAcosma",
    "Disney Wish",
    "Carnival Celebration",
    "Wonder of the Seas",
    "World Voyager",
    "Evrima",
    "Silver Origin",
    "Spirit of Adventure",
    "Iona",
    "Costa Firenze",
    "Valiant Lady",
    "Seabourn Venture"
]

# Define the list of revenue sources
revenue_sources = [
    "Ticket Sales",
    "Onboard Purchases",
    "Excursions and Tours",
    "Beverage Packages",
    "Internet and Communication Services",
    "Onboard Events and Entertainment",
    "Casino and Gambling",
    "Photography Services",
    "Retail Sales",
    "Private Events and Charters",
    "Spa and Wellness Services"
]

# Generate and write the dataset to CSV
filename = "cruise_ship_revenue.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Cruise Ship", "Cruise Line", *revenue_sources, "Net Revenue"])

    for ship in cruise_ships:
        if ship == "Norwegian Prima" or ship == "Norwegian Viva":
            cruise_line = "Norwegian Cruiselines"
        else:
            cruise_line = random.choice(["Norwegian Cruiselines", "Celebrity Cruises", "MSC Cruises", "Royal Caribbean",
                                         "Princess Cruises"])

        revenue = [random.randint(50000, 500000) for _ in range(len(revenue_sources))]
        net_revenue = sum(revenue)
        writer.writerow([ship, cruise_line, *revenue, net_revenue])

print(f"Dataset generated and saved as '{filename}' in the current directory.")
