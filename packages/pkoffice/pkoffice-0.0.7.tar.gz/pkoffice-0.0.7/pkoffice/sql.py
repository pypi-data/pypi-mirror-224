import sqlalchemy as sql
import pandas as pd
import numpy as np
from typing import Literal
from datetime import datetime


class SqlDB:
    """
    Class to manage sql database connection.
    """
    def __init__(self, server: str, database: str, driver: str):
        self.engine = sql.create_engine(f"mssql+pyodbc://{server}/"
                                        f"{database}?driver={driver}",
                                        fast_executemany=True)
        self.process_time_beg = datetime.now()
        self.process_time_end = datetime.now()
        self.df = None

    def download_data(self, query: str) -> pd.DataFrame:
        """
        Method to download data from database according to provided query.
        :param query: SQL query in string format
        :return: pandas.Dataframe
        """
        with self.engine.begin() as conn:
            return pd.read_sql(sql=sql.text(query), con=conn)

    def execute_query(self, query: str) -> None:
        """
        Method to execute query
        :param query: SQL query in string format
        :return: None
        """
        with self.engine.begin() as conn:
            conn.execute(sql=sql.text(query))

    def upload_data(self, df: pd.DataFrame, table_name: str, chunksize: int,
                    if_exists: Literal["new", "replace", "append"] = 'replace') -> None:
        """
        Method to upload pandas dataframe to database.
        :param df: pandas dataframe with data to upload
        :param table_name: name of table without []
        :param chunksize: size of single batch to upload
        :param if_exists: replace - drop/create, append - insert at the end,
               new - delete and insert
        :return: None
        """
        if if_exists == 'new':
            with self.engine.begin() as conn:
                conn.execute(sql=sql.text(f'Delete from dbo.[{table_name}]'))
            df.to_sql(table_name, con=self.engine, if_exists='append',
                      index=False, chunksize=chunksize, method='multi', schema='dbo')
        else:
            df.to_sql(table_name, con=self.engine, if_exists=if_exists,
                      index=False, chunksize=chunksize, method='multi', schema='dbo')
        self.process_time_end = datetime.now()
        self.df = df

    def process_parameters(self):
        """
        Method to return main process parameters.
        :return: [process date, process time, process duration,
                  dataframe records]
        """
        return [self.process_time_beg.strftime("%Y-%m-%d"),
                self.process_time_beg.strftime("%H:%M:%S"),
                (self.process_time_end - self.process_time_beg).seconds,
                self.df.count().max()]

    def upload_log(self, table_name: str, log_value: list) -> None:
        """
        Method to upload log to database.
        :param table_name: log table name in SQL database
        :param log_value: list of variables to upload to log table
        :return: None
        """
        self.process_time_end = datetime.now()
        sql_values = [f"'{x}'" if type(x) == str else str(x) for x in log_value]
        sql_values = ','.join(sql_values)
        with self.engine.begin() as conn:
            conn.execute(
                f"""Insert into {table_name}
                Values ({sql_values})""")


def columns_str_max_len(df: pd.DataFrame) -> list:
    """
    Function to return max length of string columns multiply by 1.5.
    :param df: dataframe which will be uploaded to database
    :return: list with max string length to set in database
    """
    col_string = [i for i in df if df[i].dtype == 'object']
    df[col_string] = df[col_string].astype('string')
    df_col_max_len = [{i: np.round(1.5 * df[i].str.len().max())} for i in col_string]
    return df_col_max_len