def unlucky1(a):
    correction = False
    if len(a) > 2:
        for x in range(len(a)-1):
            if x < 2:
                if a[x] == 1 and a[x+1] ==  3:
                    correction = True
            if x > len(a)-3:
                if a[x] == 1 and a[x+1] == 3:
                    correction = True
    elif len(a) == 2:
        if a[0] == 1 and a[1] == 3:
            correction = True
    return correction
test_inputs = [[1, 3, 4, 5],[2, 1, 3, 4, 5],[1, 1, 1],[1, 3, 1],[1, 1, 3],[1, 2, 3],[3, 3, 3],[1, 3],[1, 4],[1],[],[1, 1, 1, 3, 1],[1, 1, 3, 1, 1],[1, 1, 1, 1, 3],[1, 4, 1, 5],[1, 1, 2, 3],[2, 3, 2, 1],[2, 3, 1, 3],[1, 2, 3, 4, 1, 3]]
expected = [True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True]
all_correct = True
for i in range(len(expected)):
    if unlucky1(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)