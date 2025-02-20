import http.client
import os
from dotenv import load_dotenv
import pandas as pd
import math
import numpy as np

# Load environment variables from the . file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("DATA_WORLD_API_KEY")

# Make sure the API key available
if api_key is None:
    raise ValueError("API_KEY not found in the environment variables")

def load_dataworld(api_key, output_folder=None, output_filename=None, csv_filename=None):
    """
    Downloads the dataset from DataWorld and saves it as an XLSX file.
    If there are any null values in the DataFrame, it drops them and saves the DataFrame as a CSV file.

    Parameters:
    api_key (str): The API key for DataWorld.
    output_folder (str): The folder where the XLSX file will be saved. Default: "/Users/sash/projects/MADE/made-template/data/dataworld"
    output_filename (str): The name of the XLSX file. Default: "Spotify_billboard.xlsx"
    csv_filename (str): The name of the CSV file. Default: "Spotify_billboard.csv"

    Returns:
    pandas.DataFrame: The DataFrame containing the dataset.
    """
    conn = http.client.HTTPSConnection("api.data.world")

    headers = {'Authorization': f'Bearer {api_key}'}

    # Download the dataset from DataWorld
    conn.request("GET", 
                 "/v0/file_download/tazwar2700/billboard-hot-100-with-lyrics-and-emotion-mined-scores/Final%20processed%20dataset.xlsx", 
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Save the data to an XLSX file in the specified folder
    if output_folder is None:
        output_folder = "/Users/sash/projects/MADE/made-template/data/dataworld"
    if output_filename is None:
        output_filename = "Spotify_billboard.xlsx"
    output_file_path = os.path.join(output_folder, output_filename)
    with open(output_file_path, 'wb') as f:
        f.write(data)

    # Load the data into a pandas DataFrame
    df = pd.read_excel(output_file_path, engine='openpyxl')

    # Check for null values in the DataFrame
    null_check = df.isnull().any().any()

    # Save the data as a CSV file in the specified folder
    if null_check:
        df = df.dropna()
        if csv_filename is None:
            csv_filename = "Spotify_billboard.csv"
        output_file_path_csv = os.path.join(output_folder, csv_filename)
        df.to_csv(output_file_path_csv, index=False)

    return df

import os
from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv

def load_kaggle_api_key():
    """
    Load Kaggle API key from environment variables.

    Returns:
    - str: Kaggle API key
    """
    api_key_kaggle = os.getenv("key")
    if api_key_kaggle is None:
        raise ValueError("KAGGLE_API_KEY not found in environment variables")
    return api_key_kaggle

def kaggle_download(dataset_name, destination_folder="/Users/sash/projects/MADE/made-template/data/kaggle"):
    """
    Download all files from a Kaggle dataset.

    Parameters:
    - dataset_name (str): Name of the Kaggle dataset (e.g., 'yamaerenay/spotify-dataset-19212020-600k-tracks').
    - destination_folder (str): Destination folder for downloading files.

    Returns:
    - None
    """
    # Load Kaggle API key from environment variables
    api_key_kaggle = load_kaggle_api_key()

    # Set Kaggle API key
    os.environ["KAGGLE_KEY"] = api_key_kaggle
    os.environ["KAGGLE_CONFIG_DIR"] = os.path.expanduser("~/.kaggle")
    os.environ["KAGGLE_USERNAME"] = os.getenv("username")  # Dummy username required by Kaggle API

    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Download the dataset files to the destination folder
    api.dataset_download_files(dataset_name, path=destination_folder, unzip=True)

    print("All files downloaded successfully.")
    df = pd.read_csv(os.path.join(destination_folder, "tracks.csv"))  

    # Check for null values
    null_check = df.isnull().any().any()

    if null_check:
        df=df.dropna()
        output_file_path_csv = os.path.join(destination_folder, 'tracks.csv')
        df.to_csv(output_file_path_csv, index=False)
        os.remove(os.path.join(destination_folder, "dict_artists.json"))  # Replace with the actual file name
        os.remove(os.path.join(destination_folder, "artists.csv"))

        print("Null values checked and specific files deleted.")

def split_csv(input_file, output_folder, file_size_limit_mb=25):
    """
    Split a large CSV file into smaller files based on size.

    Parameters:
    - input_file (str): Path to the input CSV file.
    - output_folder (str): Folder where the smaller CSV files will be saved.
    - file_size_limit_mb (int): Maximum size (in MB) for each smaller CSV file. Default is 25 MB.

    Returns:
    - None
    """

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Calculate the size limit in bytes
    file_size_limit = file_size_limit_mb * 1024 * 1024

    # Read the input CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Calculate the number of smaller files needed
    num_files = math.ceil(os.path.getsize(input_file) / file_size_limit)

    # Split the DataFrame into smaller DataFrames
    smaller_dfs = np.array_split(df, num_files)

    # Save each smaller DataFrame as a separate CSV file
    for i, smaller_df in enumerate(smaller_dfs):
        smaller_file_path = os.path.join(output_folder, f"part_{i + 1}.csv")
        smaller_df.to_csv(smaller_file_path, index=False)

    print(f"CSV file split into {num_files} smaller files successfully.")





# Call the functions here
dataset_name = "yamaerenay/spotify-dataset-19212020-600k-tracks"
load_dataworld(api_key)
kaggle_download(dataset_name)
input_csv = "/Users/sash/projects/MADE/made-template/data/kaggle/tracks.csv"
output_folder = "/Users/sash/projects/MADE/made-template/data/kaggle"
split_csv(input_csv, output_folder)

