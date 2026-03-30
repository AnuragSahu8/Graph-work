from langchain_neo4j import Neo4jGraph
from src.graphrag.config import get_neo4j_config

def get_graph():
    config = get_neo4j_config()
    graph = Neo4jGraph(
       url = config['uri'],
       username = config['user'],
       password = config['password'],
    )

    return graph


