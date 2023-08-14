import os
import sys
import mysql.connector
from dotenv import load_dotenv
load_dotenv()


current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '..', 'circles_local_database_python')
sys.path.append(src_path)


class SqlMethods:

    def __init__(self):
        pass

    @staticmethod
    def get_user_by_id(table_name: str, id: str, id_col_name=""):
        try:
            connection = mysql.connector.connect(
                host=os.getenv("RDS_HOSTNAME"),
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                database= os.getenv("RDS_DB_NAME"),
            )
        except Exception as e: 
            return {'message': "error: connection to the database failed"}
            
        cursor = connection.cursor()
        try:
            cursor.execute(f"USE {table_name}")
            if id_col_name == "":
                cursor.execute(f"SELECT * FROM {table_name}")
            else:
                cursor.execute(f"SELECT * FROM {table_name} WHERE {id_col_name} = {id}")
            result = cursor.fetchall()
            connection.close()
            cursor.close()
            return result
        except Exception as e:
            return {'error': str(e)}

    # Get all users using specific filters for the where clause
    @staticmethod
    def dynamic_get(table_name: str, where_cond: str = ""):
        """
        This method returns all the data from the database.
        :param table_name: The name of the table to get the data from.
        :param where_cond: The condition to filter the data.
        :return: The data from the database.
        """
        try:
            connection = mysql.connector.connect(
                host=os.getenv("RDS_HOSTNAME"),
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                database= os.getenv("RDS_DB_NAME"),
            )
        except Exception as e: 
            return {'message': "error: connection to the database failed"}
            
        cursor = connection.cursor()
        try:
            cursor.execute(f"USE {table_name}")
            if where_cond == "":
                cursor.execute(f"SELECT * FROM {table_name}")
            else:
                cursor.execute(f"SELECT * FROM {table_name} WHERE {where_cond}")
            result = cursor.fetchall()
            connection.close()
            cursor.close()
            return result
        except Exception as e:
            return {'error': str(e)}

#Create contact
    # Route to add a new contact to the database
    @staticmethod
    def insert(table_name: str, json_data=None):
        try:
            connection = mysql.connector.connect(
                host=os.getenv("RDS_HOSTNAME"),
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                database= os.getenv("RDS_DB_NAME"),
            )
        except Exception as e: 
            return {'message': "error: connection to the database failed"}
        
        cursor = connection.cursor()
        added_ids=[]

        try:
            cursor.execute(f"USE {table_name}")
            if not json_data:
                return {'message': 'No data provided'}
    
            # Extract the data from the json
            for row, data in json_data.items():
                for param in data:
                    keys = ','.join(param.keys())
                    values = ['"{}"'.format(y) for y in param.values()]
                    values = ','.join(values)
                    query = f"INSERT INTO {table_name} ({keys}) VALUES ({values})" 
                    cursor.execute(query)
                    added_ids.append(cursor.lastrowid)
            #close connectin
            connection.commit()
            connection.close()
            cursor.close()
            return {'message': 'Contacts added successfully', 'contacts ids': added_ids}
        except Exception as e:
            return {'error': str(e)}
         
    @staticmethod     
    def update(table_name, json_data):
        try:
            connection = mysql.connector.connect(
                host=os.getenv("RDS_HOSTNAME"),
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                database= os.getenv("RDS_DB_NAME"),
            )
        except Exception as e: 
            return {'message': "error: connection to the database failed"}

        cursor = connection.cursor()
        updated_ids=[]
        try:
            cursor.execute(f"USE {table_name}")
            if not json_data:
                return {'message': 'No data provided'}
            
            # Extract the data from the json
            for row, data in json_data.items():
                for param in data:
                    keys = ','.join(param.keys())
                    values =['"{}"'.format(y) for y in param.values()]
                    values=','.join(values)
                    query=f" UPDATE {table_name} SET {keys} = {values} WHERE id = {param['id']}"
                    cursor.execute(query)
                    updated_ids.append(cursor.lastrowid)
            #close connectin
            connection.commit()
            connection.close()
            cursor.close()
            return {'message': 'Contacts updated successfully', 'contacts ids': updated_ids}
        except Exception as e:
            return {'error': str(e)}

    # The delete method updates the end_timestamp column with the current timestamp for the given id
    @staticmethod
    def delete(table_name, json_data):
        try:
            connection = mysql.connector.connect(
                host=os.getenv("RDS_HOSTNAME"),
                user=os.getenv("RDS_USERNAME"),
                password=os.getenv("RDS_PASSWORD"),
                database= os.getenv("RDS_DB_NAME"),
            )
        except Exception as err: 
            return {'message': "erro : connection to the database filed"}
           
        cursor = connection.cursor()
        deleted_ids=[]
        try:
            cursor.execute("USE end_timestamp")
            if not json_data:
                return {'message': 'No data provided'}
            user_id = json_data['id']
            query = f"INSERT INTO {table_name} end_timestanp VALUES (NOW()) WHERE id = {user_id};"
            cursor.execute(query)
            deleted_ids.append(cursor.lastrowid)
            connection.commit()
            connection.close()
            cursor.close()
            return {'message': 'Contacts deleted successfully', 'contacts ids': deleted_ids}
        except Exception as e:
            return {'error': str(e)}
