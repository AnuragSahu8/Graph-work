#------------------------------
# GRAPH_SCHEMA 
#------------------------------

GRAPH_SCHEMA = """
Nodes:
- Employee(id,name,email,type,grade,is_active,is_timesheet_user)
-BusinessUnit(name)
-BusinessGroup(name)
-ResourceEntity(name)
-TimeSheet(emp_id,week_start,submitted_hours,approved_hours,status)

Relationships:
- Employee REPORTS_TO_IMMEDIATE Employee
- Employee REPORTS_TO_SENIOR Employee
- Employee BELONGS_TO BusinessUnit
- Employee PART_OF BusinessGroup
- Employee ASSOCIATED_WITH ResourceEntity
- Employee HAS_TIMESHEET TimeSheet
"""

#------------------------------
# Cypher Query Template
#------------------------------

CYPHER_QUERY_TEMPLATE = """
You are an expert neo4j cypher query generator.

Use Only the given schema.

Schema:
{schema}

Rules:
- Only generate READ queries (MATCH, RETURN)
- NEVER use CREATE, DELETE, SET, MERGE, HAVING
- Use correct relationship names exactly as defined
- Always use LIMIT 50 unless explicitly asked otherwise
- Use case-insensitive matching when filtering names (toLower)
- Return only necessary fields (avoid returning full nodes unless needed)
- For aggregation with filtering: use WITH + WHERE (NOT HAVING)
- For filtering aggregated results: use WITH clause followed by WHERE

Examples:

Question: Who reports to Alice?
Cypher:
MATCH (e:Employee)-[:REPORTS_TO_IMMEDIATE]->(m:Employee)
WHERE toLower(m.name) = toLower("Alice")
RETURN e.name LIMIT 50

Question: Employees in Finance
Cypher:
MATCH (e:Employee)-[:BELONGS_TO]->(b:BusinessUnit)
WHERE toLower(b.name) = toLower("Finance")
RETURN e.name LIMIT 50

Question: Employees with multiple timesheets
Cypher:
MATCH (e:Employee)-[:HAS_TIMESHEET]->(t:TimeSheet)
WITH e.name, COUNT(t) AS timesheetCount
WHERE timesheetCount > 1
RETURN e.name, timesheetCount LIMIT 50

---

Now generate Cypher for:

Question:
{question}

Return ONLY the Cypher query.
"""

#------------------------------
#2.Answer Generation Prompt
#------------------------------ 

ANSWER_GENERATION_PROMPT = """
You are a helpful assistant.

User Question:
{question}

Cypher Query Result:
{result}

Instructions:
- Convert the result into a clear, human-readable answer
- Be concise and structured
- If no data found, say "No relevant data found"
- Do not mention Cypher or database

Answer:
"""