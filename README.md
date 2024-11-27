# PythonDatabaseConnector

A Python package for connecting to and querying databases (SQL Server and PostgreSQL).

## Installation

Install the package using Git:

```bash
git clone https://github.com/OHDSI-TAIWAN/PythonDatabaseConnector
cd PythonDatabaseConnector
pip install -r requirements.txt
pip install .
```

## Supported Features
* Connect to Microsoft SQL Server and PostgreSQL databases.
* Execute SQL queries and retrieve results as pandas DataFrames.
* Easily disconnect from the database.
* Compatible with macOS, Windows, and Ubuntu operating systems.

## Usage
### 1. Import the Package
```python
from PythonDatabaseConnector import PyDatabaseConnector
```
### 2. Connect to a Database
Example: Connect to a PostgreSQL Database
```python
connector = PyDatabaseConnector(
    dbms="postgresql",          # Specify the database type
    username="your_username",   # Your username
    password="your_password",   # Your password
    server="localhost",         # Database server address
    port="5432",                # Database port
    database="your_database"    # Database name
)
connector.connect()  # Establish the connection
```
Example: Connect to a SQL Server Database
```python
connector = PyDatabaseConnector(
    dbms="mssql",
    username="your_username",
    password="your_password",
    server="your_server_address",
    port="1433",  # Default port for SQL Server
    database="your_database"
)
connector.connect()
```
### 3. Execute SQL Queries
Use the execute_query method to run SQL commands. The results are returned as a pandas DataFrame.

Example: Fetch Data
```python
query = "SELECT * FROM your_table"
data = connector.execute_query(query)
print(data)
```
Example: Insert or Update Data
For non-select queries (e.g., INSERT, UPDATE, DELETE), you can use the same execute_query method. These operations return no results.

```python
query = """
INSERT INTO your_table (column1, column2)
VALUES ('value1', 'value2')
"""
connector.execute_query(query)
```
### 4. Disconnect from the Database
Always disconnect after completing your operations to free resources:

```python
connector.disconnect()
```
### 5. Handling Connection Errors
If the connection fails, the package will raise a ValueError or ConnectionError. Ensure you provide correct credentials and database details.

Example End-to-End Script
```python
from PythonDatabaseConnector import PyDatabaseConnector

# Connect to a PostgreSQL database
connector = PyDatabaseConnector(
    dbms="postgresql",
    username="user",
    password="pass",
    server="localhost",
    port="5432",
    database="mydb"
)

try:
    connector.connect()  # Establish connection
    query = "SELECT * FROM my_table"
    data = connector.execute_query(query)  # Execute query
    print("Fetched Data:")
    print(data)
finally:
    connector.disconnect()  # Disconnect safely
```
### Requirements
* Python 3.6 or higher
* pandas
* SQLAlchemy
* psycopg2-binary (for PostgreSQL)
* pymssql (for SQL Server)
### License
This package is licensed under the Apache 2.0 License. See the LICENSE file for details.