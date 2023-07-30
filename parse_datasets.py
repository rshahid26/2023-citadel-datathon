import pandas as pd

# Split into git MB limits
size_limit = 100 * 1024 * 1024  # 100MB

with open('./datasets/flight_traffic.csv', 'r') as read_file,\
        open('./datasets/flight_traffic_1.csv', 'w') as write_file:
    bytes_written = 0
    for line in read_file:
        bytes_written += len(line.encode('utf-8'))  # Get the byte size of the line
        if bytes_written > size_limit:
            break
        write_file.write(line)

# Save unique edges (determined by origin_airport, destination_airport tuple)
df_flight_traffic_raw = pd.read_csv("./datasets/flight_traffic.csv")
df_flight_traffic = df_flight_traffic_raw.drop_duplicates(
    subset=['origin_airport', 'destination_airport'])

df_flight_traffic.to_csv('unique_flights.csv', index=False)