#Author: Edward Inegbenosun
#Purpose: Exercise 1


#create input veriables with correct types
name = str(input("Enter the athlete's name: "))
low_dive = float(input(f"Enter the Low Dive score for {name}: "))
high_dive = float(input(f"Enter the High Dive score for {name}: "))
free_dive = float(input(f"Enter the Free Dive score for {name}: "))

#Calculate total and use to get average
total = low_dive + high_dive + free_dive
avg = total/3

#variables for the list
event= "Event"
score = "Score"
low = "Low Dive"
high = "High Dive"
free = "Free Dive"
tot = "Total points"
average = "Average score"

#output formatted list
print(f"{name} results")
print(f"{event:18}{score:2}")
print('-'*25)
print(f"{low:18}{low_dive:2}")
print(f"{high:18}{high_dive:2}")
print(f"{free:18}{free_dive:2}")
print('='*25)
print(f"{tot:18}{total:2}")
print(f"{average:18}{avg:2,.2f}")