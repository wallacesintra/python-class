# write
scores = list()
n = eval(input("enter the number of students: "))
for i in range (0,n):
    score = eval(input("enter the score for student {0}".format(i+1)))
    scores.append(score)
print(scores)

# mean
totalscore = sum(scores)
mean = totalscore/n
print("the mean score is {0}".format(mean))

