from datetime import datetime, timedelta
import requests


class NEODataExtractor:
    """
    Een klasse die wordt gebruikt om Near Earth Object (NEO) gegevens op te halen van de NASA NeoWs API.

    Attributen
    ----------
    api_key : str
        De API-sleutel die wordt gebruikt om te authenticeren bij de NASA NeoWs API.
    url : str
        De basis-URL voor de NASA NeoWs feed API.

    Methodes
    -------
    fetch_data(start_date=None, end_date=None):
        Haalt NEO-gegevens op van de NASA NeoWs API binnen een opgegeven datumbereik.
    """

    def __init__(self, api_key):
        """
            Initialiseert de NEODataExtractor met de opgegeven NASA API-sleutel.

            Parameters
            ----------
            api_key : str
                De API-sleutel om te authenticeren bij de NASA NeoWs API.
        """
        self.api_key = api_key
        self.url = 'https://api.nasa.gov/neo/rest/v1/feed'

    def fetch_data(self, start_date=None, end_date=None):
        if not start_date:
            start_date = datetime.now() - timedelta(days=7)
        if not end_date:
            end_date = datetime.now()

        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        params = {
            'start_date': start_date_str,
            'end_date': end_date_str,
            'api_key': self.api_key
        }

        response = requests.get(self.url, params=params)
        if response.status_code == 200: # 200 indicates succes
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")
