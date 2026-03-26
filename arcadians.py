#OOP classes
class Card:
    #Parent class other card types will inherit from/it is the base class
    def _init_(self, arcade_login, status="Exists"):
        self.arcade_login=arcade_login
        self.status=status
class Arcade_card(Card):
    #inherits from Dard class
    total_cards_created=0
    total_doubloons_added=0
    total_games_played=0
    total_doubloons_spent=0

    def _init_(self, privateer, arcade_login, doubloons=0):
        #this part called when new arcaed card made
        super()._init_(arcade_login, "Exists")
        self.privateer=privateer
        self.doubloons=doubloons

        #tracking card info
        self.total_individual_topups=0 #number of topups
        self.total_individual_games=0 #how many games played usibg card
        self.total_individual_spent=0 #how much money used up

        Arcade_card.total_cards_created +=1
        Arcade_card.total_doubloons_added+=doubloons

    def view(self):
        #shows profile stuff
        print(f"Name: {self.privateer}")
        print(f"Card ID: {self.arcade_login}")
        print(f"Balance: {self.doubloons} doubloons")
        print(f"Status: {self.status}")
        print()#just for empty line spacing

    def view_detailed_stats(self):
        #shows money wise stuff
        print(f"\n----Detailed Statistics for {self.privateer}--")
        print(f"Card ID: {self.arcade_login}")
        print(f"Current Balance: {self.doubloons} doubloons")
        print(f"Total Top-ups: {self.total_individual_topups}")
        print(f"Total Games Played: {self.total_individual_games}")
        print(f"Total Doubloons spent: {self.total_individual_spent}")
        print(f"Status: {self.status}")
        print()

    def top_up(self, balance):#adding more doubloons
        #checking for card
        if self.status !="Exists":
            print("Sorry, we are unable to add credits at this time due to your card being blocked")
            return False
        
        #checking if amount is valid
        if balance <=0:
            print("Sorry but the amount must be positive")
            return False
        
        #addind balance
        self.doubloons += balance
        #updating stats
        self.total_individual_topups +=1
        Arcade_card.total_doubloons_added += balance

        
        

    



