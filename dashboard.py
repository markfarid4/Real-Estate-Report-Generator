import streamlit as st

st.set_page_config(layout="wide")

st.title("Lease Expiration Dashboard")
st.write("Cushman & Wakefield Lease Reporting Tool")

import pandas as pd
from datetime import datetime, timedelta

uploaded_file = st.file_uploader(
    "Upload a lease report",
    type=["csv", "xlsx"]
)

if uploaded_file is None:
    st.info("Upload a CSV or Excel lease report to continue.")
    st.stop()

if uploaded_file.name.lower().endswith(".csv"):
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_excel(uploaded_file)

required_columns = [
    "Property ID",
    "Property Name",
    "City",
    "State",
    "Lease End Date",
    "Monthly Rent"
]

missing_columns = [
    column
    for column in required_columns
    if column not in data.columns
]

if missing_columns:
    st.error(
        "The uploaded file is missing these columns: "
        + ", ".join(missing_columns)
    )
    st.stop()

data["Lease End Date"] = pd.to_datetime(data["Lease End Date"])

today = pd.Timestamp.today().normalize()
days_options = [30, 60, 90, 180, 365]

days_ahead = st.selectbox(
    "Show leases expiring within:",
    days_options,
    index=2,
    format_func=lambda x: f"{x} Days"
)

deadline = today + timedelta(days=days_ahead)

expiring_soon = data[
    (data["Lease End Date"] >= today)
    & (data["Lease End Date"] <= deadline)

]

expiring_soon["Days Left"] = (expiring_soon["Lease End Date"] - today).dt.days

def get_status(days_left):
    if days_left <= 30:
        return "⛔ URGENT"
    elif days_left <= 60:
        return "⚠️ WARNING"
    else:
        return "🟢 OK"

expiring_soon["Status"] = expiring_soon ["Days Left"].apply(get_status)

expiring_soon = expiring_soon.sort_values(
    by="Days Left",
    ascending=True
)
expiring_soon = expiring_soon.reset_index(drop=True)
expiring_soon.index = expiring_soon.index + 1

city_options = ["All"] + sorted(expiring_soon["City"].unique().tolist())
selected_city = st.selectbox("Select City:", city_options)

if selected_city != "All":
    expiring_soon = expiring_soon[expiring_soon["City"] == selected_city]

expiring_soon["Index"] = range(1, len(expiring_soon) + 1)

total_properties = len(expiring_soon)

total_rent = expiring_soon["Monthly Rent"].sum()

col1, col2= st.columns(2)

col1.metric (
label=f"Properties with Leases Expiring Within {days_ahead} Days:",
    value=total_properties
)

col2.metric(
    label="Total Montly Rent for Expiring Leases:",
    value=f"${total_rent:,.0f}"
)


st.subheader(f"Leases Expiring Within {days_ahead} Days")
display_data = expiring_soon.copy()
display_data["Days Left"] = display_data["Days Left"].astype(str) + " days"
display_data["Lease End Date"] = display_data["Lease End Date"].dt.strftime("%B %d, %Y")
display_data["Monthly Rent"] = display_data["Monthly Rent"].apply(
    lambda x: f"${x:,.0f}"
)
display_data["Property ID"] = "#" + display_data["Property ID"].astype(str)

display_data = display_data[
    [
        "Index",
        "Property ID",
        "Property Name",
        "Status",
        "Days Left",
        "City",
        "State",
        "Lease End Date",
        "Monthly Rent",
    ]
]

csv = display_data.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    label="Download Filtered Report",
    data=csv,
    file_name="expiring_leases.csv",
    mime="text/csv"
)

st.dataframe(display_data ,hide_index=True)

status_counts = expiring_soon["Status"].value_counts()
st.subheader("Lease Status Summary")
st.bar_chart(status_counts)

st.success("Private website.")