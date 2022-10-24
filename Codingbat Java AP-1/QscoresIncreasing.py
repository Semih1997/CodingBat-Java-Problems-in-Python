def scoresIncreasing(a):
    control_scores = True
    for i in range(len(a)-1):
        if not(a[i] <= a[i+1]):
            control_scores = False
    return control_scores
test_inputs = [[1, 3, 4],[1, 3, 2],[1, 1, 4],[1, 1, 2, 4, 4, 7],[1, 1, 2, 4, 3, 7],[-5, 4, 11]]
expected = [True,False,True,True,False,True]
all_correct = True
for i in range(len(expected)):
    if scoresIncreasing(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)