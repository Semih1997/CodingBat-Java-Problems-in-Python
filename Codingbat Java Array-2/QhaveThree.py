def haveThree(a):
    control_have_3 = False
    count_3 = 0
    i = 0
    while i < len(a):
        if a[i] == 3:
            i += 2
            count_3 += 1
        else:
            i += 1
    if count_3 == 3:
        control_have_3 = True
    return control_have_3
test_inputs = [[3, 1, 3, 1, 3],[3, 1, 3, 3],[3, 4, 3, 3, 4],[1, 3, 1, 3, 1, 2],[1, 3, 1, 3, 1, 3],[1, 3, 3, 1, 3],[1, 3, 1, 3, 1, 3, 4, 3],[3, 4, 3, 4, 3, 4, 4],[3, 3, 3],[1, 3],[3],[1]]
expected = [True,False,False,False,True,False,False,True,False,False,False,False]
all_correct = True
for i in range(len(expected)):
    if haveThree(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)