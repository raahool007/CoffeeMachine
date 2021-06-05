# Write your code here


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.coffee = 120
        self.milk = 540
        self.money = 550
        self.cups = 9

    def print_current_state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def buy_an_espresso(self):
        if self.water < 250:
            print("Sorry, not enough water!")
        elif self.coffee < 16:
            print("Sorry, not enough coffee!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            self.water -= 250
            self.coffee -= 16
            self.money += 4
            self.cups -= 1
            print("I have enough resources, making you a coffee!")

    def buy_a_latte(self):

        if self.water < 350:
            print("Sorry, not enough water!")
        elif self.coffee < 20:
            print("Sorry, not enough coffee!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")

    def buy_a_cappuccino(self):
        if self.water < 200:
            print("Sorry, not enough water!")
        elif self.coffee < 100:
            print("Sorry, not enough coffee!")
        elif self.milk < 12:
            print("Sorry, not enough milk!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.money += 6
            self.cups -= 1
            print("I have enough resources, making you a coffee!")

    def fill_machine(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans you want to add:"))
        self.cups += int(input("Write how many disposable coffee cups you want to add:"))

    def take_money(self):
        print("I gave you", self.money)
        self.money = 0

    def buy_a_coffee(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == "1":
            self.buy_an_espresso()
        elif choice == "back":
            pass
        elif choice == "2":
            self.buy_a_latte()
        else:
            self.buy_a_cappuccino()

    def interface(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "exit":
                break
            elif action == "buy":
                self.buy_a_coffee()
            elif action == "remaining":
                self.print_current_state()
            elif action == "fill":
                self.fill_machine()
            else:
                self.take_money()


coffeemachine = CoffeeMachine()
coffeemachine.interface()