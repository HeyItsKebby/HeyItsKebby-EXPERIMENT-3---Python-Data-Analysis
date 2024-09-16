
# Import the pandas library
import pandas as pd

# Load the CSV file into a DataFrame named 'cars'
cars = pd.read_csv('cars.csv')

# Display a message indicating that the DataFrame has been loaded
print("DataFrame 'cars' has been loaded.")
cars

# Displays the first 5 rows of the DataFrame
cars.head()

# Displays the last 5 rows of the DataFrame
cars.tail()
