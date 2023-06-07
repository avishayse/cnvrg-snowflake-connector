import snowflake.connector
import argparse
import csv

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Snowflake AI-Library connector')
parser.add_argument('--user', required=True, help='Snowflake username')
parser.add_argument('--password', required=True, help='Snowflake password')
parser.add_argument('--account', required=True, help='Snowflake account')
parser.add_argument('--database', required=True, help='Snowflake database')
parser.add_argument('--warehouse', required=True, help='Snowflake warehouse')
parser.add_argument('--schema', required=True, help='Snowflake schema')
parser.add_argument('--query', required=True, help='Snowflake query')
parser.add_argument('--output', required=True, help='Output CSV file name')
args = parser.parse_args()

# Establishing a connection
conn = snowflake.connector.connect(
    user=args.user,
    password=args.password,
    account=args.account,
    warehouse=args.warehouse,
    database=args.database,
    schema=args.schema
)

# Creating a cursor
cur = conn.cursor()

try:
    # Executing the query
    cur.execute(args.query)

    # Fetching all rows
    rows = cur.fetchall()

    # Writing results to CSV file
    with open(args.output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

    # Printing success message
    print(f"Query results exported to '{args.output}'")

except snowflake.connector.Error as e:
    # Handling any Snowflake-specific errors
    print("Error occurred while executing the query:", str(e))

finally:
    # Closing the cursor and connection
    cur.close()
    conn.close()