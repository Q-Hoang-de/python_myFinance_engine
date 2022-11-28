import Dictionnary
from DatabaseConnectionConfig import DatabaseConnectionConfig


def getAccountId(givenAccountName):
    accounts = Dictionnary.getAccounts()

    for accountId, accountName in accounts:
        if accountName.lower().__eq__(givenAccountName.lower()):
            return accountId


class Transaction:
    def __init__(self, incomingAccount, outgoingAccount, amount, description):
        self.description = description
        self.amount = amount
        self.incomingAccountId = getAccountId(incomingAccount)
        self.outgoingAccountId = getAccountId(outgoingAccount)

        self.databaseConnector = DatabaseConnectionConfig().setupConnector("finance")

    def transfer(self):
        tableName = "Transaction"
        statement = "INSERT INTO %s (eingangskonto, ausgangskonto, betrag, beschreibung) " \
                    "VALUES (%s, %s, %s, '%s')" % \
                    (tableName, self.incomingAccountId, self.outgoingAccountId, self.amount, self.description)
        cursor = self.databaseConnector.cursor()
        cursor.execute(statement)
        self.databaseConnector.commit()
        cursor.close()