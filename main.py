import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = '1234'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = 'company'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

# Create an engine
engine = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
df_sql = pd.read_sql('SELECT * FROM employee', engine)
print('--------------------------------------------------------------')
# Correct the file path for CSV
department_df = pd.read_csv(r'C:\Users\CVR\Desktop\6626\departments.csv')
project_df=pd.read_excel(r'C:\Users\CVR\Desktop\6626\projects.ods')
# Display the DataFrame from MySQL
print("sample reading of data from mysql")
print("Data from MySQL:")
print(df_sql)

# Perform the merge using 'id' from MySQL and 'student_id' from the CSV file
merged_df = pd.merge(df_sql, department_df,on='id', how='outer') #always try to take outer join
merged_dff = pd.merge(df_sql, project_df,on='id', how='outer') #always try to take outer join
# Display the merged DataFrame
print("Merged DataFrame of sql and csv:")
print(merged_df)
print('------------------------------------------------------------------')
print("Merged DataFrame of sql and excel:")
print(merged_dff)
print('----------------------------------------------------------------')
#print datatypes
print(department_df.dtypes)
#memory usage
print("memory usage")
print(department_df.memory_usage(deep=True))
print('----------------------------------------------------------------')
#convert one to int16
print('int64 to int16')
department_df['id']=department_df['id'].astype(np.int16)
print(department_df.memory_usage(deep=True))
print(department_df.dtypes)
print('------------------------------------------------')
#memory saving: int16 takes 2 bytes and int64 takes 8 bytes
#float to int try to do only when necessary and object to category
print('float to int')
print("BEFORE")
print(project_df.dtypes)
print(project_df.memory_usage(deep=True))
print("AFTER")
project_df['manager_sal']=project_df['manager_sal'].astype(np.int64)
print(project_df.memory_usage(deep=True))
print(project_df.dtypes)
print('----------------------------------------------------------')
print('object to categorical')
print("BEFORE")
print(project_df.dtypes)
print(project_df.memory_usage(deep=True))
print("AFTER")
project_df['project_name'] = project_df['project_name'].astype('category')
print(project_df.memory_usage(deep=True))
print(project_df.dtypes)
print('----------------------------------------------------------')