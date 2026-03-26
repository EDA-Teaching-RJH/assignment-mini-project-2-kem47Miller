#OOP classes
class Card:
    #Parent class other card types will inherit from/it is the base class
    def __init__(self, arcade_login, status="Exists"):
        self.arcade_login=arcade_login
        self.status=status
class Arcade_card(Card):
    #inherits from Card class
    total_cards_created=0
    total_doubloons_added=0
    total_games_played=0
    total_doubloons_spent=0

    def __init__(self, privateer, arcade_login, doubloons=0):
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


    @property
    def privateer(self):
        #hetter for player name
        return self._privateer
    @privateer.setter
    def privateer(self, value):
        #setter for player name
        self._privateer= value
    @property
    def arcade_login(self):
        #getter for card ID
        return self.arcade_login
    @arcade_login.setter
    def acrade_login(self, value):
        #setter for card id
        self._arcade_login= value
    @property
    def doubloons(self):
        #getter for balance
        return self._doubloons
    @doubloons.setter
    def doubloons(self, value):
        #setter to ensure balance is valid
        if value >=0:
            self._doubloons= value
        else:
            print("Sorry but your balance can't be negative")
    @property
    def status(self):
        #getter  for status
        return self._status
    @status.setter
    def status(self, value):
        #setter to check if stauts is valid
        if value in ["Exist", "Blocked"]:
            self._status= value
        else:
            print("Invalid status")
    @property
    def total_individual_topups(self):
        #getter for individual top-ups
        return self._total_individual_topups
    @total_individual_topups.setter
    def total_individual_topups(self, value):
        #setter for individual top ups
        self._total_individual_topups= value
    @property
    def total_individual_games(self):
        #getter for each game
        return self._total_individual_games
    @total_individual_games.setter
    def total_individual_games(self, value):
        """Setter for individual games"""
        self._total_individual_games = value

    @property
    def total_individual_spent(self):
        #getter for individual spent
        return self._total_individual_spent

    @total_individual_spent.setter
    def total_individual_spent(self, value):
        #setter for individual spent
        self._total_individual_spent = value
    @property
    def total_cards_all_time(self):
        #Returns total cards ever created
        return Arcade_card.total_cards_created

    @property
    def total_doubloons_all_time(self):
        #Returns total doubloons ever added
        return Arcade_card.total_doubloons_added

    @property
    def total_games_all_time(self):
        #Returns total games ever played
        return Arcade_card.total_games_played
    @property
    def total_spent_all_time(self):
        #Returns total doubloons ever spent
        return Arcade_card.total_doubloons_spent


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
        print(f"New balance: {self.doubloons}")
        return True 
    
    def pricing(self, price):#cal balance after player buy game
        #check if card blocked
        if self.status != "Exists":
            print("Sorry, but your card appears to be blocked")#tells them they ac't play game
            return False
        
        #check if balance is enough
        if self.doubloons >= price:
            self.doubloons -=price#carry through with purchase and subtract price

            #update changes to stats
            self.total_individual_games +=1
            self.total_individual_spent +=price
            Arcade_card.total_games_played +=1
            Arcade_card.total_doubloons_spent += price
            print(f"Balance is now: {self.doubloons}")
            return True
        else:
            print("Balance is insufficient")
            return False
        
    def block(self):
        #prevent card from top-ups and gaming by cahnging status to blocked
        self.status="Blocked"
        print(f"Sorry but the card for {self.arcade_login} has been blocked")

    def unblock(self):
        #changes status back to "Exists", unblocking users card
        self.status="Exists"
        print(f"Good news, {self.arcade_login} your card has been unblocked")

    




        
        

    



