import pandas as pd

def time_series_analysis(data):
    time_series = pd.to_datetime(data["Date"])
    data.set_index(time_series, inplace=True)
    return data

# Example usage:
data = pd.read_csv("time_series_data.csv")
time_series_data = time_series_analysis(data)
print(time_series_data)
