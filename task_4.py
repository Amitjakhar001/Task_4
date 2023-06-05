import csv
import sqlite3

# Connect to the database
conn = sqlite3.connect('shipment_database.db')
cursor = conn.cursor()

# Drop the existing shipping_data table if it exists
cursor.execute('''DROP TABLE IF EXISTS shipping_data''')

# Create the shipping_data table with the correct columns
cursor.execute('''CREATE TABLE shipping_data (
                    id INTEGER PRIMARY KEY,
                    origin_warehouse TEXT,
                    destination_store TEXT,
                    product TEXT,
                    on_time TEXT,
                    product_quantity INTEGER,
                    driver_identifier TEXT
                )''')

# Read and insert data from Spreadsheet 0
with open('shipping_data_0.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier = row
        cursor.execute('''INSERT INTO shipping_data (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier)
                          VALUES (?, ?, ?, ?, ?, ?)''', (origin_warehouse, destination_store, product, on_time, int(product_quantity), driver_identifier))

# Read and insert data from Spreadsheet 1
with open('shipping_data_1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        shipment_identifier, product, on_time = row
        cursor.execute('''INSERT INTO shipping_data (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier)
                          VALUES (?, ?, ?, ?, ?, ?)''', (None, None, product, on_time, 1, None))

# Read and insert data from Spreadsheet 2
with open('shipping_data_2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        shipment_identifier, origin_warehouse, destination_store, driver_identifier = row
        cursor.execute('''INSERT INTO shipping_data (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier)
                          VALUES (?, ?, ?, ?, ?, ?)''', (origin_warehouse, destination_store, None, None, 1, driver_identifier))

# Commit changes and close the connection
conn.commit()
conn.close()


