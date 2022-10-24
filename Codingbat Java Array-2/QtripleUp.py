def tripleUp(a):
    control_tripleUp = False
    if len(a) > 2:
        for i in range(len(a) - 2):
            if a[i] + 1 == a[i+1] and a[i] + 2 == a[i+2]:
                control_tripleUp = True
    return control_tripleUp
test_inputs = [[1, 4, 5, 6, 2],[1, 2, 3],[1, 2, 4],[1, 2, 4, 5, 7, 6, 5, 6, 7, 6],[1, 2, 4, 5, 7, 6, 5, 7, 7, 6],[1, 2],[1],[],[10, 9, 8, -100, -99, -98, 100],[10, 9, 8, -100, -99, 99, 100],[-100, -99, -99, 100, 101, 102],[2, 3, 5, 6, 8, 9, 2, 3]]
expected = [True,True,False,True,False,False,False,False,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if tripleUp(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)