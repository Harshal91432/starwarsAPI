import pymysql
import toml
import yaml
from pymysql.connections import Connection


_settings  = {}

def make_connection():
    try:
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='harsh_root',
                             port=3306,
                             database='starwarsDB')

    except pymysql.Error as ex:
        print(f"[ ERROR ] connection cannot successful - {ex}")

    return connection



def load_from_yaml():
    """pickes configuration from settings/secerets.yaml
    and store them into _global "_settings" variable"""



    global _settings

    with open("settings/secrets.yaml", "r") as fp:
        doc = yaml.load(fp, Loader=yaml.FullLoader)
        # conn = pymysql.connect(**doc)
        # return conn

    if not doc:
        return

    for key_, val_ in doc.items():
        _settings[key_] = val_


def get_db_con() -> Connection:
    """
    Makes actual DB connection
    Returns:

    """
    load_from_yaml()

    try:

        connection = pymysql.connect(**_settings)
    except pymysql.err.Error as ex:
        print(f"[ERROR ] cannot make connection {ex}")

    return connection


def get_db_con_toml():
    """pickes configuration from settings/secerets.toml"""


    with open('settings/secrets.toml', 'r') as fp:

        config = toml.load(fp)

        dbconfig = config.get("mysqldb")       # secerts.toml file only access mysqldb
        conn_ = pymysql.connect(**dbconfig)   # **kwargs dict value
        return conn_



if __name__ == "__main__":
    conn = make_connection()
    toml_conn = get_db_con_toml()
    yaml_conn = get_db_con()
    breakpoint()

