import tweepy
import math
import pgeocode


class Volunteer:
    
    def __init__(self, name, postal_code):
        self.name = name
        self.postal_code = postal_code
        self.distance = -1 #default value
        
    def say_hi(self):
        print("Hi, I am " + self.name)
        
class Recipient(Volunteer):
    def __init__(self,name, postal_code, grocery_list):
        self.grocery_list = grocery_list
        self.name = name
        self.postal_code = postal_code
        self.distance = -1 #default value

    def print_list(self):
        for item in self.grocery_list:
            print(item)


recip_list = [
    Recipient('Alice','B1T 1Y9',['apples','bananas','oranges']),
    Recipient('Bob','H7X 0J4',['apples','bananas','oranges']),
    Recipient('Carson','E5S 6K1',['apples','bananas','oranges']),
    Recipient('Dale','V1L 1E5',['apples','bananas','oranges']),
    Recipient('Elon','J0M 3L1',['apples','bananas','oranges'])
]

def calc_distance(volunteer, recip_list, country = 'CA'): #calculates distance for each postal code and then returns a sorted list
    dist = pgeocode.GeoDistance(country) 
    for recipient in recip_list:
        recipient.distance = math.ceil(dist.query_postal_code(volunteer.postal_code, recipient.postal_code))
    
    recip_list.sort(key= lambda x: x.distance, reverse=True)
    return

vol1 = Volunteer('Fred','L5K 2M3')

calc_distance(vol1, recip_list)

for i in recip_list: 
    print(str(i.distance) + '  ' + i.name)

print(recip_list.pop())

print('\n\n')

for i in recip_list: 
    print(str(i.distance) + '  ' + i.name)
