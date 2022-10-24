def sameFirstLast(a):
    control = False
    if len(a) == 0:
        control = False
    else:
        if a[0] == a[len(a)-1]:
            control = True
    return control
test_inputs = [[1, 2, 3],[1, 2, 3, 1],[1, 2, 1],[7],[],[1, 2, 3, 4, 5, 1],[1, 2, 3, 4, 5, 13],[13, 2, 3, 4, 5, 13],[7, 7]]
expected = [False,True,True,True,False,True,False,True,True]
all_correct = True
for i in range(len(expected)):
    if sameFirstLast(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)