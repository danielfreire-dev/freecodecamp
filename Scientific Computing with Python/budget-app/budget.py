class Category:
    def __init__(self, name):
        self.name=name
        self.ledger=[]
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount,'description': description})
      
    def withdraw(self, amount, description=""):
       
        if (self.check_funds(amount)):
            self.ledger.append({'amount': -amount,'description': description})
            return True
        else:
            return False
        
    def get_balance(self):
        get_balance=0
        for i in range(len(self.ledger)):
           get_balance+=self.ledger[i]['amount']
        return get_balance
    
    def get_withdraw(self):
        get_withdraw = self.ledger[0]['amount']-self.get_balance()
        return get_withdraw
    
    def transfer(self, amount, category):
        if (self.check_funds(amount)):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}" )
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if self.get_balance()>= amount:
            return True
        else:
            return False
    
    def __str__(self):
        string_title = self.name
        string_ledger= string_title.center(30, '*') +'\n'
        for i in self.ledger:
            string_ledger+=f'{i.get("description")[:23]:23}' + f'{i.get("amount"):7.2f}' + '\n'
        string_ledger+= f'Total: {self.get_balance()}'
        

        return string_ledger



def create_spend_chart(categories):
    
    chart = 'Percentage spent by category\n'
    withdrawals = []
    for name in categories:
        withdrawals.append(name.get_withdraw())
        
    percent_withdrawal = [round(i / sum(withdrawals) * 100) for i in withdrawals]
    names = [cat.name.lower().capitalize() for cat in categories]
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percent_withdrawal:
            chart += "o  " if percent >= i else "   "
        chart += "\n"

    chart += ' ' * 4 + '-' * (2 * (len(categories) + 1) + 2)
    max_len = len(max(names, key=len))
    names = [i.ljust(max_len) for i in names]
    for i in range(max_len):
        chart += '\n     '
        for name in names:
            chart += name[i] + '  '

    return chart