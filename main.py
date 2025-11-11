from google.cloud import bigquery
import pandas as pd
import os

# Set environment variable for credentials
# Check if the credential file exists
credentials_path = os.path.join(
    os.path.dirname(__file__), 
    'credentials', 
    'bigquery-key.json'
)

if os.path.exists(credentials_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
else:
    print("WARNING: Credentials file not found. Please set up BigQuery credentials.")
    print("See README.md for setup instructions.")
    exit(1)

# Configuration - users should modify this
PROJECT_ID = 'etl-pipline-project-477623'  # TODO: Update with your project ID
DATASET_ID = 'main'
TABLE_ID = 'cleaned_data_table'

try:
    # Initialize the client (will automatically use the environment variable)
    client = bigquery.Client(project=PROJECT_ID)
    # Test connection
    print(f"Successfully connected to project: {client.project}")
except Exception as e:
    print(f"Error connecting to BigQuery client: {e}")
    print("Make sure you have set up credentials correctly (see README.md)")
    exit(1)

# Ensure the datafile is not empty
datafile = pd.read_csv('data/Electric_Vehicle__EV__Charging_Data-_Municipal_Lots_and_Garages.csv')
if not datafile.empty:
    print('datafile is not empty')

'''
Wanted data columns:
     - Date
     - Station Name
     - Location Name
     - Charge Box ID
     - Charge Duration (min)
     - Connected Duration (min)
     - Energy Provided (kWh)
'''
data_columns_to_keep = ['Date', 'Station Name', 'Location Name', 'Charge Box ID',
                              'Charge Duration (min)', 'Connected Duration (min)', 'Energy Provided (kWh)']

data_table_not_null = datafile[data_columns_to_keep].dropna()

# rename columns to align with BigQuery naming conventions
data_table_not_null.columns = (data_table_not_null.columns
                               .str.replace(' ', '_').str.replace(r'[()]', '', regex=True).str.lower())

# limit the number of decimal places to 4
data_table_not_null = data_table_not_null.round({'charge_duration_min': 4, 'connected_duration_min': 4, 'energy_provided_kwh': 4})

print("Shape of cleaned datafile:", data_table_not_null.shape)
try:
    client.load_table_from_dataframe(data_table_not_null, 'main.cleaned_data_table',
                                     job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE"))
    print("Table loaded successfully!")
except Exception as e:
    print(f"Error when loading table: {e}")