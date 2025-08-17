# Create a dictionary of students and their scores

students_score = {
    "Hilal":34,
    "Ameen":41,
    "Zain":45,
    "Hain":48,
    "Ihan":50
    }

students_score["Mehthab"] =46

print(students_score)

for i,j in students_score.items():
    print(f"{i}:{j}")

# Merge two dictionaries

students_score2 = {
    "Muhammed":50,
    "Ayisha":40,
    "Umar":35,
}

all_score = {**students_score, **students_score2}
print(all_score)