from Persistence.Transaction import Transaction

incomingAccount = "Comdirecte"
outgoingAccount = "kasse"
amount = 720
description = "test"
transaction = Transaction(incomingAccount, outgoingAccount, amount, description)

transaction.transfer()
