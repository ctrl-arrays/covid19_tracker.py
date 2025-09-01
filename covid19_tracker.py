import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import requests
import os
import argparse

def download_csv(url, folder="data", filename="owid-covid-data.csv"):
    """
    Downloads a CSV file from the given URL into the specified folder.
    Creates the folder if it doesn't exist.
    Returns the full path to the downloaded file.
    """
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)

    if os.path.exists(file_path):
        print(f"Using existing local data: {file_path}")
        return file_path

    try:
        print(f"Downloading data from: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Download complete: {file_path}")
        return file_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        exit()

def main():
    # This allows the user to specify the country to track when running the script
    parser = argparse.ArgumentParser(description="COVID-19 Tracker")
    parser.add_argument("--country", type=str, required=True, help="Country name to track COVID-19 data for")
    parser.add_argument("--save", action="store_true", help="Save filtered data")
    args = parser.parse_args()
    country_name = args.country

    # Download/Check if a local 'data' folder exists; if not, create it
    data_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    data_file = download_csv(data_url)

    # Load data into pandas
    df = pd.read_csv(data_file)

    # Filter data for the chosen country
    country_df = df[df["location"] == country_name]

    # Check if data exists for the country
    if country_df.empty:
        print(f"No data found for {country_name}. Please check the country name.")
        exit()

    # Check required_columns
    required_columns = ["date", "total_cases", "total_deaths"]
    missing = [col for col in required_columns if col not in country_df.columns]
    if missing:
        print(f"Missing columns in data: {missing}")
        exit()

    # Convert date column to datetime type
    country_df["date"] = pd.to_datetime(country_df["date"])

    # Plot total cases over time using matplotlib + seaborn
    plt.figure(figsize=(12,6))
    sns.lineplot(data=country_df, x="date", y="total_cases")
    plt.title(f"COVID-19 Total Cases in {country_name}")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot total deaths over time using matplotlib + seaborn
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=country_df, x="date", y="total_deaths", color='red')
    plt.title(f"COVID-19 Total Deaths in {country_name}")
    plt.xlabel("Date")
    plt.ylabel("Total Deaths")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Interactive plot using plotly
    fig = px.line(
        country_df,
        x="date",
        y=["total_cases", "total_deaths"],
        title=f"COVID-19 Cases and Deaths in {country_name}",
        labels={"value": "Count", "date": "Date", "variable": "Metric"}
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Count",
        legend_title="Metric",
        hovermode="x unified"
    )
    fig.show()

    # Save filtered country data (optional)
    if args.save:
        if not os.path.exists("output"):
            os.makedirs("output")
        output_file = f"output/{country_name}_covid_data.csv"
        country_df.to_csv(output_file, index=False)
        print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    main()
