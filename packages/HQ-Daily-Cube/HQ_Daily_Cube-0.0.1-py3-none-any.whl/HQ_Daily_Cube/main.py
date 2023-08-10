import pymssql
import pandas as pd
import getpass
from datetime import datetime

def connect_to_db():
    return pymssql.connect(
        server="KFICWPNXDBSP01",
        user="t_board_db",
        password="planX2018",
        database="PlanX"
    )

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

def get_user_id():
    return getpass.getuser()

def check_permissions(conn, cursor, user_id, region_name):
    cursor.execute(f"SELECT * FROM sta.PowerBI_Users WHERE User_ID='{user_id}' and Region_Name = '{region_name}'")
    user = cursor.fetchone()

    Daily_cube = pd.DataFrame()

    if not user:
        Daily_cube['Permission'] = ["you don’t have permission to execute and getting the Data, Please contact hossam.ibrahim@hlag.com"]
    else:
        max_api_calls = user[3]
        
        # Check if the user has already called the API today
        cursor.execute(f"SELECT SUM(No_Of_Calls) FROM sta.PowerBI_Calls WHERE User_ID='{user_id}' AND Region_Name='{region_name}' AND DATEADD(dd, 0, DATEDIFF(dd, 0, Call_DateTime)) = DATEADD(dd, 0, DATEDIFF(dd, 0, GETDATE()))")
        calls_today = cursor.fetchone()[0] or 0

        if calls_today >= max_api_calls:
            Daily_cube['Permission'] = ["You are already exceeding your daily Calls, please try tomorrow or contact hossam.ibrahim@hlag.com"]
        else:
            Daily_cube = execute_stored_procedure(cursor, 'dbo.PowerBI_CL_Daily')

            # Record the API call
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(f"INSERT INTO sta.PowerBI_Calls (Region_Name, User_ID, Query_url, Call_DateTime, No_Of_Calls) VALUES ('{region_name}', '{user_id}', 'dbo.PowerBI_CL_Daily', '{current_time}', 1)")
            conn.commit()
    return Daily_cube

def execute_stored_procedure(cursor, procedure_name):
    cursor.execute(f"EXEC {procedure_name};")
    
    # Fetch all rows from the result of the procedure
    rows = cursor.fetchall()
    
    # Get column names from cursor.description
    columns = [column[0] for column in cursor.description]

    # Create a DataFrame from the rows and columns
    return pd.DataFrame(rows, columns=columns)

def main():
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            user_id = get_user_id()
            region_name = 'H.Q'
            Daily_cube = check_permissions(conn, cursor, user_id, region_name)
    return Daily_cube

def HQ_Daily_Cube():
    Daily_cube = main()
    return Daily_cube
