import pandas as pd
from datetime import datetime, timedelta

data = pd.read_csv("properties.csv")

data["Lease End Date"] = pd.to_datetime(data["Lease End Date"])

today = datetime.today()
deadline = today + timedelta(days=90)

expiring_soon = data[
    (data["Lease End Date"] >= today)
    & (data["Lease End Date"] <= deadline)
]

expiring_soon = expiring_soon.sort_values(by="Lease End Date")


total_rent = expiring_soon["Monthly Rent"].sum()

print(f"Properties Expiring Within 90 Days: {len(expiring_soon)}")
print(f"Total Monthly Rent Expiring: ${total_rent:,.0f}")
print("=" * 50)

print()

if len(expiring_soon) == 0:
    print("No leases are expiring within the next 90 days.")
else:
    print("Lease details:")
    print("=" * 50)


def print_lease(row):
    days_left = (row["Lease End Date"] - today).days

    if days_left <= 30:
        status = "🔴 URGENT"
    elif days_left <= 60:
        status = "🟡 WARNING"
    else:
        status = "🟢 OK"

    print("=" * 50)
    print(F" Index: {row['Index']}")
    print(f"{status} {row['Property Name']}")
    print("=" * 50)
    print(f"📍 City: {row['City']}")
    print(f"🗺️ State: {row['State']}")
    print(f"📅 Lease Ends: {row['Lease End Date'].strftime('%B %d, %Y')}")
    print(f"⏳ Days Left: {days_left}")
    print(f"💰 Rent: ${row['Monthly Rent']:,.0f}")
    print()

for index, row in expiring_soon.iterrows():
    print_lease(row)

