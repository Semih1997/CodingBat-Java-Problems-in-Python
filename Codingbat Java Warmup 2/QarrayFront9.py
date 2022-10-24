def arrayFront9(a):
    correction = False
    if len(a) < 4:
        for x in a:
            if x == 9:
                correction = True
    else:
        for x in a[:4]:
            if x == 9:
                correction = True
    return correction
test_inputs = [[1, 2, 9, 3, 4],[1, 2, 3, 4, 9],[1, 2, 3, 4, 5],[9, 2, 3],[1, 9, 9],[1, 2, 3],[1, 9],[5, 5],[2],[9],[],[3,9,2,3,3]]
expected = [True,False,False,True,True,False,True,False,False,True,False,True]
all_correct = True
for i in range(len(expected)):
    if arrayFront9(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)