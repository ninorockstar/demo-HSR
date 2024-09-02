import pandas as pd
class NEODataTransformer:
    @staticmethod
    def transform(data):
        neo_list = []
        for date in data['near_earth_objects']:
            for neo in data['near_earth_objects'][date]:
                neo_data = {
                    'name': neo['name'],
                    'date': date,
                    'estimated_diameter_min_meters': neo['estimated_diameter']['meters']['estimated_diameter_min'],
                    'estimated_diameter_max_meters': neo['estimated_diameter']['meters']['estimated_diameter_max'],
                    'miss_distance_kilometers': neo['close_approach_data'][0]['miss_distance']['kilometers'],
                    'relative_velocity_kmph': neo['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
                }
                neo_list.append(neo_data)

        return pd.DataFrame(neo_list)