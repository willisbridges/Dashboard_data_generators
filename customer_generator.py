import csv
import random

# Define the number of rows in the dataset
num_rows = 3000

# Define the list of cities and states
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Philadelphia",
    "Phoenix", "San Antonio", "San Diego", "Dallas", "San Francisco",
    "Austin", "Seattle", "Denver", "Boston", "Nashville", "Atlanta",
    "Miami", "Portland", "Las Vegas", "New Orleans"
]

states = [
    "New York", "California", "Illinois", "Texas", "Pennsylvania",
    "Arizona", "Texas", "California", "Texas", "California",
    "Texas", "Washington", "Colorado", "Massachusetts", "Tennessee",
    "Georgia", "Florida", "Oregon", "Nevada", "Louisiana"
]

# Generate and write the dataset to CSV
filename = "cruise_customer_dataset.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Age", "Gender", "Name", "Birth", "Race", "Home City", "Home State", "Amount Spent", "Estimated Income", "Destination"])

    for i in range(1, num_rows + 1):
        id = i
        age = random.randint(18, 80)
        gender = random.choice(["Male", "Female"])
        name = f"Customer {i}"
        birth = f"{random.randint(1950, 2005)}-{'%02d' % random.randint(1, 12)}-{'%02d' % random.randint(1, 28)}"
        race = random.choice(["White", "Black", "Asian", "Hispanic", "Other"])
        home_city = random.choice(cities)
        home_state = states[cities.index(home_city)]
        amount_spent = round(random.uniform(1000, 10000), 2)
        estimated_income = round(random.uniform(20000, 150000), 2)
        destination = random.choice(["Alaska", "Hawaii", "Asia", "Europe", "Middle East & Africa", "South America"])

        writer.writerow([id, age, gender, name, birth, race, home_city, home_state, amount_spent, estimated_income, destination])

print(f"Dataset generated and saved as '{filename}' in the current directory.")
