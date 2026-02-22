class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    
    

class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(name + " is already in the network.")
        else:
            new_person = Person(name)
            self.people[name] = new_person

    def add_friendship(self, name1, name2):
        # check if both people exist
        if name1 not in self.people or name2 not in self.people:
            print("Friendship not created. One or both people don't exist.")
            return

        person1 = self.people[name1]
        person2 = self.people[name2]

        # add each other as friends
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name in self.people:
            person = self.people[name]
            friend_names = []

            for friend in person.friends:
                friend_names.append(friend.name)

            print(name + " is friends with: " + ", ".join(friend_names))



# Test your code here
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Duplicate test
network.add_person("Alex")

# Add friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Alex", "Taylor")
network.add_friendship("Jordan", "Johnny")  # person doesn't exist

network.print_network()