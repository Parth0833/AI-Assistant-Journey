your_friends = {"Rahul", "Amit", "Neha"}
other_person = {"Neha", "Priya", "Karan"}

# 1. Mutual friends: Elements present in BOTH sets (Intersection)
mutual_friends=your_friends.intersection(other_person)  

# 2. New friends: People in the other person's list who aren't your friends yet (Set Difference)
new_friends=other_person.difference(your_friends)  

# Display Results
print("Mutual friends:", mutual_friends)
print("New friends to suggest:", new_friends)