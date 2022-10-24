def biggerTwo(a,b):
    if sum(a) < sum(b):
        return b
    elif sum(b) < sum(a):
        return a
    else:
        return a
test_inputs = [[1, 2],[3, 4],[1, 1],[2, 1],[2, 2],[1, 3],[6, 7]]
other_test_inputs = [[3, 4],[1, 2],[1, 2],[1, 1],[1, 3],[2, 2],[3, 1]]
expected = [[3, 4],[3, 4],[1, 2],[2, 1],[2, 2],[1, 3],[6, 7]]
all_correct = True
for i in range(len(expected)):
    if biggerTwo(test_inputs[i],other_test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
    