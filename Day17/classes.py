class User:
    def __init__(self, id, company):
        print("new user being created")
        self.id = id
        self.corporation = company  # doesn't have to match
        self.followers = 0

    def follow(self, user):
        user.followers += 1


user_2 = User("002", "GlobeCorp")
print(user_2.corporation)


user_1 = User("001", "Goog")
user_1.id = 1
user_1.name = "Jimone"

print(user_1.name)


def function():
    pass


user_2.follow(user_1)
print(user_1.followers)
