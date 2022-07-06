from authorization.authorize import Auth
from postgresql.psql import Database
import time


def writer(group, tps):
    db = Database()
    auth = Auth(group, tps)
    auth.get_df()
    users = db.get_users(group)
    for user in users:
        df = auth.df.loc[auth.df['pizzeriaID'] == user[1]]
        metrics = df['NameMetrics'].tolist()
        columns = ', '.join(metrics)
        auth.workbook(columns, user[0], user[1])
        print(user[0])
        time.sleep(5)
