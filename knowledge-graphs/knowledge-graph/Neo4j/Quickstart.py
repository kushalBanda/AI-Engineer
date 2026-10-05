import os
from config import Config
from neo4j import GraphDatabase
config = Config()

# Neo4j
NEO4J_URI = config.neo4j_uri
NEO4J_PASSWORD = config.neo4j_password
NEO4J_USERNAME = config.neo4j_username
NEO4J_DATABASE = config.neo4j_database
AURA_DS = config.aura_instance_id

# AI
LLM = config.model
os.environ['OPENAI_API_KEY'] = config.openai_api_key
OPENAI_API_KEY = config.openai_api_key


URI = NEO4J_URI
AUTH = (NEO4J_USERNAME, NEO4J_PASSWORD)


with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

    summary = driver.execute_query("""
    CREATE (a:Person {name: $name})
    CREATE (b:Person {name: $friendName})
    CREATE (a)-[:KNOWS]->(b)
    """,
    name="Alice", friendName="David",
    database_=config.neo4j_database,
).summary
print("Created {nodes_created} nodes in {time} ms.".format(
    nodes_created=summary.counters.nodes_created,
    time=summary.result_available_after
))



records, summary, keys = driver.execute_query("""
    MATCH (p:Person)-[:KNOWS]->(:Person)
    RETURN p.name AS name
    """,
    database_=config.neo4j_database,
)

# Loop through results and do something with them
for record in records:
    print(record.data())  # obtain record as dict

# Summary information
print("The query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records),
    time=summary.result_available_after
))