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

    def runEtl(self, start_date=None, end_date=None):
        # Extract data
        raw_data = self.extractor.fetch_data(start_date, end_date)
        # print(raw_data)
        # # Transform data
        transformed_data = self.transformer.transform(raw_data)
        # print(transformed_data)
        # # Load data
        self.loader.load(transformed_data)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')

    # Initialize the ETL pipeline
    pipeline = NEODataPipeline(api_key)
    # Run the pipeline
    pipeline.runEtl()
