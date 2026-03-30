from src.db.neo4j_client import Neo4jClient


def ingest_data(df):
    client = Neo4jClient()

    query = """
    UNWIND $rows as row
    
    MERGE (e:Employee {id: row.emp_id})
    SET e.name = row.name,
        e.email = row.email,
        e.type = row.type,
        e.grade = row.grade,
        e.is_active = row.is_active,
        e.is_timesheet_user = row.is_ts_user

    MERGE (m1:Employee {name: row.manager})
    MERGE (m2:Employee {name: row.senior_manager})

    MERGE (e)-[:REPORTS_TO_IMMEDIATE]->(m1)
    MERGE(e)-[:REPORTS_TO_SENIOR]->(m2)

    MERGE (bu:BusinessUnit {name: row.bu})
    MERGE (bg:BusinessGroup {name: row.bg})
    MERGE (re:ResourceEntity {name: row.re})

    MERGE (e)-[:BELONGS_TO]->(bu)
    MERGE (e)-[:PART_OF]->(bg)
    MERGE (e)-[:ASSOCIATED_WITH]->(re)

    MERGE (t:TimeSheet {
    emp_id: row.emp_id,
    week_start: row.week})
    SET t.submitted_hours = row.submitted,
        t.approved_hours = row.approved,
        t.status = row.status

    MERGE (e)-[:HAS_TIMESHEET]->(t)
    """

    batch_size = 1000
    rows = []
    for i,(_,row) in enumerate(df.iterrows(),start = 1):

        rows.append({
            "emp_id": int(row['Employee']),
            "name": row['Employee Name'],
            "email": row['Email'],
            "type": row['Employee Type'],
            "grade": row['Grade'],
            "is_active": bool(row['Resource Is Active']),
            "is_ts_user": bool(row['SN Timesheet Users']),

            "manager": row['Immediate Reporting Manager'],
            "senior_manager": row['Senior Reporting Manager'],

            "bu": row['Parent Business Unit'],
            "bg": row['Parent Business Group'],
            "re": row['Resource Entity'],

            "week": row['Week Start On'].strftime('%Y-%m-%d'),
            "submitted": row['Total Submitted Hours'],
            "approved": row['Approved Hours'],
            "status": row['Time Sheet State']

        })

        if len(rows) == batch_size:
            client.execute_write(query,parameters = {'rows': rows})
            print(f"Inserted batch up to row {i}")
            rows = []

    # Insert remaining rows
    if rows:
        client.execute_write(query,{'rows': rows})
        print(f"Inserted final batch")

    client.close()

    print('Data Ingestion completed successfully.')

        
        

