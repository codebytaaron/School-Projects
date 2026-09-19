# Grade calculator program

student_name = "Teddy"

# list of test scores
scores = [85, 90, 78, 92, 88]

total = 0

# add up all scores
for score in scores:
    total = total + score

# calculate average
average = total / len(scores)

# find highest score
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score

# find lowest score
lowest = scores[0]
for score in scores:
    if score < lowest:
        lowest = score

# determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

# print results
print("Student:", student_name)
print("Scores:", scores)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Final Grade:", grade)

# extra check
if average > 100:
    print("Invalid scores entered")
