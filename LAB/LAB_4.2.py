import statistics

# All students' marks for 4 subjects: English, Mother Tongue, Math, Science
# Ah Boy is the first student (index 0)
students_marks = [
    [60, 70, 90, 80],  # Ah Boy
    [90, 50, 85, 75],
    [35, 55, 70, 60],
    [85, 75, 85, 95],
    [70, 60, 70, 55],
    [50, 40, 75, 65]
]

# Subject names
subjects = ['English', 'Mother Tongue', 'Math', 'Science']

# Get Ah Boy's marks (first student)
ah_boy = students_marks[0]

# We will store Ah Boy's T-scores here
t_scores = []

# Go through each subject one by one
for subject_index in range(4):
    # Get all students' marks for this subject
    subject_marks = [student[subject_index] for student in students_marks]
    
    # Calculate average (mean) and standard deviation (spread)
    average = statistics.mean(subject_marks)
    std_dev = statistics.stdev(subject_marks)
    
    # Ah Boy's mark for this subject
    ah_boy_mark = ah_boy[subject_index]
    
    # Calculate T-score using the formula
    t = 50 + 10 * (ah_boy_mark - average) / std_dev
    t_scores.append(t)

    # Print T-score for this subject
    print(f"{subjects[subject_index]} T-score: {t:.0f}") #change number to 2 for 2dp

# Calculate total PSLE score
total_psle = sum(t_scores)
print(f"Total PSLE Score:",round(total_psle,0)) 
