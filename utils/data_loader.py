# import pandas as pd

# def load_data(file_path):
#     """Load CSV/Excel files into DataFrame"""
#     try:
#         if file_path.name.endswith('.csv'):
#             return pd.read_csv(file_path)
#         elif file_path.name.endswith(('.xls', '.xlsx')):
#             return pd.read_excel(file_path)
#         else:
#             raise ValueError("Unsupported file format")
#     except Exception as e:
#         raise RuntimeError(f"Error loading file: {str(e)}")

# def clean_data(df):
#     """Basic data cleaning"""
#     try:
#         # Drop empty rows/columns
#         df = df.dropna(how='all').dropna(axis=1, how='all')
        
#         # Convert date columns
#         date_cols = [col for col in df.columns if 'date' in col.lower()]
#         for col in date_cols:
#             df[col] = pd.to_datetime(df[col], errors='coerce')
            
#         return df
#     except Exception as e:
#         raise RuntimeError(f"Data cleaning failed: {str(e)}")


import pandas as pd
import mysql.connector

def load_data(file_path):
    """Load CSV/Excel files into DataFrame"""
    try:
        if file_path.name.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.name.endswith(('.xls', '.xlsx')):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        raise RuntimeError(f"Error loading file: {str(e)}")

def load_data_from_mysql(host, user, password, database, table):
    """Load data from a MySQL database table into DataFrame"""
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        # Query the table
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, connection)
        
        # Close the connection
        connection.close()
        
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading data from MySQL: {str(e)}")

def clean_data(df):
    """Basic data cleaning"""
    try:
        # Drop empty rows/columns
        df = df.dropna(how='all').dropna(axis=1, how='all')
        
        # Convert date columns
        date_cols = [col for col in df.columns if 'date' in col.lower()]
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            
        return df
    except Exception as e:
        raise RuntimeError(f"Data cleaning failed: {str(e)}")