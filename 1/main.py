"""
Step 1:

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. 
As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, 
the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. 
that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Step 2:

Find the top 3 carrying the most calories, how many calories are they carrying?

"""


with open("input.txt", encoding = 'utf-8') as f:
   raw_input = f.read()
   elfs = raw_input.split("\n\n")
   
elfs_dict = {}
for i,elf in enumerate(elfs):
    total_cal = 0
    calories = elf.split("\n")
    for cal in calories:
        total_cal = total_cal + int(cal)
    elfs_dict[i] = total_cal   
    
most_calories = max(elfs_dict,key=elfs_dict.get)
total_cal_list = list(elfs_dict.values())
total_cal_list.sort(reverse=True)
top_three_total_cal = total_cal_list[0]+total_cal_list[1]+total_cal_list[2]
print(f"Elf carrying most calories is elf {most_calories} who carries:{elfs_dict[most_calories]} calories.")
print(f"Top three elfs are carrying: {top_three_total_cal} calories.")