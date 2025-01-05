import random
import time
import math
import os

class Game:
    def __init__(self):
        self.balance = 1000  # Initial capital
        self.bitscrap_amount = 0  # Amount of BitScrap owned
        self.bitscrap_price = 50000  # Initial BitScrap price
        self.game_over = False

    def display_status(self):
        print(f"\nCurrent balance: ${self.balance:.1f}")
        print(f"You own {self.bitscrap_amount:.4f} BitScrap worth ${self.bitscrap_amount * self.bitscrap_price:.2f}")
        print(f"Current BitScrap price: ${self.bitscrap_price:.2f}")

    def buy_bitscrap(self):
        print("\nBuying BitScrap...")
        try:
            amount_to_spend = float(input(f"You have ${self.balance:.1f}. How much do you want to spend on BitScrap? "))
            if amount_to_spend > self.balance:
                print("You don't have enough funds!")
            else:
                bitscrap_bought = amount_to_spend / self.bitscrap_price
                self.bitscrap_amount += bitscrap_bought
                self.balance -= amount_to_spend
                print(f"You bought {bitscrap_bought:.4f} BitScrap.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def sell_bitscrap(self):
        print("\nSelling BitScrap...")
        try:
            amount_to_sell = float(input(f"You have {self.bitscrap_amount:.4f} BitScrap. How much do you want to sell? "))
            if amount_to_sell > self.bitscrap_amount and not math.isclose(amount_to_sell, self.bitscrap_amount, rel_tol=1e-9):
                print("You don't have enough BitScrap to sell!")
            else:
                self.bitscrap_amount -= amount_to_sell
                self.balance += amount_to_sell * self.bitscrap_price
                print(f"You sold {amount_to_sell:.4f} BitScrap.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def random_event(self):
        event_type = random.choice(['up', 'down'])
        change_percentage = random.uniform(0.01, 0.1)  # Price change from 1% to 10%

        if event_type == 'up':
            self.bitscrap_price *= (1 + change_percentage)
        else:
            self.bitscrap_price *= (1 - change_percentage)

        print(f"Market event: BitScrap price {'increased' if event_type == 'up' else 'decreased'} by {change_percentage * 100:.2f}%")

    def mine_bitscrap(self):
        mined_bitscrap = random.uniform(0.001, 0.01)
        self.bitscrap_amount += mined_bitscrap
        print(f"You mined {mined_bitscrap:.4f} BitScrap.")

    def play(self):
        while not self.game_over:
            os.system('cls')
            self.display_status()
            print("\n1. Buy BitScrap")
            print("2. Sell BitScrap")
            print("3. Check market situation")
            print("4. Mine BitScrap")
            print("5. End game")

            choice = input("Choose an action: ")
            os.system('cls')
            if choice == '1':
                self.buy_bitscrap()
            elif choice == '2':
                self.sell_bitscrap()
            elif choice == '3':
                self.random_event()
            elif choice == '4':
                self.mine_bitscrap()
            elif choice == '5':
                print("Thank you for playing!")
                self.game_over = True
            else:
                print("Invalid choice! Try again.")

            time.sleep(2)

if __name__ == "__main__":
    game = Game()
    game.play()