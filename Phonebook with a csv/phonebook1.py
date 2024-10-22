# Saves names and numbers to a CSV file

import csv
from cs50 import get_string

# Get name and number
name = get_string("Name: \n")
number = get_string("Number: \n")      

# Open CSV file
with open("phonebook.csv", "a") as file:

    # Print to file
    writer = csv.writer(file)
    writer.writerow((name, number))
