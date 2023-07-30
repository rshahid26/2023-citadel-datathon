import pandas as pd

# Fill in airports dataset holes
df_airports = pd.read_csv("./datasets/airports.csv", encoding='ISO-8859-1')

missing_data = df_airports[df_airports[['longitude', 'latitude']].isnull().any(axis=1)]

df_airports.loc[df_airports['airport_id'] == 'ECP', 'longitude'] = -85.795611
df_airports.loc[df_airports['airport_id'] == 'ECP', 'latitude'] = 30.357106
df_airports.loc[df_airports['airport_id'] == 'PBG', 'longitude'] = -73.468168
df_airports.loc[df_airports['airport_id'] == 'PBG', 'latitude'] = 44.652054
df_airports.loc[df_airports['airport_id'] == 'UST', 'longitude'] = -81.342548
df_airports.loc[df_airports['airport_id'] == 'UST', 'latitude'] = 29.954252

df_airports.to_csv("./datasets/airports.csv", index=False)
missing_data = df_airports[df_airports[['longitude', 'latitude']].isnull().any(axis=1)]
print(missing_data)
