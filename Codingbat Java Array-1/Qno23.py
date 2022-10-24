def no23(a):
    correction = True
    if (a[0] == 2 or a[0] == 3 or a[1] == 2 or a[1] == 3):
        correction = False
    return correction
test_inputs = [[4, 5],[4, 2],[3, 5],[1, 9],[2, 9],[1, 3],[1, 1],[2, 2],[3, 3],[7, 8],[8, 7]]
expected = [True,False,False,True,False,False,True,False,False,True,True]
all_correct = True
for i in range(len(expected)):
    if no23(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)  