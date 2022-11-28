import Dictionnary
from DatabaseConnectionConfig import DatabaseConnectionConfig


def getIncomeTypeId(incomeTypeName):
    incomeTypes = Dictionnary.getIncomeColumns()
    for incomeTypeId, incomeName in incomeTypes:
        if incomeName.lower().__eq__(incomeTypeName.lower()):
            return incomeTypeId


def getIncomingAccountId(incomingAccountName):
    accounts = Dictionnary.getAccounts()

    for accountId, accountName in accounts:
        if incomingAccountName.lower().__eq__(accountName.lower()):
            return accountId


class IncomeEntity:
    def __init__(self, bookingAmount, bookingDate, bookingPurpose, incomeTypeName, incomingAccountName):
        self.bookingAmount = bookingAmount
        self.bookingDate = bookingDate
        self.bookingPurpose = bookingPurpose
        self.incomeType = getIncomeTypeId(incomeTypeName)
        self.incomingAccount = getIncomingAccountId(incomingAccountName)
        self.databaseConnector = DatabaseConnectionConfig().setupConnector("finance")

    def insert(self):
        cursor = self.databaseConnector.cursor()
        table = "Erloesbuchungen"
        statement = "INSERT INTO %s (buchungsbetrag, eingangskonto, buchungsdatum, buchungszweck, erloesart) " \
                    "VALUES (%s, %s, '%s', '%s', %s)" % (table, self.bookingAmount, self.incomingAccount, self.bookingDate, self.bookingPurpose, self.incomeType)

        cursor.execute(statement)
        self.databaseConnector.commit()
        cursor.close()
