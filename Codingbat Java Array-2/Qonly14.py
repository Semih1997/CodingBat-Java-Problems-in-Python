def only14(a):
    control_14 = True
    for i in range(len(a)):
        if a[i] != 4 and a[i] != 1:
            control_14 = False
    return control_14
test_inputs = [[1, 4, 1, 4],[1, 4, 2, 4],[1, 1],[4, 1],[2],[],[1, 4, 1, 3],[1, 1, 1, 5],[4, 1, 4, 1]]
expected = [True,False,True,True,False,True,False,False,True]
all_correct = True
for i in range(len(expected)):
    if only14(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)