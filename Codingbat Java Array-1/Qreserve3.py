def reserve3(a):
    a = [a[2],a[1],a[0]]
    return a
test_inputs = [[1, 2, 3],[5, 11, 9],[7, 0, 0],[2, 1, 2],[1, 2, 1],[2, 11, 3],[0, 6, 5],[7, 2, 3]]
expected = [[3, 2, 1],[9, 11, 5], [0, 0, 7],[2, 1, 2], [1, 2, 1],[3, 11, 2],[5, 6, 0], [3, 2, 7]]
all_correct = True
for i in range(len(expected)):
    if reserve3(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)
