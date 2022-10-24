def has12(a):
    control_2_exist = False
    if 1 in a:
        first_place_1 = a.index(1)
        a = a[first_place_1:]
        for i in range(len(a)):
            if a[i] == 2:
                control_2_exist = True
    return control_2_exist
test_inputs = [[1, 3, 2],[3, 1, 2],[3, 1, 4, 5, 2],[3, 1, 4, 5, 6],[3, 1, 4, 1, 6, 2],[2, 1, 4, 1, 6, 2],[2, 1, 4, 1, 6],[1],[2, 1, 3],[2, 1, 3, 2],[2],[3, 2],[3, 5, 1]]
expected = [True,True,True,False,True,True,False,False,False,True,False,False,False]
all_correct = True
for i in range(len(expected)):
    if has12(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)