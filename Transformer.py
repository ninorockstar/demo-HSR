import pandas as pd
class NEODataTransformer:
    @staticmethod
    def transform(data):
        """
        Transforms the nested dictionary of near-Earth objects (NEO) data into a flat structure
        and returns a pandas DataFrame.
        Args:
            data (dict): The input data containing near-Earth objects with dates as keys
                         and a list of NEOs for each date.
        Returns:
            pd.DataFrame: A pandas DataFrame where each row represents a NEO and its relevant information.
        """
        neo_list = [
            {
                'name': neo['name'],
                'date': date,
                'estimated_diameter_min_meters': neo['estimated_diameter']['meters']['estimated_diameter_min'],
                'estimated_diameter_max_meters': neo['estimated_diameter']['meters']['estimated_diameter_max'],
                'miss_distance_kilometers': neo['close_approach_data'][0]['miss_distance']['kilometers'],
                'relative_velocity_kmph': neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
            }
            # Iterate through each date and associated NEOs in the 'near_earth_objects' dictionary
            for date, neos in data['near_earth_objects'].items()
            # Iterate through each NEO object for a given date
            for neo in neos
        ]
        return pd.DataFrame(neo_list)