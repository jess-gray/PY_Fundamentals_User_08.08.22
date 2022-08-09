class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self):
        if self.is_rewards_member == True: 
            return "already a member"
        self.is_rewards_member = True
        self.gold_card_points = self.gold_card_points + 200

    def spend_points(self,amount):
        if self.gold_card_points < (amount):
            return("not enough points")
        
        self.gold_card_points = self.gold_card_points - (amount)
        return self.gold_card_points
    
    

Amy = User('Amy','Gray','agray@yahoo.com',53)
Lori = User('Lori', 'Poland', 'lpoland@gmail.com', 21)
Linda = User('Linda', 'Poland', 'LindaPoland@gmail.com', 25)


Amy.enroll()
print(Amy.spend_points(250))
print(Amy.is_rewards_member)
Amy.display_info()

Lori.enroll()
print(Lori.spend_points(50))

Linda.enroll()
print(Linda.spend_points(80))

Lori.display_info()
Linda.display_info()