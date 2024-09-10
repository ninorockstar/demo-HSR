from datetime import datetime, timedelta
import requests


class NEODataExtractor:
    """
    Een klasse die wordt gebruikt om Near Earth Object (NEO) gegevens op te halen van de NASA NeoWs API.

    Attributen
    ----------
    api_key: str
        De API-sleutel die wordt gebruikt om te authenticeren bij de NASA NeoWs API.
    URL: str
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
        """
        Haalt gegevens op van een externe API binnen een opgegeven datumbereik.

        Deze functie haalt gegevens op van een opgegeven URL door een HTTP GET-verzoek te doen,
        met gebruik van de verstrekte API-sleutel en het opgegeven datumbereik.
        Als er geen start- of einddatum wordt opgegeven, haalt de functie standaard gegevens op voor de laatste 7 dagen.

        Args:
            start_date (datetime, optioneel): De begindatum voor het ophalen van gegevens. Standaard is 7 dagen geleden.
            end_date (datetime, optioneel): De einddatum voor het ophalen van gegevens. Standaard is de huidige datum.
        Returns:
            dict: De opgehaalde gegevens in JSON-formaat als het verzoek succesvol is.
        Raises:
            Exception: Als het ophalen van gegevens mislukt (geen statuscode 200).
        """
        if not start_date:
            start_date = datetime.now() - timedelta(days=7)
        if not end_date:
            end_date = datetime.now()

        # Zet data in het juiste format.
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        params = {
            'start_date': start_date_str,
            'end_date': end_date_str,
            'api_key': self.api_key
        }
        #   Data van 1 week dus in het object.
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")
