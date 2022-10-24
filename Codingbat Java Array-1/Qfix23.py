def fix23(a):
    for x in range(len(a)-1):
        if a[x] == 2 and a[x+1] == 3:
            a[x+1] = 0
    return a
test_inputs = [[1, 2, 3],[2, 3, 5],[1, 2, 1],[3, 2, 1],[2, 2, 3],[2, 3, 3]]
expected = [[1, 2, 0],[2, 0, 5],[1, 2, 1],[3, 2, 1],[2, 2, 0],[2, 0, 3]]
all_correct = True
for i in range(len(expected)):
    if fix23(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)