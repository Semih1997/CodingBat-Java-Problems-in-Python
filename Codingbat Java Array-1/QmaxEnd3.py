def maxEnd3(a):
    if a[0] < a[2]:
        a = [a[2],a[2],a[2]]
    else:
        a = [a[0],a[0],a[0]]
    return a
test_inputs = [[1, 2, 3],[11, 5, 9],[2, 11, 3],[11, 3, 3],[3, 11, 11],[2, 2, 2],[2, 11, 2],[0, 0, 1]]
expected = [[3, 3, 3],[11, 11, 11], [3, 3, 3],[11, 11, 11],[11, 11, 11], [2, 2, 2], [2, 2, 2],[1, 1, 1]]
all_correct = True
for i in range(len(expected)):
    if maxEnd3(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(maxEnd3(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)