
from Persistence import Dictionnary
from Persistence.DatabaseConnectionConfig import DatabaseConnectionConfig


def getOutgoingAccountNumber(outgoingAccountName):
    accounts = Dictionnary.getAccounts()
    for (accountId, accountName) in accounts:
        if accountName.lower().__eq__(outgoingAccountName.lower()):
            return accountId


def getExpenseTypeNumber(expenseTypeName):
    expenses = Dictionnary.getExpenseColumns()
    for (expenseId, expenseName) in expenses:
        if expenseName.lower().__eq__(expenseTypeName.lower()):
            return expenseId


class ExpenseEntity:

    def __init__(self, bookingDate, bookingAmount, bookingPurpose, outgoingAccountName, expenseTypeName):
        self.bookingDate = bookingDate
        self.bookingAmount = bookingAmount
        self.bookingPurpose = bookingPurpose
        self.outgoingAccount = getOutgoingAccountNumber(outgoingAccountName)
        self.expenseType = getExpenseTypeNumber(expenseTypeName)

        self.databaseConnector = DatabaseConnectionConfig().setupConnector("finance")

    def insert(self):
        if self.expenseType is None or self.outgoingAccount is None:
            raise Exception(self.bookingPurpose + " could not be inserted cause of None value")
        else:
            tableName = "Kostenbuchungen"
            statement = "INSERT INTO %s " \
                        "(buchungsbetrag, kostenart, buchungsdatum, ausgangskonto, buchungszweck)" \
                        "VALUES (%s, %s, '%s', %s, '%s')" % \
                        (tableName, self.bookingAmount, self.expenseType, self.bookingDate, self.outgoingAccount, self.bookingPurpose)
            cursor = self.databaseConnector.cursor()
            cursor.execute(statement)
            self.databaseConnector.commit()
            cursor.close()


