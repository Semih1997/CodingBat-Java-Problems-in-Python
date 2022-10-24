def double23(a):
    correction = False
    if len(a) > 1:
        if (a[0] == 2 and a[1] == 2) or (a[0] == 3 and a[1] == 3):
            correction = True
    return correction
test_inputs = [[2, 2],[3, 3],[2, 3],[3, 2],[4, 5],[2],[3],[],[3,4]]
expected = [True,True,False,False,False,False,False,False,False,]
all_correct = True
for i in range(len(expected)):
    if double23(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)