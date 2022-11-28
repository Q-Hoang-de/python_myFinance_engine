from datetime import datetime

from Persistence.IncomeEntity import IncomeEntity

bookingDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
bookingAmount = 300.00
bookingPurpose = "test"
incomingAccountName = "Visa kredit"
incomeTypeName = "Gehalt"

income = IncomeEntity(bookingAmount, bookingDate, bookingPurpose, incomeTypeName, incomingAccountName)
income.insert()