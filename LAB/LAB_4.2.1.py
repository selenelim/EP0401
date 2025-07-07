import numpy as np

# All students' marks (rows = students, columns = subjects)
students_marks = np.array([
    [60, 70, 90, 80],  # Ah Boy
    [90, 50, 85, 75],
    [35, 55, 70, 60],
    [85, 75, 85, 95],
    [70, 60, 70, 55],
    [50, 40, 75, 65]
])

# Subject names
subjects = ['English', 'Mother Tongue', 'Math', 'Science']

# Ah Boy's marks (first row)
ah_boy = students_marks[0]

# Calculate mean and standard deviation for each subject (column-wise)
means = np.mean(students_marks, axis=0)
stds = np.std(students_marks, axis=0, ddof=1)  # ddof=1 for sample std deviation

# Calculate T-scores
t_scores = 50 + 10 * (ah_boy - means) / stds

# Print T-scores for each subject
for i in range(4):
    print(f"{subjects[i]} T-score: {t_scores[i]:.2f}")

# Total PSLE score
total_psle = np.sum(t_scores)
print(f"\nTotal PSLE Score: {total_psle:.2f}")
