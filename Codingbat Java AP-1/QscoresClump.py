def scoresClump(a):
    control_clumpy = False
    for i in range(len(a)-2):
        if a[i+2] - a[i] <= 2:
            control_clumpy = True
    return control_clumpy
test_inputs = [[3, 4, 5],[3, 4, 6],[1, 3, 5, 5],[2, 4, 5, 6],[2, 4, 5, 7],[2, 4, 4, 7],[3, 3, 6, 7, 9],[3, 3, 7, 7, 9],[4, 5, 8]]
expected = [True,False,True,True,False,True,False,True,False]
all_correct = True
for i in range(len(expected)):
    if scoresClump(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)