from Persistence.DatabaseConnectionConfig import DatabaseConnectionConfig

database = "finance"
mydb = DatabaseConnectionConfig().setupConnector(database)


def getExpenseColumns():
    tableName = "Kostenarten"
    statement = "SELECT kostenartenId, kostenartenName FROM %s" % tableName
    cursor = mydb.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    cursor.close()
    return result


def getIncomeColumns():
    tableName = "Erloesarten"
    statement = "SELECT erloesartenId, erloesartenName FROM %s" % tableName
    cursor = mydb.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    cursor.close()
    return result


def getAccounts():
    tableName = "Konto"
    statement = "SELECT kontoId, kontoName FROM %s" % tableName
    cursor = mydb.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    cursor.close()
    return result
