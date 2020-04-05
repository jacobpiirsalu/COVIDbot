import tweepy
import math
import pgeocode



# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("pGBDoAaEpkliVKBOLwjtcmHGc", 
#     "xF3g1wrP50b6BlZEd20u4oVfjgH1FGQcuWUzlQO5aUWOufvlhw")
# auth.set_access_token("622518493-6VcLIPprbQbv9wkcBBPvCle8vsjU9fE85Dq9oStl", 
#     "tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq")

# api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")


class Volunteer:
    
    def __init__(self, name, postal_code):
        self.name = name
        self.postal_code = postal_code
        
    def say_hi(self):
        print("Hi, I am " + self.name)
        
class Recipient(Volunteer):
    def __init__(self,name, postal_code, grocery_list):
        self.grocery_list = grocery_list
        self.name = name
        self.postal_code = postal_code

    def print_list(self):
        for item in self.grocery_list:
            print(item)

lista = [
    'H7Y 9E6',
    'H7X 0J4',
    'G3E 4G0',
    'J9B 4R6',
    'J0L 0T2',
    'K7C 0H5'
]
listb = [
    'E7P 2L2',
    'G0A 5S8',
    'E5S 6K1',
    'V1L 1E5',
    'R7N 9S6',
    'J0M 3L1'
]
dist = pgeocode.GeoDistance('CA')
print(dist.query_postal_code(lista, listb))
# user1 = Volunteer("John","2658 Hammond Rd")
# user2 = Recipient("Jill", "2777 Hammond Rd",['apples','bananas','oranges'])

# user2.print_list()

# print(user1.name)
# user1.name = "joe"
# print(user1.name)

# print(user2.address)


