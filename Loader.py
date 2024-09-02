class NEODataLoader:
    @staticmethod
    def load(dataframe, file_name='neo_data.csv'):
        dataframe.to_csv(file_name, index=False)
        print(f"Data successfully saved to {file_name}")
