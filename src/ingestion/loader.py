import pandas as pd


def load_data(file_path:str,sheet_name:str)->pd.DataFrame:
    """
    Loads data from an Excel file and returns it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.
    sheet_name (str): The name of the sheet to load.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print("Data loaded successfully")
        return df
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None