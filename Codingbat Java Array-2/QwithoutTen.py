def withoutTen(a):
    last_list = []
    for i in range(len(a)):
        if a[i] != 10:
            last_list.append(a[i])
    for i in range(len(a)):
        if a[i] == 10:
            last_list.append(0)
    return last_list
test_inputs = [[1, 10, 10, 2],[10, 2, 10],[1, 99, 10],[10, 13, 10, 14],[10, 13, 10, 14, 10],[10, 10, 3],[1],[13, 1],[10],[]]
expected = [[1, 2, 0, 0],[2, 0, 0],[1, 99, 0],[13, 14, 0, 0],[13, 14, 0, 0, 0],[3, 0, 0],[1],[13, 1],[0],[]]
all_correct = True
for i in range(len(expected)):
    if withoutTen(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)