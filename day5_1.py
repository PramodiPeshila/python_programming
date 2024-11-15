#find max score and sum

score = [23,56,78,98,50,25,70,12,28,94,20]

# method 1

max_score = max(score)
print(f"Maximum Score = {max_score}")

total_score = sum(score)
print(f"Total Score = {total_score}")

# method 2
stu_score = 0
for value in score:
    if value > stu_score :
        stu_score = value

print(f"Maximum Score (Method 2) = {stu_score}")

total = 0
for value in score:
    total += value

print(f"Total Score (Method 2) = {total}")


