# 🏢 Lease Expiration Dashboard

A web-based dashboard built with **Python**, **Pandas**, and **Streamlit** for analyzing commercial real estate lease expirations.

This project allows property managers and real estate analysts to upload an Excel or CSV lease report and instantly identify leases approaching expiration.

## 🚀 Live Demo

https://cw-lease-expiration-dashboard.streamlit.app

---

## Features

- Upload Excel (.xlsx) or CSV lease reports
- Filter leases by expiration window:
  - 30 Days
  - 60 Days
  - 90 Days
  - 180 Days
  - 365 Days
- Filter results by city
- Automatically classify leases as:
  - ⛔ URGENT
  - ⚠️ WARNING
  - 🟢 OK
- View key metrics:
  - Number of expiring leases
  - Total monthly rent at risk
- Interactive lease table
- Download filtered results as CSV
- Lease status summary chart

---

## Technologies Used

- Python
- Streamlit
- Pandas
- OpenPyXL

---

## Project Structure

```
Real-Estate-Report-Generator/
│
├── dashboard.py
├── app.py
├── properties.csv
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/markfarid4/Real-Estate-Report-Generator.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run dashboard.py
```

---

## Dashboard Preview

*(Add screenshots here after uploading them to GitHub.)*

---

## Example Workflow

1. Upload a lease report.
2. Select the desired expiration window.
3. Filter by city if needed.
4. Review upcoming lease expirations.
5. Download the filtered report.

---

## Future Improvements

- Search by Property ID
- Filter by state
- Export to Excel
- Interactive charts using Plotly
- Summary cards by city
- Dark mode

---

## Author

**Mark Farid**

Built as a portfolio project demonstrating Python, data analysis, and dashboard development using Streamlit.