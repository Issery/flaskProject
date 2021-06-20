USERNAME = 'lancer'
PASSWORD = 'Lrd19970323'
HOSTNAME = 'test1-server.database.windows.net'
PORT = 3306
DATABASE = 'test1database'

DB_URI = 'mssql+pymssql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
new_uri = 'mssql+pyodbc://sa:password@localhost/TestDB?driver=ODBC+Driver+13+for+SQL+Server'
app_config = 'mssql+pyodbc://lancer:Lrd19970323@test1-server.database.windows.net/test1database?driver=ODBC+Driver+17+for+SQL+Server&charset=utf8'
