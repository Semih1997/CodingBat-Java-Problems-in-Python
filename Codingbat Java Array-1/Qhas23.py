def has23(a):
    correction = False
    if (a[0] == 2 or a[0] == 3 or a[1] == 2 or a[1] == 3):
        correction = True
    return correction
test_inputs = [[2, 5],[4, 3],[4, 5],[2, 2],[3, 2],[3, 3],[7, 7],[3, 9],[9,5]]
expected = [True,True,False,True,True,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if has23(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)