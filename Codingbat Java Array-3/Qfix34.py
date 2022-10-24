def fix34(a):
    indexes_4 = []
    indexes_3 = []
    for i in range(len(a)):
        if a[i] == 4:
            indexes_4.append(i)
        if a[i] == 3:
            indexes_3.append(i)
    for i in range(len(indexes_3)):
        j = a[indexes_3[i]+1]
        a[indexes_3[i]+1] = 4
        a[indexes_4[i]] = j
    return a
test_inputs = [[1, 3, 1, 4],[1, 3, 1, 4, 4, 3, 1],[3, 2, 2, 4],[3, 2, 3, 2, 4, 4],[2, 3, 2, 3, 2, 4, 4],[5, 3, 5, 4, 5, 4, 5, 4, 3, 5, 3, 5],[3, 1, 4],[3, 4, 1],[1, 1, 1],[1],[],[7, 3, 7, 7, 4],[3, 1, 4, 3, 1, 4],[3, 1, 1, 3, 4, 4]]
expected = [[1, 3, 4, 1],[1, 3, 4, 1, 1, 3, 4],[3, 4, 2, 2],[3, 4, 3, 4, 2, 2],[2, 3, 4, 3, 4, 2, 2],[5, 3, 4, 5, 5, 5, 5, 5, 3, 4, 3, 4],[3, 4, 1],[3, 4, 1],[1, 1, 1],[1],[],[7, 3, 4, 7, 7],[3, 4, 1, 3, 4, 1],[3, 4, 1, 3, 4, 1]]
all_correct = True
for i in range(len(expected)):
    if fix34(test_inputs[i]) != expected[i]:
        print(test_inputs[i],fix34(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)