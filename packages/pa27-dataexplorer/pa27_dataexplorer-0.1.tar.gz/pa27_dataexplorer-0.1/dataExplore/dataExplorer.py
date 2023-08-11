import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DataExplorer:
    def __init__(self, file_name):
        df = pd.read_csv(file_name)
        self.data = df

    def summary(self):
        shape = self.data.shape
        columns = self.data.columns
        summary = f'''
        The dataset has {shape[0]} columns and {shape[1]} rows.
        Below are the column list:
        {columns}
        '''
        return summary

    def histogram(self):
        
        data = self.data
        # Find numerical columns
        numerical_columns = data.select_dtypes(include=['int', 'float']).columns.tolist()
        self.numerical_columns = numerical_columns

        # Create a histogram for each numerical variable
        for col in numerical_columns:
            data[col].hist(bins=20, edgecolor='black')
            plt.title(f'{col} Distribution')
            plt.xlabel(f'{col}')
            plt.ylabel('Frequency')
            plt.show()
        
    
    def heat_map(self):
        # Calculate the correlation matrix
        corr_matrix = self.data[self.numerical_columns].corr()

        # Set the figure size
        plt.figure(figsize=(30, 20))

        # Create the heatmap using seaborn
        sns.heatmap(corr_matrix, annot=True, cmap='mako', fmt='.2f', linewidths=0.5)

        # Add title
        plt.title('Correlation Heatmap')

        # Show the plot
        plt.show()

    def detect_outliers(self):
        pass

    def missing_data_info(self):
        #columns with no missing values
        no_nan_cols = self.data.columns[self.data.isnull().mean() == 0]
        #columns with more than 50% rows of missing values
        mid_nan_cols = self.data.columns[self.data.isnull().mean() > 0.5]
        #columns with more than 75% rows of missing values
        high_nan_cols = self.data.columns[self.data.isnull().mean() > 0.75]

        missing_data_info = f'''
        {len(no_nan_cols)} columns with no missing values: {no_nan_cols}
        --
        {len(mid_nan_cols)} columns with 50%+ missing values: {mid_nan_cols}
        --
        {len(high_nan_cols)} columns with 75%+ missing values: {high_nan_cols}
        '''

        return missing_data_info

    def create_dashboard(self):
        pass


