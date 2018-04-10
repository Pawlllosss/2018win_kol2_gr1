# Banking simulator. Write a code in python that simulates the banking system.
# The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
# If you can thing of any other features, you can add them.
# This code shoud be runnable with 'python kol1.py'.
# You don't need to use user input, just show me in the script that the structure of your code works.
# If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
# Do your best, show off with good, clean, well structured code - this is more important than number of features.
# After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
# Good Luck

import json
from pathlib import Path

def moneyTransfer(banksDictionary, clientFromTransferValue, **clients):
    if (clientFromTransferValue < 0):
        return None

    if changeClientBalance(banksDictionary, -clientFromTransferValue, *clients["clientFrom"]) is not False:
        changeClientBalance(banksDictionary, clientFromTransferValue, *clients["clientTo"])

# pass bankName, clientName, lastName, moneyChange
def changeClientBalance(banksDictionary, clientFromTransferValue, *clientData):
    if (len(clientData) != 3):
        return False

    clientBank = banksDictionary.get(clientData[0])

    if clientBank is None:
        return False

    clientNameTuple = (clientData[1], clientData[2])

    clientMoney = clientBank.get(clientNameTuple)
    if clientMoney is not None and (clientMoney + clientFromTransferValue) >= 0:
        clientBank[clientNameTuple] += clientFromTransferValue
    else:
        return False

def printBankClients(bankName, banksDictionary):
    bankClientsDictionary = banksDictionary.get(bankName)

    if bankClientsDictionary is None:
        return None

    print("Clients of the bank: ", bankName)

    for client, money in bankClientsDictionary.items():
        print(client[0], "\t", client[1], "\t", money)

def printAllBanks(banksDictionary):
    for bankName in banksDictionary:
        printBankClients(bankName, banksDictionary)


# it creates a list in this format { (Name, LastName) : money ] , ... ]
def createClients():
    clientsDictionary = {}
    # here you create a new client until you don't write any name
    while True:
        clientString = input("[name],[last name],[moneyBalance]: ")

        if (clientString == ""):
            return clientsDictionary

        # check if split works correctly
        name, lastName, moneyBalance = clientString.split(",")

        clientsDictionary[(name, lastName)] = int(moneyBalance)

def createBanks(banksDictionary):
    # here you create new banks until you don't write any name
    while True:
        bankName = input("Bank name: ")
        if (bankName.strip() == ""):
            return banksDictionary

        clientsDictionary = createClients()
        banksDictionary[bankName] = clientsDictionary

def writeToJson(banksDictionary):
    #I need to convert tuple to string as json supports only string as a key
    with open("banksDictionary.json", "w") as file:
        json.dump(
            {bank: {"_".join(name): money for name, money in clients.items()} for bank, clients in banksDictionary.items()}
            , file)

def readFromJson():
    fileName="banksDictionary.json"

    if Path(fileName).is_file():
        with open(fileName, "r") as file:
            dataReceived = json.load(file)
        return {bank: {tuple(name.split("_")): money for name, money in clients.items()} for bank, clients in dataReceived.items()}

    return {}

    print(dataReceived)

if __name__ == "__main__":

    banksDictionary = readFromJson()
    createBanks(banksDictionary)
    # withdraw money
    changeClientBalance(banksDictionary, -300, "PKO", "Andrzej", "Golota")
    printBankClients("PKO", banksDictionary)

    moneyTransfer(banksDictionary, 1500, clientFrom=["PKO", "Andrzej", "Golota"], clientTo=["PKO", "Stefan", "Batory"])
    printBankClients("PKO", banksDictionary)

    printAllBanks(banksDictionary)

    writeToJson(banksDictionary)

