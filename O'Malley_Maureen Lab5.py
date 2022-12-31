#The number of calories that are burned each minute on the treadmill
#is first assigned to the variable "burnedPerMinute".
burnedPerMinute = 4.2

#The table headings are printed.
print("Minutes\tCalories Burned")
print("------------------------")

#The for loop displays the minutes passed and how many calories will
#be burned by the specified time.
for minutes in range(10, 31, 5):
    caloriesBurned = minutes * burnedPerMinute
    print(minutes, "\t", caloriesBurned)
