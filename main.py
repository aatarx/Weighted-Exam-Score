# Weighted Exam Score Average

# Entering how many exams you have

number_of_exams = int(input("Enter Number of Exams: "))

# Entering how many credit these exams cover
total_credits = int(input("Enter how many credits these exams cover: "))

# Begin with average of 0 and then add up percentages from each exam
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter Exam Score: "))
    exam_credits = int(input("Enter how many credit this exam covered: "))
    average = average + score*exam_credits/total_credits

    print("Your average is", average)