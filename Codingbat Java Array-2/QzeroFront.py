def zeroFront(a):
    last_list = []
    for i in range(len(a)):
        if a[i] == 0:
            last_list.append(a[i])
    for i in range(len(a)):
        if a[i] != 0:
            last_list.append(a[i])
    return last_list
test_inputs = [[1, 0, 0, 1],[0, 1, 1, 0, 1],[1, 0],[0, 1],[1, 1, 1, 0],[2, 2, 2, 2],[0, 0, 1, 0],[-1, 0, 0, -1, 0],[],[9, 9, 0, 9, 0, 9]]
expected = [[0, 0, 1, 1],[0, 0, 1, 1, 1],[0, 1],[0, 1],[0, 1, 1, 1],[2, 2, 2, 2],[0, 0, 0, 1],[0, 0, 0, -1, -1],[],[0, 0, 9, 9, 9, 9]]
all_correct = True
for i in range(len(expected)):
    if zeroFront(test_inputs[i]) != expected[i]:
        print(test_inputs[i])
        all_correct = False
print("All Correct: ", all_correct)