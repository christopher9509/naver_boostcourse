# Quiz 3.

from this import s
from unittest import result

score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    for i, stu_score in enumerate(score):
        print('{0}번, 평균 : {1}'.format(i+1, (stu_score[0] + stu_score[1])/2 ))

print(get_avg(score))

