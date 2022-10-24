def scores100(a):
    control_100 = False
    for i in range(len(a)-1):
        if a[i] == 100 and a[i+1] == 100:
            control_100 = True
    return control_100
test_inputs = [[1, 100, 100],[1, 100, 99, 100],[100, 1, 100, 100],[100, 1, 100, 1],[1, 2, 3, 4, 5],[1, 2, 100, 4, 5]]
expected = [True,False,True,False,False,False]
all_correct = True
for i in range(len(expected)):
    if scores100(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)