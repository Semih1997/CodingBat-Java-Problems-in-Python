def swapEnds(a):
    first_index = a[0]
    last_index = a[len(a)-1]
    a[0] = last_index
    a[len(a)-1] = first_index
    return a
test_inputs = [[1, 2, 3, 4],[1, 2, 3],[8, 6, 7, 9, 5],[3, 1, 4, 1, 5, 9],[1, 2],[1]]
expected = [[4, 2, 3, 1],[3, 2, 1],[5, 6, 7, 9, 8],[9, 1, 4, 1, 5, 3],[2, 1],[1]]
all_correct = True
for i in range(len(expected)):
    if swapEnds(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        print(swapEnds(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)