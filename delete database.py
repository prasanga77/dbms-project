import os

# Specify the path to the database file
database_file = "attendance.db"

# Check if the file exists
if os.path.exists(database_file):
    # Delete the file
    os.remove(database_file)
    print("Database cleared successfully!")
else:
    print("Database file not found.")

