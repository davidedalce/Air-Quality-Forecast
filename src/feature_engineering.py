import pandas as pd

class FeatureEngineering:
    """
    A class to perform feature engineering operations, data cleaning and data exploration.
    """

    def __init__(self, df):
        """
        Initializes the FeatureEngineering class with a DataFrame.
        """
        self.df = df

    def data_cleaning(self):
        """
        Cleans the dataset by removing missing values and duplicates.
        Updates the class instance with the cleaned DataFrame.
        """
        if self.df.isna().sum().any():
            print(f"Columns with missing values:\n{self.df.isna().sum()}")
            self.df = self.df.dropna()
        else:
            print("No missing values found 🚀")

        if self.df.duplicated().any():
            print(f"Duplicate rows found: {self.df[self.df.duplicated()]}")
            self.df = self.df.drop_duplicates()
        else:
            print("No duplicates found 🚀")

        print("Data has been cleaned 🥳")
        return self.df
    
    def find_uniques(self):
        
        """
        Prints the unique entries in a dataframe

        """

        for col in self.df.columns:

            bold_col = f"\033[1m{col}\033[0m"

            if self.df[col].dtype in ["object", "bool", "category"]:
                print(f"{bold_col}: has unique {self.df[col].nunique()} values: {self.df[col].unique()} \n")
                
            else:
                print(f"{bold_col}: has {self.df[col].nunique()} unique values \n")

