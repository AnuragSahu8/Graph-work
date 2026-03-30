from neo4j import GraphDatabase
import os 
from dotenv import load_dotenv

load_dotenv()

class Neo4jClient:
    def __init__(self):
        self.uri = os.getenv('NEO4J_URI')
        self.user = os.getenv('NEO4J_USERNAME')
        self.password = os.getenv('NEO4J_PASSWORD')

        print(self.uri,self.user,self.password)

        self.driver = GraphDatabase.driver(
            self.uri,
            auth = (self.user,self.password)
        )

    def close(self):
        self.driver.close()

    def execute_write(self,query,parameters = None):
        with self.driver.session() as session:
            session.execute_write(lambda tx: tx.run(query,parameters))
