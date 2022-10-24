def commmonEnd(a,b):
    if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
        return True
    else:
        return False
test_inputs = [[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3]]
other_test_inputs = [[7, 3],[7, 3, 2],[1, 3],[1],[2]]
expected = [True,False,True,True,False]
all_correct = True
for i in range(len(expected)):
    if commmonEnd(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)