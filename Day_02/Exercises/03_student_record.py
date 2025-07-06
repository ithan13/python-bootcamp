# student_names = ("Juan","Maria","Joseph")
# student_scores = (70,90,81)
#
# for student_name,student_score in zip(student_names,student_scores):
#     print(f"Student",student_name,"scored",student_score,"in the exam")

student_names = ("Juan","Maria","Joseph")
student_scores = (70,90,81)

for index,(student_name,student_score) in enumerate(zip(student_names,student_scores), start=1):
    print(f"Student",index,student_name,"scored",student_score,"in the exam")
