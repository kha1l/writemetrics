from dotenv import load_dotenv
import os


class Config:
    load_dotenv()
    dbase = os.getenv('DATA_BASE')
    user = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    host = os.getenv('IP')
    sheet_day = os.getenv('SHEET_DAY')
    sheet_week = os.getenv('SHEET_WEEK')
    sheet_month = os.getenv('SHEET_MONTH')
    table_ptf = os.getenv('TABLE_PTF')
    table_pyt = os.getenv('TABLE_PYT')
    table_msk = os.getenv('TABLE_MSK')
    table_kor = os.getenv('TABLE_KOR')
    table_spg = os.getenv('TABLE_SPG')
    table_omk = os.getenv('TABLE_OMK')
    table_vkz = os.getenv('TABLE_VKZ')
    table_vrs = os.getenv('TABLE_VRS')
    table_zel = os.getenv('TABLE_ZEL')


