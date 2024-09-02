import pandas as pd
from Extractor import NEODataExtractor
from Transformer import NEODataTransformer
from Loader import NEODataLoader
import os
from dotenv import load_dotenv

class NEODataPipeline:
    def __init__(self, api_key):
        self.extractor = NEODataExtractor(api_key)
        self.transformer = NEODataTransformer()
        self.loader = NEODataLoader()

    def run(self, start_date=None, end_date=None):
        # Extract data
        raw_data = self.extractor.fetch_data(start_date, end_date)

        # Transform data
        transformed_data = self.transformer.transform(raw_data)

        # Load data
        self.loader.load(transformed_data)


if __name__ == "__main__":
    load_dotenv()
    # Replace 'your_api_key' with your actual NASA API key
    api_key=os.getenv('NASA_API_KEY')

    api_key = 'ywKJbft8HQx8ffSZTw8wjmEP2fv61KjZLaOC3hAv'
    # Initialize the ETL pipeline
    pipeline = NEODataPipeline(api_key)
    # Run the pipeline
    pipeline.run()
