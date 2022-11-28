# 'Abonement','Fastfood','Freizeit','Hauseinrichtungen','Kosmetik','Sonstige Gebühr',
# 'Lebensmittels','Miete','Sport','Technik','Telefon','Versicherung','Urlaub','Studium','Mobilität',
# 'Klamotten','Sonstiges','Staatliche Abgabe','Lebensunterhalt','Gesundheit'

from Persistence.ExpenseEntity import ExpenseEntity
from datetime import datetime
import pandas as pd

df = pd.read_csv("test.csv", sep=';')
for index, row in df.iterrows():
    bookingDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bookingAmount = row["amount"]
    bookingPurpose = row["bookingPurpose"]
    outgoingAccountName = row["outgoingAccount"]
    expenseTypeName = row["expenseType"]

    expense = ExpenseEntity(bookingDate, bookingAmount, bookingPurpose, outgoingAccountName, expenseTypeName)

    expense.insert()
