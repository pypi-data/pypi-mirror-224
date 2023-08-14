import os
from dotenv import load_dotenv
from timeout_decorator import timeout
from requests.exceptions import RequestException

import pandas as pd
import pymysql
from pyArango.connection import Connection

# ============================================================
# Config Do not Touch
# ============================================================
CONNECTION_TIMEOUT = 10 # Max time in second if we can't connect to DB

# Get the current directory of the script (package directory)
package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Navigate to the credentials directory inside the package
credentials_dir = os.path.join(package_dir, 'credentials')

# Load environment variables from the login_credentials.env file
env_file_path = os.path.join(credentials_dir, 'login_credentials.env')
load_dotenv(dotenv_path=env_file_path)
# ============================================================
# Functions
# ============================================================

class MySQLConnection:
    """
    A class to handle the MySQL database connection and queries.

    Attributes:
        host (str): The host IP or domain name for the MySQL server.
        port (int): The port number for the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password associated with the username.
        database_name (str): The name of the database to connect to.
        connection (pymysql.connections.Connection): The MySQL connection object.

    Methods:
        __init__(self, host, port, user, password, database_name):
            Initializes the MySQLConnection object with the provided connection details.

        connect(self):
            Establishes a connection to the MySQL database.

        close(self):
            Closes the MySQL database connection.

        query(self, sql):
            Executes a SQL query on the connected MySQL database and returns the result as a pandas DataFrame.
    """

    def __init__(self, database_name):
        """
        Initializes the MySQLConnection object with the provided connection details.

        Args:
            host (str): The host IP or domain name for the MySQL server.
            port (int): The port number for the MySQL server.
            user (str): The username to connect to the MySQL server.
            password (str): The password associated with the username.
            database_name (str): The name of the database to connect to.
        """
        self.host = os.path.join(package_dir, 'mysql_config_ip_host')
        self.port = os.path.join(package_dir, 'mysql_config_ip_port')
        self.user = os.path.join(package_dir, 'mysql_config_user_name')
        self.password = os.path.join(package_dir, 'mysql_config_user_password')
        self.database_name = database_name
        self.connection = None

    @timeout(CONNECTION_TIMEOUT)
    def connect(self):
        """
        Establishes a connection to the MySQL database.

        Raises:
            ConnectionError: If there is an error connecting to the MySQL database.
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database_name
            )
            print("Successfully connected to {} database".format(self.database_name))
        except Exception as e:
            raise ConnectionError("Connection error: " + str(e))

    def close(self):
        """
        Closes the MySQL database connection.
        """
        if self.connection:
            self.connection.close()

    def query(self, sql):
        """
        Executes a SQL query on the connected MySQL database and returns the result as a pandas DataFrame.

        Args:
            sql (str): The SQL query to be executed.

        Returns:
            pd.DataFrame: A DataFrame containing the result of the SQL query.

        Raises:
            ConnectionError: If the connection to the MySQL database is not established.
            ValueError: If there is an error executing the SQL query.
        """
        if not self.connection:
            raise ConnectionError("Not connected to the database.")

        try:
            query_result = pd.read_sql(sql, self.connection)
        except Exception as e:
            raise ValueError("Error executing the query: " + str(e))

        return query_result
    
    def show_example(self):
        """
        Display the usage of this Class
        """
        information = """
        #=========================================================
        # Usage Example
        #=========================================================
        host = os.getenv("mysql_config_ip_host")
        port = int(os.getenv("mysql_config_ip_port"))
        user = os.getenv("mysql_config_user_name")
        password = os.getenv("mysql_config_user_password")
        # option gateway / invoicer / payment, select only 1
        database_name = os.getenv("mysql_config_dbname_gateway")
        database_name = os.getenv("mysql_config_dbname_invoicer")
        database_name = os.getenv("mysql_config_dbname_payment")

        # Create an instance of the MySQLConnection class
        connection = MySQLConnection(host, port, user, password, database_name)

        try:
            # Connect to the database
            connection.connect()

            # Perform your queries
            sql_query = "<insert your query codes>"
            result = connection.query(sql_query)

            # Do something with the query result (e.g., print or process data)
            print(result)

        except Exception as e:
            print("Error:", str(e))
        finally:
            # Don't forget to close the connection when you're done
            connection.close()
                    """
        print(information)

class ArangoDBConnection:
    """
    A class to handle the connection to ArangoDB and perform queries.

    Attributes:
        arango_url (str): The URL of the ArangoDB server.
        username (str): The username to connect to the ArangoDB server.
        password (str): The password associated with the username.
        connection (pyArango.connection.Connection): The ArangoDB connection object.

    Methods:
        __init__(self, arango_url, username, password):
            Initializes the ArangoDBConnection object with the provided connection details.

        connect(self):
            Establishes a connection to the ArangoDB server.

        close(self):
            Closes the connection to the ArangoDB server.

        query(self, collection_name, query_codes):
            Executes an AQL query on a specific collection and returns the result as a DataFrame.
    """

    def __init__(self, arango_url, username, password):
        """
        Initializes the ArangoDBConnection object with the provided connection details.

        Args:
            arango_url (str): The URL of the ArangoDB server.
            username (str): The username to connect to the ArangoDB server.
            password (str): The password associated with the username.
        """
        self.arango_url = arango_url
        self.username = username
        self.password = password
        self.connection = None

    @timeout(CONNECTION_TIMEOUT)
    def connect(self):
        """
        Establishes a connection to the ArangoDB server.

        Raises:
            ConnectionError: If there is an error connecting to the ArangoDB server.
        """
        try:
            self.connection = Connection(arangoURL=self.arango_url,
                                         username=self.username, 
                                         password=self.password)
            print("Successfully connected to ArangoDB server.")
            return(self.connection)
        except RequestException as e:
            raise ConnectionError("Connection error: " + str(e))

    def close(self):
        """
        Closes the connection to the ArangoDB server.
        """
        if self.connection:
            self.connection.close()

    def query(self, collection_name, query_codes, batch_size = 100):
        """
        Executes an AQL query on a specific collection and returns the result as a DataFrame.

        Args:
            collection_name (str): The name of the ArangoDB collection to query.
            query_codes (str): The AQL query codes to be executed.
            batch_size (int): Total rows will be gathered, such as LIMIT 100

        Returns:
            pd.DataFrame: A DataFrame containing the result of the AQL query.

        Raises:
            ConnectionError: If the connection to the ArangoDB server is not established.
        """
        # Try to connect
        self.connect()
        collection_connection = self.connection[collection_name]
        # Config the connection
        query_result = collection_connection.AQLQuery(query_codes, batchSize=batch_size).response['result']
        return pd.DataFrame(query_result)
    
    def show_attributes(self):
        """
        Displays the values of the class attributes.
        """
        print("arango_url:", self.arango_url)
        print("username:", self.username)
        print("password:", self.password)
        print("connection:", self.connection)
    
    def show_example(self):
        """
        Display the usage of this Class
        """
        information = """# Usage example:
                    arango_url = os.getenv("arango_replicate_config_url")
                    username = os.getenv("arango_replicate_config_username")
                    password = os.getenv("arango_replicate_config_password")
                    collection_name = "<insert the collection name>" # For example: "paper_chain_document_flow"
                    aql_query = "<insert your query codes"

                    # Create an instance of the ArangoDBConnection class
                    arango_db = ArangoDBConnection(arango_url, username, password)
                    result_df = arango_db.query(collection_name, aql_query,batch_size = 5) # Show only 5
                    result_df
                    """
        print(information)