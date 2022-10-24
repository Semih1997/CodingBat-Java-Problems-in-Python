def isEverywhere(a,b):
    control_b = True
    if len(a) > 1:
        for i in range(len(a)-1):
            if a[i] != b and a[i+1] != b:
                control_b = False
    return control_b
test_inputs = [[1, 2, 1, 3],[1, 2, 1, 3],[1, 2, 1, 3, 4],[2, 1, 2, 1],[2, 1, 2, 1],[2, 1, 2, 3, 1],[3, 1],[3, 1],[3],[],[1, 2, 1, 2, 3, 2, 5],[2, 1, 2, 2, 2, 1, 1, 2]]
other_test_inputs = [1,2,1,1,2,2,3,2,1,165465,2,2]
expected = [True,False,False,True,True,False,True,False,True,True,True,False]
all_correct = True
for i in range(len(expected)):
    if isEverywhere(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)