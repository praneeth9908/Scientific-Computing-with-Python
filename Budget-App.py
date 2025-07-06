import math
class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = []

    def __str__(self):
        title = self.category.center(30,'*') + '\n'
        ledgers = ''
        total = 0
        for i in self.ledger:
            total += i['amount']
            ledgers += i['description'][:23].ljust(23)
            ledgers += f"{i['amount']:.2f}".rjust(7) + '\n'
        total = f"Total: {total:.2f}"
        return title + ledgers + total


    def deposit(self,amount, description =""):
        self.ledger.append({'amount':amount,'description':description})
    
    def withdraw(self,amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,'description':description})
            return True
        return False

    def get_balance(self):
        return sum(i['amount'] for i in self.ledger)

    def transfer(self, amount, otherCategory):
        if self.withdraw(amount, f"Transfer to {otherCategory.category}"):
            otherCategory.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
            

food = Category('Food')
food.deposit(1000,'deposit')
food.withdraw(100.15,'groceries')
food.withdraw(115.89,'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.deposit(1000,'deposit')
clothing.withdraw(400,'pant')


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Step 1: Calculate total spent and individual spends
    spent_per_category = []
    total_spent = 0
    for cat in categories:
        spent = sum(-entry['amount'] for entry in cat.ledger if entry['amount'] < 0)
        spent_per_category.append((cat.category, spent))
        total_spent += spent

    # Step 2: Calculate percentages rounded down to nearest 10
    percentages = [math.floor((spent / total_spent) * 10) * 10 for _, spent in spent_per_category]

    # Step 3: Construct the bar chart (0 to 100)
    chart = ""
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Step 4: Add the horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Step 5: Add category names vertically
    max_len = max(len(name) for name, _ in spent_per_category)
    names = [name.ljust(max_len) for name, _ in spent_per_category]

    for i in range(max_len):
        chart += "     "  # 5 spaces
        for name in names:
            chart += name[i] + "  "
        if i != max_len - 1:
            chart += "\n"

    return title + chart



lst = []
lst.append(food)
lst.append(clothing)

print(create_spend_chart(lst))
