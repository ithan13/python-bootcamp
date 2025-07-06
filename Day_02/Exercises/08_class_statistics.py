student_scores = [98,75,100,86,100,3]

lowest_score = min(student_scores)
print(lowest_score)

highest_score = max(student_scores)
print(highest_score)

total_score = sum(student_scores)
data_qty = len(student_scores)
print(f"Average is",total_score/data_qty)

ranking = sorted(student_scores)
print(ranking)

ranking = sorted(student_scores,reverse=True)
print(ranking)

