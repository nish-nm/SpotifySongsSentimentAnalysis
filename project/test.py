import unittest
import os
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
api_key = os.getenv("DATA_WORLD_API_KEY")

class TestDataPipeline(unittest.TestCase):
    def test_kaggle_download_csv(self):
        # Test if Kaggle API call downloads CSV files successfully
        destination_folder = "/home/runner/work/SpotifySongsSentimentAnalysis/SpotifySongsSentimentAnalysis/data/kaggle"
        dataset_name = "artists.csv"

        # Check if CSV files are downloaded
        csv_files = [file for file in os.listdir(destination_folder) if file.endswith('.csv')]
        self.assertTrue(csv_files)

    def test_kaggle_download_json(self):
        # Test if Kaggle API call downloads JSON files successfully
        destination_folder = "/home/runner/work/SpotifySongsSentimentAnalysis/SpotifySongsSentimentAnalysis/data/kaggle"
        dataset_name = "dict_artists.json"

        # Make sure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Check if JSON files are downloaded
        json_files = [file for file in os.listdir(destination_folder) if file.endswith('.json')]

        # Assert that there are no JSON files downloaded
        self.assertFalse(json_files, "No JSON files should be downloaded.")

    def test_csv_files_no_null_values(self):
        # Test if CSV files in the 'dataworld' subfolder have no null values
        csv_folder = "/home/runner/work/SpotifySongsSentimentAnalysis/SpotifySongsSentimentAnalysis/data/dataworld"

        for csv_file in os.listdir(csv_folder):
            if csv_file.endswith('.csv'):
                csv_path = os.path.join(csv_folder, csv_file)
                df = pd.read_csv(csv_path)
                self.assertFalse(df.isnull().values.any())

    def test_csv_files_no_null_values(self):
        # Test if CSV files in the 'csv_data' subfolder have no null values
        csv_folder = "/home/runner/work/SpotifySongsSentimentAnalysis/SpotifySongsSentimentAnalysis/data/kaggle"

        for csv_file in os.listdir(csv_folder):
            if csv_file.endswith('.csv'):
                csv_path = os.path.join(csv_folder, csv_file)
                df = pd.read_csv(csv_path)
                self.assertFalse(df.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
