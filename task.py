#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Good Luck

class Client:
    first_name = ""
    last_name = ""

    def __init__(self, name_set, last_nam_set):
        self.first_name = name_set
        self.last_name = last_nam_set
    
    def print_client(self):
        print(self.first_name, self.last_name)
       

class Bank:
    client_list = {}
    bank_name = ""

    def __init__(self, bank_name_set):
        self.bank_name = bank_name_set

    def print_bank(self):
        print(self.bank_name)
        
    def add_client(self, client_to_add, his_money = 0):
        self.client_list.update( {client_to_add : his_money } )

    # money_change > 0 if input money_change < 0 if withdraw
    def cash_change(self, client, money_change):
        self.client_list[client] += money_change
        
    def transfer(self, client_from, client_to, money_change):
        if(self.client_list[client_from] < money_change ):
            return NULL
        
        self.client_list[client_from] -= money_change
        self.client_list[client_to] += money_change
        
    def print_clients(self):
        print("PRINTING CLIENT LIST")
        for client, money in self.client_list.items():
            client.print_client()
            print(money)
            print("=================")
            

if __name__ == "__main__":
    bank_alior = Bank("alior")
    bank_alior.print_bank()

    client_kowalski = Client("Jan", "Kowalski")
    client_nowak = Client("Andrzej", "Nowak")
    
    bank_alior.add_client(client_kowalski, 1000)
    bank_alior.add_client(client_nowak)

    bank_alior.print_clients()    
    
    bank_alior.cash_change(client_nowak, 2000)
    bank_alior.print_clients()
   
    bank_alior.transfer(client_nowak, client_kowalski, 500)
    bank_alior.print_clients()