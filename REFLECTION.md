Kem47, Kezia Miller,23028873

---


My miniproject is a code for a pirate themed arcade that allows players to create accounts and use said account to play games. The program saves data to a csv file and then exports it to a text file.

---

Reference

We learned about importing and using libraries in the lecture 7. Having learned this I used the `re` library for regex and `statistics` for calculations. I also created my own library called `custom.py` which contains my validation functions.


In week 8 we learned about OOP. I made a `Card` class as my parent class and `Arcade_card` as my sub class. This was hard at first but eventually it worked.


We learned about pattern matching in week 9. I used regex to check if card IDs are in the right format (PIRT followed by 5 numbers) and to validate player names.


This week we learned about reading and writing files. I used this to save card data to `pirate.csv` and export reports to `arcade_report.txt`.


We learned about testing code. I made test functions to check if my top_up and play_game methods work correctly.

---

Problems I had

CSV Files
I struggled the most with CSV files. At first, I didn't understand how to read the data and turn it back into card objects. But I referred to the lecture notes for help to understand.

super().__init__():
I also struggled with `super().__init__()` because I didn't understand it at first. I didn't know why I needed to call the parent class. I referred to workshop to helped me understand that I should set up the card_id and status from the Card class before adding player name and balance.Eg:


class Card:
    def __init__(self, arcade_login, status="Exists"):
        self.arcade_login = arcade_login
        self.status = status

class Arcade_card(Card):
    def __init__(self, privateer, arcade_login, doubloons=0):
        super().__init__(arcade_login, "Exists")  # This was confusing at first
        self.privateer = privateer
        self.doubloons = doubloons

---

How My Code Works

1. When the program starts, it loads any existing cards from `pirate.csv`
2. The menu lets users create cards, add credits, play games, and block/unblock cards
3. All data is stored in memory while the program runs
4. When users choose to save and exit, the program writes all cards back to `pirate.csv`
5. Users can also export a readable report to `arcade_report.txt`

---

