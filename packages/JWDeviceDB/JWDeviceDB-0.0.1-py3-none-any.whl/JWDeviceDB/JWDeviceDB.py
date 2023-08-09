import configparser
import sqlite3


class JWDeviceError(Exception):

    def __init__(self, value):
        self.value = value


class JWDeviceEntry:

    hostname = None
    ip = None
    device_type = None

    def __init__(self, _hostname=None, _ip=None, _device_type=None):
        self.hostname = _hostname
        self.ip = _ip
        self.device_type = _device_type

    def __str__(self):
        return(f'\'{self.hostname}\', \'{self.ip}\', \'{self.device_type}\'')

    def __repr__(self):
        return(f'{self.__class__.__name__}(\'{self.hostname}\', \'{self.ip}\', \'{self.device_type}\')')


class JWDeviceDB:

    results = None
    entries = []
    config = None
    host_regex = None
    ip_regex = None

    def __init__(self, _config=None, _host_regex=None, _ip_regex=None):
        self.config = _config
        self.host_regex = _host_regex
        self.ip_regex = _ip_regex

        # print(f'host_regex = {self.host_regex}')
        # print(f'ip_regex = {self.ip_regex}')

        if (self.config == None):
            raise JWDeviceError('ERROR: Config file not specified')

        if (self.host_regex == None and self.ip_regex == None):
            raise JWDeviceError('ERROR: Need to specify host_regex OR ip_regex')

        if (self.host_regex):
            self.host_regex = self.host_regex.split(' ')
        if (self.ip_regex):
            self.ip_regex = self.ip_regex.split(' ')

        try:
            cfg = configparser.ConfigParser()
            valid = cfg.read(self.config)
            if not valid:
                raise JWDeviceError('ERROR: Config file does not exist')
        except configparser.Error:
            raise JWDeviceError('ERROR: Invalid config file')

        try:
            SQLDB = cfg.get('DevicesDB', 'path')
        except configparser.Error:
            raise JWDeviceError('ERROR: Section/Option error in config file')

        try:
            db = sqlite3.connect(f'file:{SQLDB}?mode=ro', uri=True)
        except sqlite3.Error:
            raise JWDeviceError('ERROR: Error opening DB file')

        sql_query = None
        if (self.host_regex):
            sql_query = 'Hostname NOT NULL'
            for i in self.host_regex:
                sql_query += f' AND Hostname LIKE "%{i}%"'

        if (self.ip_regex):
            if (sql_query == None):
                sql_query = 'MgmtIP NOT NULL'
            for i in self.ip_regex:
                sql_query += f' AND MgmtIP LIKE "%{i}%"'

        try:
            cursor = db.cursor()
            sql_query = f'SELECT * FROM Devices WHERE {sql_query} ORDER BY Hostname ASC'
            # print(sql_query)
            cursor.execute(sql_query)
            rows = cursor.fetchall()
        except sqlite3.Error:
            raise JWDeviceError('ERROR: Sqlite DB query error')

        # print(f'len rows == {len(rows)}')
        self.results = len(rows)
        for row in rows:
            # print(row)
            entry = JWDeviceEntry(row[0], row[1], row[2])
            self.entries.append(entry)


    def __len__(self):
        return self.results


    def __getitem__(self, i):
        if ((i >= 0) and (i < self.results)):
            return(self.entries[i])
        return(None)

