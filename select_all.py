import pymysql
import pandas as pd

mydb_connection = pymysql.connect(
        user = 'root',
        password = 'Ashish@12',
        host = 'localhost',
        database = 'ashish'
        )

select_all_query = """ 
    select * from emp
"""

try:
    if mydb_connection.open:
        print("connected to mysql")

    mycursor = mydb_connection.cursor()
    
    mycursor.execute(select_all_query)
    rows = mycursor.fetchall()
    Columns=['emp_id', 'emp_name', 'emp_age', 'emp_department', 'emp_salary', 'emp_join_date']

    df = pd.DataFrame(rows, columns=Columns)
    df.to_csv('employees_total.csv', index=False)

    with open ('employees_total.txt','w') as file:
        file.write(df.to_string())

except mydb_connection.Error as err:
    print(f"connection error : {err}")

finally:
    mycursor.close()
    mydb_connection.close()

