import pandas as pd

def clean_dataframe(df:pd.DataFrame)->pd.DataFrame:
    """
    Cleans the input DataFrame by performing the following operations:
    1. Strips leading and trailing whitespace from column names.
    2. Drop rows where empid is missing.
    3. Filling missing values with the "unknown" string.
    4. Drop Duplicates.
    """
    # Strip leading and trailing whitespace from column names
    df.columns = df.columns.str.strip()

    # Drop rows where empid is missing
    df = df.dropna(subset=['Employee'])

    # Convert Employee ID to int.
    df['Employee'] = df['Employee'].astype(int)

    # Fill missing values with "unknown"
    df['Immediate Reporting Manager'] = df['Immediate Reporting Manager'].fillna('Unknown')
    df['Senior Reporting Manager'] = df['Senior Reporting Manager'].fillna('Unknown')

    df['Parent Business Group'] = df['Parent Business Group'].fillna('Unknown')
    df['Parent Business Unit'] = df['Parent Business Unit'].fillna('Unknown')   
    df['Resource Entity'] = df["Resource Entity"].fillna('Unknown')

    df['Employee Type'] = df['Employee Type'].fillna('Unknown')
    df['Grade'] = df['Grade'].fillna('Unknown') 
    df['Email'] = df['Email'].fillna('Unknown') 

    # Drop duplicates
    df = df.drop_duplicates()

    print('Data cleaning completed.')
    print(f"Final Shape:{df.shape}")

    return df



    
    
    
   
    
    return df

