
# Import the pandas library
import pandas as pd

# Load the CSV file into a DataFrame named 'cars'
cars = pd.read_csv('cars.csv')

# Display a message indicating that the DataFrame has been loaded
print("DataFrame 'cars' has been loaded.")
cars

# Selects the first 5 rows and every second column starting from column index 1
cars.iloc[:5,1::2]

# Selects all rows from the DataFrame `cars` where the value in the 'Model' column is 'Mazda RX4'
cars.loc[cars['Model'] == 'Mazda RX4']

# Selects the 'Model' and 'cyl' columns for rows where the 'Model' column is 'Camaro Z28'
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]

# Retrieves the 'Model', 'cyl', and 'gear' columns for rows where the 'Model' is 'Mazda RX4 Wag', 'Ford Pantera L', or 'Honda Civic'.
cars.loc[
    (cars['Model'] == 'Mazda RX4 Wag') | 
    (cars['Model'] == 'Ford Pantera L') | 
    (cars['Model'] == 'Honda Civic')
] [['Model', 'cyl', 'gear']]
