import warnings
from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from jose import jwt
from datetime import datetime
load_dotenv(find_dotenv())

connection_string = os.getenv("cockroack_db_connect_string")
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")

sql_engine = create_engine(connection_string)

def get_user_info():
    table_name = "jmstracker_dashboard_users"
    query = f"select * from {table_name}"
    # read in the data as a data frame based on the query and connection
    return pd.read_sql_query(query, sql_engine)

def get_user_password(username: str):
    df_sql = get_user_info()
    return df_sql.loc[df_sql["username"]==username, 
                      "password_hash"].iloc[0]

def add_unhash_password_column(data):
    def unhash(col):
        unhash_dict = jwt.decode(col, 
                                 SECRET_KEY, 
                                 algorithms=[ALGORITHM])
        return unhash_dict["password"]
    return data.assign(**{"password": 
                            lambda d: d["password_hash"]
                            .apply(unhash)})

def create_user(username: str,
                password: str):
    table_name = "jmstracker_dashboard_users"    
    comp_df = get_user_info()
    
    if username not in comp_df["username"].tolist():    
        token = jwt.encode({'password': password}, 
                        SECRET_KEY, 
                        algorithm=ALGORITHM)
        df = (pd.DataFrame({"created_at": str(datetime.now()), 
                            "username": username,
                            "password_hash": token},
                    index=[0])
        )
        df.to_sql(name=table_name,
            con=sql_engine,
            if_exists="append")
    else:
        warnings.warn("""
                      Warning: User already exists in SQL table
                      so was not created
                      """)