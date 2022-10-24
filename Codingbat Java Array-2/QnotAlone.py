def notAlone(a,b):
    if len(a) > 2:
        control_a = a[1:len(a)-1]
        for i in range(len(control_a)):
            if control_a[i] == b and (a[i] != control_a[i] and a[i+2] != control_a[i]):
                if a[i] < a[i+2]:
                    a[i+1] = a[i+2]
                else:
                    a[i+1] = a[i]
    return a
test_inputs = [[1, 2, 3],[1, 2, 3, 2, 5, 2],[3, 4],[1, 3, 1, 2],[],[7, 1, 6],[1, 1, 1],[1, 1, 1, 2]]
other_test_inputs = [2,2,3,1,3,1,1,1]
expected = [[1, 3, 3],[1, 3, 3, 5, 5, 2],[3, 4],[1, 3, 3, 2],[],[7, 7, 6],[1, 1, 1],[1, 1, 1, 2]]
all_correct = True
for i in range(len(expected)):
    if notAlone(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)