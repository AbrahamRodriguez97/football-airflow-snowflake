import pandas as pd
import os

def get_football_data(output_path):
    """
    Simulates data extraction from a soccer API and saves it as a CSV.
    :param output_path: Local path to store the temporary CSV file.
    """
    # Mock data representing top European leagues
    data = {
        'league_name': ['La Liga', 'Premier League', 'Serie A', 'Bundesliga', 'Ligue 1'],
        'country': ['Spain', 'England', 'Italy', 'Germany', 'France'],
        'season': [2024, 2024, 2024, 2024, 2024]
    }
    df = pd.DataFrame(data)
    
    # Ensure the directory exists to avoid FileNotFoundError
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save to CSV without headers to match Snowflake's COPY INTO command
    df.to_csv(output_path, index=False, header=False) 
    return output_path