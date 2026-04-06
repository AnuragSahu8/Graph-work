from src.ingestion.loader import load_data
from src.ingestion.config import DATA_PATH
from src.ingestion.transformer import clean_dataframe
from src.ingestion.ingest import ingest_data

def main():
    # Step 1: Load the data
    print("Step 1: Loading data...")
    df = load_data(DATA_PATH,sheet_name='Sheet1')


    # Step 2: Clean the data
    print("Step 2: Cleaning data...")
    df = clean_dataframe(df)

    # print('Cleaned Data Preview')
    # print(df.head())
    
    # Step 3: Ingest the data into Neo4j
    print("Step 3: Ingesting data into Neo4j...")
    ingest_data(df)



    

if __name__ =="__main__":
    main()