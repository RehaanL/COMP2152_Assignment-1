"""
#Author: Rehaan Lachporia
#Assignment: #1
"""


# Step b: Create 4 variables
gym_member = "Alex Alliton"  #String
preferred_weight_kg = 20.5  #Float
highest_reps = 25  #Int
membership_active = True  #Boolean


# Step c: Create a dictionary named workout_stats
#Data type: Dictionary
workout_stats = {
    "Alex": (30, 40, 50),
    "Jamie": (20, 30, 40),
    "Taylor": (10, 20, 30),
}


# Step d: Calculate total workout minutes using a loop and add to dictionary
temp = {}
for item in workout_stats:
    name = f"{item}_Total"
    total = sum(workout_stats[item])
    temp.update({name: total})

workout_stats.update(temp)


# Step e: Create a 2D nested list called workout_list
#Data type: List/Array
workout_list = []
#going through each key in the workout_stats dictionary
for item in workout_stats:
    #checking if that key contains a tuple datatype
    if isinstance(workout_stats[item], tuple):
        #creating temp array to store each tuple value
        temp = []
        #adding each value into the temp array
        temp.extend(workout_stats[item])
        #adding the temp array to the workout_list array
        workout_list.append(temp)


# Step f: Slice the workout_list
#Part f.1
n=0
for item in workout_stats:
    if isinstance(workout_stats[item], tuple):
        name = item
        print(f"{name}: Yoga minutes",workout_list[n][0], "| Running minutes", workout_list[n][1])
        n+=1

#Part f.2
w=0
for item in workout_stats:
    if isinstance(workout_stats[item], tuple):
        if w == 0:
            w+=1
        else:
            name = item
            print(f"{name}: Weightlifting minutes",workout_list[w][2])
            w+=1


# Step g: Check if any friend's total >= 120
for item in workout_stats:
    if isinstance(workout_stats[item], int):
        if workout_stats[item] >= 120:
            print(f"Great job staying active, {item.removesuffix('_Total')}")


# Step h: User input to look up a friend
friend_name = input("Please enter your friends name:")
#verifying the input in case user types wrong
validated_string = friend_name.capitalize()
if validated_string in workout_stats:
    print(f"{validated_string}: Yoga minutes",
          workout_stats[validated_string][0],
          "| Running minutes", workout_stats[validated_string][1],
          "| Weightlifting minutes", workout_stats[validated_string][2],
          "| Total Workout Minutes", workout_stats[f"{validated_string}_Total"])
else:
    print(f"Friend {validated_string} not found in the records")


# Step i: Friend with highest and lowest total workout minutes
temp = []
for item in workout_stats:
    if isinstance(workout_stats[item], int):
        temp.append([workout_stats[item],f"{item.removesuffix('_Total')}"])

sorted_array = sorted(temp)

print(f"Friend with the highest total workout minutes: {sorted_array[-1][1]} --> {sorted_array[-1][0]}")
print(f"Friend with the lowest total workout minutes: {sorted_array[0][1]} --> {sorted_array[0][0]}")
