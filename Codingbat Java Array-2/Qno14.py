def no14(a):
    control_no_14 = True
    if (1 in a) and (4 in a):
        control_no_14 = False
    return control_no_14
test_inputs = [[1, 2, 3],[1, 2, 3, 4],[2, 3, 4],[1, 1, 4, 4],[2, 2, 4, 4],[2, 3, 4, 1],[2, 1, 1],[1, 4],[1],[4],[1, 1, 1, 1]]
expected = [True,False,True,False,True,False,True,False,True,True,True]
all_correct = True
for i in range(len(expected)):
    if no14(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)