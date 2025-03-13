import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

PATH = "Air-Quality-Forecast\data\lstm-datasets"

class DatasetDownloader:
    def __init__(self, dataset_slug, download_path):
        self.dataset_slug = dataset_slug
        self.download_path = download_path

    def download(self):
        api = KaggleApi()
        api.authenticate()

        # Check if the dataset is already downloaded
        if not os.path.exists(self.download_path):
            print("Dataset not found. Downloading...")
            if not os.path.exists(os.path.dirname(self.download_path)):
                os.makedirs(os.path.dirname(self.download_path))
            api.dataset_download_files(self.dataset_slug, path=self.download_path, unzip=True)
            print("Dataset downloaded successfully!")
        else:
            print("Dataset already exists. Skipping download.")

    def importer(self):

        try:
            file1_path = os.path.join(self.download_path, "LSTM-Multivariate_pollution.csv")
            file2_path = os.path.join(self.download_path, "pollution_test_data1.csv")
            self.df1 = pd.read_csv(file1_path)
            self.df2 = pd.read_csv(file2_path)
            print("Datasets imported successfully!")
        except:
            print("Datasets not found")

            
        return self.df1, self.df2
