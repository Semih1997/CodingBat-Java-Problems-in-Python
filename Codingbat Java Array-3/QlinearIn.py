def linearIn(a,b):
    control_In = False
    list_control = []
    for i in range(len(b)):
        if b[i] in a:
            list_control += "x"
    if len(list_control) == len(b):
        control_In = True
    return control_In
test_inputs = [[1, 2, 4, 6],[1, 2, 4, 6],[1, 2, 4, 4, 6],[2, 2, 4, 4, 6, 6],[2, 2, 2, 2, 2],[2, 2, 2, 2, 2],[2, 2, 2, 2, 4],[1, 2, 3],[1, 2, 3],[1, 2, 3],[-1, 0, 3, 3, 3, 10, 12]]
other_test_inputs = [[2, 4],[2, 3, 4],[2, 4],[2, 4],[2, 2],[2, 4],[2, 4],[2],[-1],[],[0, 3, 12, 14]]
expected = [True,False,True,True,True,False,True,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if linearIn(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i],i)
        all_correct = False
print("All Correct: ", all_correct)