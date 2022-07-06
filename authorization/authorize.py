import requests.exceptions
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from config.conf import Config
from gspread_dataframe import get_as_dataframe
from datetime import datetime, time, timedelta, date
from date_work import DataWork
from postgresql.psql import Database
import decimal
from gspread.utils import rowcol_to_a1


class Auth:
    cfg = Config()
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        './config/writer.json',
        scopes=scopes
    )
    clients = {
        'vkus': cfg.table_ptf,
        'korsakov': cfg.table_kor,
        'south': cfg.table_pyt,
        'msk-sch': cfg.table_msk,
        'sergpas': cfg.table_spg,
        'omsk': cfg.table_omk,
        'vkz': cfg.table_vkz,
        'veris': cfg.table_vrs,
        'zelen': cfg.table_zel
    }
    sheet_name = {
        'day': cfg.sheet_day,
        'week': cfg.sheet_week,
        'week2': cfg.sheet_week,
        'month': cfg.sheet_month
    }
    df = None
    dt = None
    tps = None

    def __init__(self, group: str, tps: str):
        self.gsc = gspread.authorize(self.credentials)
        self.sheet = self.gsc.open_by_key(self.clients[group])
        self.gt = self.sheet.worksheet(self.sheet_name[tps])
        self.tps = tps

    def get_df(self):
        df = get_as_dataframe(self.gt)
        self.df = df.dropna(subset=['NameMetrics'])
        if self.tps == 'week2':
            self.dt = DataWork().set_date() - timedelta(days=3)
            dt = datetime.strftime(self.dt, "%d.%m.%y")
        elif self.tps == 'month':
            self.dt = DataWork().set_date()
            dt = 'июн. 22'
        else:
            self.dt = DataWork().set_date()
            dt = datetime.strftime(self.dt, "%d.%m.%y")
        cell_col = self.gt.find(dt)
        if cell_col is None:
            self.gt.add_cols(1)
            self.gt.update_cell(1, df.shape[1] + 1, dt)

    def workbook(self, col: str, name: str, rest_id: int):
        total_metrics = list()
        db = Database()
        if self.tps == 'week2':
            metrics = db.get_metrics(col, self.dt, rest_id, 'week')
        else:
            metrics = db.get_metrics(col, self.dt, rest_id, self.tps)
        try:
            metrics = metrics[0]
            for i in metrics:
                if isinstance(i, time):
                    i = DataWork.change_time(i)
                    total_metrics.append([i])
                elif isinstance(i, decimal.Decimal):
                    i = float(i)
                    total_metrics.append([i])
                elif isinstance(i, timedelta):
                    i = DataWork.change_timedelta(i)
                    total_metrics.append([i])
                elif isinstance(i, date):
                    i = DataWork.change_date(i)
                    total_metrics.append([i])
                else:
                    total_metrics.append([i])
            cell_row = self.gt.find(name)
            if self.tps == 'month':
                cell_col = self.gt.find('июн. 22')
            else:
                cell_col = self.gt.find(datetime.strftime(self.dt, '%d.%m.%y'))
            try:
                cell_start = rowcol_to_a1(cell_row.row + 1, cell_col.col)
                cell_end = rowcol_to_a1(cell_row.row + 1 + len(metrics), cell_col.col)
                params = {'valueInputOption': 'USER_ENTERED'}
                body = {'values': total_metrics}
                try:
                    self.sheet.values_update(f'{self.sheet_name[self.tps]}!{cell_start}:{cell_end}', params, body)
                except requests.exceptions.InvalidJSONError:
                    pass
            except AttributeError:
                pass
        except IndexError:
            pass
