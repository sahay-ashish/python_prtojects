import pymysql
import os
import pandas as pd

mydb_connection = pymysql.connect(
    host = "localhost",
    user="root",
    password="Ashish@12",
    database="ashish"
    )

select_query = """
    select * from emp
    where emp_department = 'IT'
"""

mycursor = mydb_connection.cursor()

try:
    if mydb_connection.open:
        print("connected to database")

    mycursor = mydb_connection.cursor()
    mycursor.execute(select_query)

    rows=mycursor.fetchall()

    Columns=['emp_id', 'emp_name', 'emp_age', 'emp_department', 'emp_salary', 'emp_join_date']
    #print(type(rows))
    #print("----------------------------------------------------------------------")
    #print(rows)
    df = pd.DataFrame(rows, columns=Columns)
    df.to_csv('employee.csv', index=False)

    df_text = df.describe()

    with open ('employee.txt', 'w') as file:
        file.write(df.to_string())

except mydb_connection.Error as err:
    print(f"Error : {err}")

finally:
    mycursor.close()
    print("closing mysql-cursor")
    mydb_connection.close()
    print("closing mysql-connection")
