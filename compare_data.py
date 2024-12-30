import pymysql
import pandas as pd

client_data = pd.read_csv('client_data.csv')
vendor_data = pd.read_csv('vendor_data.csv')

print(type(client_data))

client_data = client_data[['emp_id','emp_name','emp_age','emp_department','emp_salary','emp_join_date']]
vendor_data = vendor_data[['emp_id','emp_name','emp_age','emp_department','emp_salary','emp_join_date']]

merged_data = pd.merge(client_data, vendor_data, on = 'emp_id', how ='outer', suffixes = ('_client', '_vendor'))

#print('--------------------------------------------------------------------------------------')
#print(merged_data)
#print('--------------------------------------------------------------------------------------')

difference = merged_data[
             (merged_data['emp_name_client'] != merged_data['emp_name_vendor']) |
             (merged_data['emp_age_client'] != merged_data['emp_age_vendor']) |
             (merged_data['emp_department_client'] != merged_data['emp_department_vendor']) |
             (merged_data['emp_salary_client'] != merged_data['emp_salary_vendor']) |
             (merged_data['emp_join_date_client'] != merged_data['emp_join_date_vendor']) 
        ]

if not difference.empty:
    difference.to_csv('difference_report.csv', index = False)
    print('Difference found and report is generated \n')
    with open ('difference.txt','w') as file:
        file.write(difference.to_string())

else:
    print('No difference found')
