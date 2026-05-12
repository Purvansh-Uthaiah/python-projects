class Expense :
    def __init__(self,name,category,amount) :
        self.name = name
        self.category = category
        self.amount = amount

class Tracker:
    def __init__(self) :
        self.all_expenses = []
        self.category = {
            1: "Food" ,
            2: "Health" ,
            3: "Fitness" ,
            4: "Transportation" ,
            5: "Shopping",
            6: "Clothes",
            7: "Investments",
            8: "Others",
            9: "view Expenses",
            10: "Exit"
        }
    def show_menu(self):
         while True:
            print("1 -> Food")
            print("2 -> Health ")
            print("3 -> Fitness")
            print("4 -> Transportation ")
            print("5 -> shopping")
            print("6 -> clothes")
            print("7 -> Investments")
            print("8 -> Others... ")
            print("9 -> view Expenses ")
            print("10 -> Exit")

            try:
              category = int(input("Enter your category: "))
            except:
              print("Invalid input! Enter the number of the category to proceed")
              continue

            if category >=1 and category <= 8:
              self.add_expense(category)
            elif category == 9:
              self.view_expenses()
              break
            else:
              break

    def add_expense(self,category) :
              name = input("Enter the name of the item : ")

              amount = float(input("Enter the amount of the item : ₹ "))


              category_name = self.category[category]
              new_expense = Expense(name,category_name,amount)
              self.all_expenses.append(new_expense)

    def view_expenses(self) :
        category_total = {}
        for exp in self.all_expenses :
         print(f"{exp.name:<15} | {exp.category:<15} | ₹{exp.amount}")

         if exp.category in category_total:
            category_total[exp.category] += exp.amount
         else:
             category_total[exp.category] = exp.amount

        total = sum(exp.amount for exp in self.all_expenses)
        print(f"\n Total Expenses : ₹ {total}")

        print("\n category_wise Total: ")
        for category, amount in category_total.items() :
           print(f"{category:<15} | ₹{amount}")


tracker = Tracker()
tracker.show_menu()%  