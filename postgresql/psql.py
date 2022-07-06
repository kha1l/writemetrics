import psycopg2
from config.conf import Config
from datetime import date


class Database:
    @property
    def connection(self):
        cfg = Config()
        return psycopg2.connect(
            database=cfg.dbase,
            user=cfg.user,
            password=cfg.password,
            host=cfg.host,
            port='5432'
        )

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def get_users(self, group: str):
        sql = '''
            SELECT restName, restId 
            FROM settings 
            WHERE restGroup=%s
            order by restId;
        '''
        parameters = (group,)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def get_metrics(self, col, dt: date, rest_id: int, table: str):
        sql = f'SELECT {col} FROM {table} WHERE ordersDay=%s AND restId=%s'
        parameters = (dt, rest_id)
        return self.execute(sql, parameters, fetchall=True)
