class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewares_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewares_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self
    def enroll(self):
        if self.is_rewares_member == True:
            print("User already a member.")
        else: 
            self.is_rewares_member = True
            self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough points.")
        else:
            self.gold_card_points -= amount
        return self
Bobby = User("Bobby", "Smith", "bobby@gmail.com", 30)
Maria = User("Maria", "Morina", "murrmurr@gmail.com", 45)
Bean = User("Bean", "Bartie", "beanie@gmail.com", 21)
Bobby.display_info().enroll().spend_points(50).display_info().enroll()
Maria.enroll().spend_points(80).display_info()
Bean.display_info().spend_points(40)