def noTriples(a):
    control = True
    if len(a) < 3:
        return control
    for x in range(len(a)-2):
        if a[x] == a[x+1] == a[x+2]:
            control = False
    return control
test_inputs = [[1, 1, 2, 2, 1],[1, 1, 2, 2, 2, 1],[1, 1, 1, 2, 2, 2, 1],[1, 1, 2, 2, 1, 2, 1],[1, 2, 1],[1, 1, 1],[1, 1],[1],[]]
expected = [True,False,False,True,True,False,True,True,True]
all_correct = True
for i in range(len(expected)):
    if noTriples(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)