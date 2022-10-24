def fix45(a):
    indexes_5 = []
    indexes_4 = []
    for i in range(len(a)):
        if a[i] == 5:
            indexes_5.append(i)
        if a[i] == 4:
            indexes_4.append(i)
    for i in range(len(indexes_4)):
        j = a[indexes_4[i]+1]
        a[indexes_4[i]+1] = 5
        a[indexes_5[i]] = j
    return a
test_inputs = [[5, 4, 9, 4, 9, 5],[1, 4, 1, 5],[1, 4, 1, 5, 5, 4, 1],[4, 9, 4, 9, 5, 5, 4, 9, 5],[5, 5, 4, 1, 4, 1],[4, 2, 2, 5],[1, 1, 1],[4, 5],[5, 4, 1],[]]
expected = [[9, 4, 5, 4, 5, 9],[1, 4, 5, 1],[1, 4, 5, 1, 1, 4, 5],[4, 5, 4, 5, 9, 9, 4, 5, 9],[1, 1, 4, 5, 4, 5],[4, 5, 2, 2],[1, 1, 1],[4, 5],[1, 4, 5],[]]
all_correct = True
for i in range(len(expected)):
    if fix45(test_inputs[i]) != expected[i]:
        print(test_inputs[i],fix45(test_inputs[i]))
        all_correct = False
print("All Correct: ", all_correct)