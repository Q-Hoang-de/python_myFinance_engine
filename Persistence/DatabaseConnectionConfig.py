import mysql.connector


class DatabaseConnectionConfig:
    def __init__(self):
        self.host = "localhost"
        self.user = "hoang"
        self.password = "hoangquynh"
        self.loginMode = "mysql_native_password"

    def setupConnector(self, databaseName):
        connector = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=databaseName,
            auth_plugin=self.loginMode)
        return connector
