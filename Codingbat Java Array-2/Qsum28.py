def sum28(a):
    sum_28 = 0
    control_8 = False
    for i in range(len(a)):
        if a[i] == 2:
            sum_28 += 2
    if sum_28 == 8:
        control_8 = True
    return control_8
test_inputs = [[2, 3, 2, 2, 4, 2],[2, 3, 2, 2, 4, 2, 2],[1, 2, 3, 4],[2, 2, 2, 2],[1, 2, 2, 2, 2, 4],[],[2],[8],[2, 2, 2],[2, 2, 2, 2, 2],[5, 2, 2, 2, 4, 2]]
expected = [True,False,False,True,True,False,False,False,False,False,True]
all_correct = True
for i in range(len(expected)):
    if sum28(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)